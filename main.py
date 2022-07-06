#!/usr/bin/env python
## 
from engine import tweetEngine
import time
from userData import getUserList, getUserCardFromName
from threading import Thread
##

##
engine = tweetEngine()
engine.loginToTwitter()
driver = engine.driver
print("finish")
##


## 
engine.turnToSearchPageOf("video asdfsdf")
engine.find_element("//span[contains(text(),'Latest')]").click()
print("finish")
##

## click profile
engine.enterPersonalLikes()
print("finish")
engine.downloadAllTheTweetsInThePage()
##

##
# for user in getUserList():
#     userCard = getUserCardFromName(user)
#     print(userCard)
#     userCard.printAllTweets()
##

## 
startTime = time.asctime()
print(startTime)
tweets = engine.downloadAllTheTweetsInThePage()
print(len(tweets))
for tweet in tweets:
    print("***********************************************")
    tweet.printTweet()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("finish")
endTime = time.asctime()
print(endTime)
##

##
driver.close()
##
