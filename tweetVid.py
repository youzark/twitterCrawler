import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class tweetVid:
    """
    Introduction:
    Internal Data representation , use to print the picture

    initMethod:
    (name:path)
    
    Function:
    __str__()
    """
    def __init__(self,fileName,filePath,url):
        self.fileName = fileName
        self.filePath = os.path.expanduser(filePath)
        self.url = url
