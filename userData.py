import os
import json
from helper import getRidOfSpaceAndSpecialChar
from tweet import tweet

class userData:
    """
    per User information: basic, dataStorage
    Init Method:
        userName
        userHandle

    

    twitterInfo     --.
                      |
                      .--(Create User Data) --> userData  <-- (update userData)-- tweetCard
                      |                             ^
    twitterDetail   --.                             |
                                                    |
                                                (Visit User Data)
                                                    |
                                                    |
                                                  engine
    """
    def __init__(self,userName,userHandle,dataDirBasic="~/.local/.personalData/twitter/"):
        self.userName = self.addNamePrefix(getRidOfSpaceAndSpecialChar(userName))
        self.userHandle = userHandle
        self.baseDir = os.path.expanduser(dataDirBasic)
        self.dataDir = os.path.expanduser(dataDirBasic + self.userHandle + "/")
        self.userImgDir = os.path.expanduser(self.dataDir + "pic/")
        self.userVidDir = os.path.expanduser(self.dataDir + "vid/")
        self.userGIFDir = os.path.expanduser(self.dataDir + "gif/")
        self.userTweetsDir = os.path.expanduser(self.dataDir + "tweet/")
        self.createDataDirIfNotexits()
        self.tweetInfoList = self.loadTweetInfoList()

    
    def addNamePrefix(self,userName):
        if str(userName)[0:5] == "name_":
            return userName
        else:
            return "name_" + userName

        
    def createDataDirIfNotexits(self):
        if not os.path.isdir(self.dataDir):
            os.mkdir(self.dataDir)
            os.mkdir(self.userImgDir)
            os.mkdir(self.userVidDir)
            os.mkdir(self.userTweetsDir)
            os.mkdir(self.userGIFDir)
            userInfo = {
                    "userName":self.userName,
                    "userHandle":self.userHandle,
                    "tweetFileDocuments":[]
                    }
            with open(self.dataDir + 'userInfo.json',"w") as f:
                f.write(json.dumps(userInfo,indent=4))
            self.addToUserList()


    def loadTweetInfoList(self):
        userTweetPath = self.dataDir +  "userInfo.json"
        with open(userTweetPath,"r") as f:
            userInfo = json.load(f)
        return userInfo["tweetFileDocuments"]
        

    def addToUserList(self):
        userList = {}
        userListPath = str(self.baseDir) + "userList.json"
        if os.path.exists(userListPath):
            with open(userListPath,"r") as f:
                userList = json.load(f)
        if not self.userHandle in userList:
            userList[self.userName] = self.userHandle
        with open(userListPath,"w") as f:
            f.write(json.dumps(userList,indent=4))


    def updateUserTweetDocument(self,tweetFileDocument):
        userTweetPath = self.dataDir + "userInfo.json"
        with open(userTweetPath,"r") as f:
            userInfo = json.load(f)
        existTweetList = userInfo["tweetFileDocuments"]
        if not tweetFileDocument in existTweetList:
            userInfo["tweetFileDocuments"].append(tweetFileDocument)
        with open(userTweetPath,"w") as f:
            f.write(json.dumps(userInfo,indent=4))

    def printAllTweets(self):
        tweets = [ tweet(tweetDocument) for tweetDocument in self.tweetInfoList ]
        for tweetCard in tweets:
            tweetCard.printTweetCard()

    def __str__(self):
        userName = "UserName:\t\t\t" + self.userName + "\n"
        userHandle = "UserHandle:\t\t\t" + self.userHandle + "\n"
        return userName + userHandle

# load user card given name
def getUserCardFromName(userName):
    return userData(userName,getUserHandle(userName))
#

def getUserHandle(userName):
    return getUserList()[userName]

def getUserList():
    userList = {}
    with open(os.path.expanduser("~/.local/.personalData/twitter/userList.json")) as f:
        userList = json.load(f)
    return userList


