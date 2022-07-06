import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class tweetPicture:
    """
    Introduction:
    Internal Data representation , use to print the picture

    Data stream:(Picture)
    www.twitter.com -> TweetCard -> LocalFile -> tweetPicture -> Internal

    initMethod:
    (name:path)
    
    Function:
    __str__()
    """
    def __init__(self,fileName,filePath,url):
        self.fileName = fileName
        self.filePath = os.path.expanduser(filePath)
        self.url = url

    def printPic(self):
        img = mpimg.imread(self.filePath + self.fileName)
        plt.imshow(img)
        plt.show()
