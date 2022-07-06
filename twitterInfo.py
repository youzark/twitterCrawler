from selenium.webdriver.common.by import By
from datetime import datetime
from helper import getRidOfSpaceAndSpecialChar
from userData import userData
from tweetTextInfo import tweetTextInfo
from tweetPicture import tweetPicture
from myLog import funcLogger
from tweetGIF import tweetGIF

class twitterInfo:
    """
    Introduction:
    Gather All Info of the tweet :Text Info , User Info , MultiMedia Download Info
    In general page with list of tweets

    Init Method:
    twitter webpage element <article ... \article >
    
    """
    def __init__(self,articleSession):
        self.tweet = articleSession

        # separate the tweet into several parts
        sectionMap = self.separateTweet()

        # Collect basic information (must before everything)
        self.userData = self.getUserInfo(sectionMap["userSection"]) #User Information

        # Collect Comment and Reply
        self.textInfo = self.getTextInfo(sectionMap["userSection"],sectionMap["blogSubSections"],sectionMap["referenceSection"])

        self.pics = self.getPics(sectionMap["imgSections"])

        self.GIFs = self.getGIFs(sectionMap["GIFSections"])

    @funcLogger
    def separateTweet(self):
        sectionMap = {}
        mainInfoSection = self.tweet.find_element(by=By.XPATH,value="./div[1]/div[1]/div[1]/div[2]/div[2]")
        sectionMap["userSection"] = mainInfoSection.find_element(by=By.XPATH,value="./div[1]")
        blogSection = mainInfoSection.find_element(by=By.XPATH,value="./div[2]")
        sectionMap["blogSubSections"]= blogSection.find_elements(by = By.XPATH,value = "./div") # four/three sections: reply comment reference and status
        sectionMap["referenceSection"]= sectionMap["blogSubSections"][len(sectionMap["blogSubSections"])-2]
        sectionMap["GIFSections"] = sectionMap["referenceSection"].find_elements(by= By.XPATH, value = ".//video[@type='video/mp4']")
        sectionMap["imgSections"] = sectionMap["referenceSection"].find_elements(by = By.XPATH , value = ".//img")
        sectionMap["vidSection"] = sectionMap["referenceSection"].find_elements(by=By.XPATH ,value = "//video[@aria-label='Embedded video']")
        return sectionMap

    def getGIFs(self,GIFSections):
        GIFUrls = [GIFSection.get_attribute("src") for GIFSection in GIFSections]
        GIFs = [ tweetGIF(
            url=imgUrl,
            fileName= self.userData.userHandle + "_" + self.textInfo.timeFull + "seq-" + str(seq),
            filePath= self.userData.userGIFDir)
            for seq, imgUrl in enumerate(GIFUrls ) ]
        return GIFs

    def getPics(self,imgSections):
        imgUrls = [imgSection.get_attribute("src") 
                for imgSection in imgSections 
                if not imgSection.get_attribute("src")[-4:] == ".svg" ]
        pics = [ tweetPicture(
            fileName=self.userData.userHandle + "_" + self.textInfo.timeFull + "seq-" + str(seq),
            filePath=self.userData.userImgDir,
            url=imgUrl) 
            for seq, imgUrl in enumerate(imgUrls) ]
        return pics

    def getPicInfo(self,imgSections):
        imgUrls = self.getPicUrls(imgSections)
        self.picInfoMap(imgUrls)
    
    def getPicUrls(self,imgSections):
        imgUrls = []
        if not len(imgSections) == 0:
            for entry in imgSections:
                if not entry.get_attribute("src")[-4:] == ".svg":
                    imgUrls.append(entry.get_attribute("src"))
        return imgUrls

    def picInfoMap(self,imgUrls):
        self.imgNameToFilePath = {}
        self.imgNameToUrls = {}
        seq = 0
        for url in imgUrls:
            fileName = self.userData.userHandle + "_" + self.textInfo.timeFull + "seq-" + str(seq)
            # if dlImg(url,fileName,self.userData.userImgDir):
            self.imgNameToUrls[fileName] = url
            self.imgNameToFilePath[fileName] = self.userData.userImgDir
            seq = seq + 1

    def getUserInfo(self,userSection):
        userName = getRidOfSpaceAndSpecialChar(userSection.find_element(by=By.XPATH,value=".//span").text)
        userHandle = userSection.find_element(by=By.XPATH,value=".//span[contains(text(),'@')]").text
        return userData(userName,userHandle)

    def getTextInfo(self,userSection,blogSubSections,referenceSection):
        tweetTime = userSection.find_element(by=By.XPATH,value=".//time").get_attribute("datetime")
        timeObj = datetime.strptime(tweetTime,'%Y-%m-%dT%H:%M:%S.000Z')
        comment,reply = self.getReplyAndMajorComment(blogSubSections)
        refText = self.getQuoteTweetText(referenceSection)
        return tweetTextInfo(comment,reply,timeObj,refText)

    def getReplyAndMajorComment(self,blogSubSections):
        comment = blogSubSections[len(blogSubSections)-3].text
        if len(blogSubSections) == 4:
            reply = blogSubSections[len(blogSubSections) - 4].text
        else:
            reply = ""
        return comment,reply
        
    def getQuoteTweetText(self,referenceSection):
        return referenceSection.text

    def isContainSubQuote(self,referenceSection):
        try:
            referenceSection.find_element(by=By.XPATH,value=".//time")
            return True
        except:
            return False
