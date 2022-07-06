import os
from selenium.webdriver.common.by import By
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from tweetCard import tweetCard
from localPassword import getPasswd , getUserName
from time import sleep
from datetime import datetime
from myLog import funcLogger
from threading import Thread
import logging
from downloader import mediaDownloader
from queue import Queue
from tweetVid import tweetVid
"""
The only interface to users
Only high level action can be done.
high level action is defined to execute a specific task ( like download all the tweet in current site, add all the friends , display certain tweet , search for specific tweets for download )
high level action can be separate into {browserAction part} and {infomation part}
{infomation part} will control multiple threads responsible for separate tweet , download pic , download vid separately
"""
class tweetEngine:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s-%(levelname)s:%(name)s:%(message)s",level=logging.ERROR)
        self.finishFlagQueue = Queue()
        self.mediaDownloadTaskQueue = Queue()
        self.openDownloader()
        self.vidDownloaderThread = Thread(target=self.listenM3u8Request,daemon=True)

    # login 
    def loginToTwitter(self,headless=False):
        # instance
        # options = Options()
        # options.headless = True
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("permissions.default.image",2)
        # profile.set_preference("media.autoplay.blocking_policy",2)
        # driver = webdriver.Firefox(firefox_profile=profile)
        seleniumOptions = {
                'proxy' : {
                    'http': "http://127.0.0.1:7890",
                    'https': "http://127.0.0.1:7890",
                    "no_proxy": "localhost,127.0.0.1"
                    }
                }
        options = Options()
        options.headless = headless
        driver = webdriver.Firefox(seleniumwire_options=seleniumOptions,options = options)
        self.driver = driver
        driver.get("http://www.twitter.com/login")

        # Login userName
        userNameElement = self.find_element("//input[@name='text']")
        userNameElement.clear()
        userNameElement.send_keys(getUserName())
        userNameElement.send_keys(Keys.RETURN)

        # Login password
        passWordElement = self.find_element("//input[@name='password']")
        passWordElement.clear()
        passWordElement.send_keys(getPasswd())
        passWordElement.send_keys(Keys.RETURN)
    #

    def openDownloader(self):
        self.picDownloaderThread = Thread(target=mediaDownloader.mediaDownloader,args=[self.mediaDownloadTaskQueue,self.finishFlagQueue],daemon=True)
        self.picDownloaderThread.start()

    def closeDownloader(self):
        self.finishFlagQueue.put(True)

    # search for info
    def turnToSearchPageOf(self,info):
        searchBar = self.find_element("//input[@aria-label='Search query']")
        searchBar.clear()
        searchBar.send_keys(info)
        searchBar.send_keys(Keys.RETURN)

        # come to latest tab
        self.find_element("//span[contains(text(),'Latest')]").click()

    def clickProfile(self):
        self.find_element("//span[contains(text(),'Profile')]").click

    def clickLikes(self):
        self.find_element("//span[contains(text(),'Likes')]").click


    def enterPersonalLikes(self):
        self.find_element("//span[contains(text(),'Profile')]").click()
        self.find_element("//span[contains(text(),'Likes')]").click()

    @funcLogger
    def scrollPageDown(self,lastPosition,tryTime = 2):
        while tryTime > 0:
            # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.execute_script("window.scrollBy(0,6 * window.innerHeight);")
            currentPosition = self.driver.execute_script("return window.pageYOffset;")
            sleep(1)
            success = not (lastPosition == currentPosition)
            if success:
                return True
            else:
                tryTime = tryTime - 1
        return False

    def getAllTheCurrentArticalSession(self):
        articleSessions = self.find_elements("//article[@data-testid='tweet']")
        return articleSessions

    def downloadMultiMediaPart(self,tweet):
        pics = tweet.pics
        for pic in pics:
            self.finishFlagQueue.put(False)
            self.mediaDownloadTaskQueue.put(pic)
        GIFs = tweet.GIFs
        for GIF in GIFs:
            self.finishFlagQueue.put(False)
            self.mediaDownloadTaskQueue.put(GIF)

    def getCurrentPosition(self):
        return self.driver.execute_script("return window.pageYOffset;")

    def downloadAllTheTweetsInThePage(self):
        self.vidDownloaderThread.start()
        self.tweets = []
        try:
            while True:
                lastPosition = self.getCurrentPosition()
                articleSessions = self.getAllTheCurrentArticalSession()
                for articleSession in articleSessions:
                    tweet = tweetCard(articleSession)
                    if self.tweetNotVisitYet(self.tweets,tweet):
                        self.tweets.append(tweet)
                    self.downloadMultiMediaPart(tweet)
                    sleep(1)
                if not self.scrollPageDown(lastPosition):
                    break
        except Exception as e:
            logging.exception(f"Catch exception In {__name__}")
        return self.tweets

    def tweetNotVisitYet(self,tweets,tweet):
        for tt in tweets:
            if tt.tweetDocument["fileName"] == tweet.tweetDocument["fileName"]:
                return False
        return True

    def find_element(self,xPathValue,baseElement=None):
        if not baseElement == None:
            return baseElement.find_element(by=By.XPATH,value=xPathValue)
        wait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,xPathValue)))
        return self.driver.find_element(by=By.XPATH,value=xPathValue)

    def find_elements(self,xPathValue,baseElement=None):
        if not baseElement == None:
            return baseElement.find_element(by=By.XPATH,value=xPathValue)
        wait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,xPathValue)))
        return self.driver.find_elements(by=By.XPATH,value=xPathValue)

    def listenM3u8Request(self):
        while True:
            self.driver.wait_for_request(r"\.m3u8",timeout=10000)
            requests = self.driver.requests
            for req in requests:
                if str(req).find("m3u8") > 0 and str(req).find("tag=") > 0:
                    vid = tweetVid(fileName = f"{datetime.now().strftime('%m_%d_%H_%M_%S')}.mp4",
                            filePath=os.path.expanduser("~/.local/.personalData/twitterVid/"),
                            url=req)
                    self.finishFlagQueue.put(False)
                    self.mediaDownloadTaskQueue.put(vid)
            del self.driver.requests
