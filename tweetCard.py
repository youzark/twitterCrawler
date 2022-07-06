from twitterInfo import twitterInfo
from twitterDetail import tweetDetailPageNotReply
import json

class tweetCard:
    """
    Introduction:
    General Downloader ,download all sorts of tweets infomation ,There Sorts of information store locally:
        text information
        user information
        picture resource

    Data Stream:
                  .-->   twitterInfo  --.  
                  |                     |
    www.twitter.com                     . --> tweetCard -> local Storage -> Internal
                  |                     |
                  .-->   twitterDetail--.

    twitterInfo and twitterDetail will store pics locally

    twitterInfo     --.
                      |   {userData}
                      . --{textInfo} --> tweetCard :  
                      |   {pics}
    twitterDetail   --. 

    tweetCard will store tweet info locally

    Init Method:
    twitter webpage element <article ... \article >
    """
    def __init__(self,articleSession):
        # init the tweet card:
        try:
            self.tweetCard = twitterInfo(articleSession)
        except:
            self.tweetCard = tweetDetailPageNotReply(articleSession)

        # User Info 
        self.userData = self.tweetCard.userData

        # Tweet Status
        self.textInfo = self.tweetCard.textInfo

        # Image Part
        self.pics = self.tweetCard.pics

        # GIF Part
        self.GIFs = self.tweetCard.GIFs

        # Document tweet information
        self.tweetFileName = self.userData.userHandle + "_" + self.textInfo.timeFull
        self.imgNameToFilePath = {pic.fileName:pic.filePath for pic in self.pics }
        self.imgNameToUrls = {pic.fileName:pic.url for pic in self.pics}
        self.GIFNameToFilePath = {GIF.fileName:GIF.filePath for GIF in self.GIFs}
        self.GIFNameToUrls = {GIF.fileName:GIF.url for GIF in self.GIFs}
        self.tweetDocument = {
                "fileName":self.tweetFileName,
                "userName":self.userData.userName,
                "userHandle":self.userData.userHandle,
                "timeDate":self.textInfo.timeDate,
                "timePoint":self.textInfo.timePoint,
                "reply":self.textInfo.reply,
                "comment":self.textInfo.comment,
                "quoteTweetText":self.textInfo.comment,
                "imgNameToFilePath":self.imgNameToFilePath,
                "picNameToUrls":self.imgNameToUrls,
                "GIFNameToFilePath":self.GIFNameToFilePath,
                "GIFNameToUrls":self.GIFNameToUrls
                }
        with open(self.userData.userTweetsDir + self.tweetFileName + ".json","w+") as f:
            f.write(json.dumps(self.tweetDocument,indent = 4))
        self.userData.updateUserTweetDocument(self.tweetDocument)

    def printTweet(self):
        print(self.userData)
        print(self.textInfo)
        for pic in self.pics:
            pic.printPic()
