class tweetTextInfo:
    def __init__(self,comment,reply,timeObj,quoteTweetText):
        self.reply = reply
        self.comment = comment
        self.timeDate = str(timeObj.year) + "-" + str(timeObj.month) + "-" + str(timeObj.day)
        self.timePoint = str(timeObj.hour) + "-" + str(timeObj.minute) + "-" + str(timeObj.second)
        self.timeFull = self.timeDate + "_" + self.timePoint
        self.quoteTweetText = quoteTweetText 

    def __str__(self):
        time = "PostTime:\t\t\t" + self.timeFull + "\n"
        reply = "Reply Info:\t\t\t" + "\n" + self.reply + "\n"
        comment = "Comment:\t\t\t" + "\n" + self.comment + "\n"
        quote = "Quote:\t\t\t" + "\n" + self.quoteTweetText + "\n"
        return time + reply + comment + quote
