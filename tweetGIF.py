import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class tweetGIF:
    """
    Introduction:
    Internal Data representation , use to print the picture.

    It's supposed to be the only way to visit tweetGIF through out the whole
    process apart from the downloader

    Data stream:(GIF url)
    www.twitter.com -> TweetCard -> LocalFile -> tweetVid -> Internal

    initMethod:
    (name:path)
    
    Function:
    __str__()
    """
    def __init__(self,fileName,filePath,url):
        self.fileName = fileName
        self.filePath = os.path.expanduser(filePath)
        self.url = url
