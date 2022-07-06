from tweetPicture import tweetPicture

class tweet:
    """
    1.Init Method:
    tweetDocument

    2.Functions:
    printTweetDocument

    """
    def __init__(self,tweetDocument):

        self.fileName = tweetDocument["fileName"]
        self.userName= tweetDocument["userName"]
        self.userHandle = tweetDocument["userHandle"]
        self.timeDate = tweetDocument["timeDate"]
        self.timePoint = tweetDocument["timePoint"]
        self.reply = tweetDocument["reply"]
        self.comment = tweetDocument["comment"]
        self.imgNameToFilePath = tweetDocument["imgNameToFilePath"]
        self.imgNameToUrls = tweetDocument["picNameToUrls"]
        self.GIFNameToFilePath = tweetDocument["GIFNameToFilePath"]
        self.GIFNameToUrls = tweetDocument["GIFNameToUrls"]

        self.pics = [ tweetPicture(url=self.imgNameToUrls[fileName],fileName=fileName,filePath=self.imgNameToFilePath[fileName]) for fileName in self.imgNameToFilePath ]
        self.timeFull = self.timeDate + "_" + self.timePoint

    def printTweetCard(self):
        print("UserName:\t\t\t" + self.userName)
        print("UserHandle:\t\t\t" + self.userHandle)
        print("PostTime:\t\t\t" + self.timeFull)
        print("Reply Info:\t\t\t")
        print(self.reply)
        print("Comment:\t\t\t")
        print(self.comment)
        for pic in self.pics:
            pic.printPic()
