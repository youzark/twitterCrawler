#!/usr/bin/env python
import requests
from concurrent.futures import ThreadPoolExecutor 
from myLog import threadLogger
import os
import logging
from subprocess import run

@threadLogger
def _downloadImg(url,fileName,filePath):
    if not os.path.exists(filePath+fileName):
        imageContent = requests.get(url).content
        fullPath = filePath + fileName
        with open(fullPath, "wb") as f:
            f.write(imageContent)

@threadLogger
def _downloadGIF(url,fileName,filePath):
    if not os.path.exists(filePath+fileName):
        GIFContent = requests.get(url).content
        fullPath = filePath + fileName
        with open(fullPath, "wb") as f:
            f.write(GIFContent)

@threadLogger
def _downloadM3u8(url,fileName,filePath):
    highestResolutionM3u8Url = _parseM3u8(url)[-1]
    fullPath = filePath + fileName
    if not os.path.exists(fullPath):
        print("start downloading: " + fileName)
        command = ["ffmpeg","-i",highestResolutionM3u8Url,"-c","copy",fullPath]
        run(command,stdout=None)
        print("finish downloading: " + fileName)
    
"""
There are two sorts of m3u8 urls in twitter.
one with tag=12 , contain multiple sub m3u8 represents different resolution

the second with specific resolution ,contain all the stream file url
here we only accept the first one 
the process will parse the m3u8 and extract the sub m3u8 with highest resolution
"""
def _parseM3u8(url):
    m3u8File = requests.get(url).content
    m3u8InfoList = m3u8File.decode("utf-8").split("\n")
    m3u8List = ["https://video.twimg.com" + m3u8Info for m3u8Info in m3u8InfoList if m3u8Info[:14] == "/ext_tw_video/" ]
    return m3u8List


def mediaDownloader(workQueue,finishFlagQueue,threadNum=5):
    logging.info("Pic Downloader Ready To Download")
    with ThreadPoolExecutor(max_workers=threadNum) as ex:
        while True:
            if not workQueue.empty():
                item = workQueue.get()
                if str(item.__class__) == "<class 'tweetPicture.tweetPicture'>":
                    ex.submit(_downloadImg,item.url,item.fileName,item.filePath)
                if str(item.__class__) == "<class 'tweetGIF.tweetGIF'>":
                    ex.submit(_downloadGIF,item.url,item.fileName,item.filePath)
            else:
                finishFlag = finishFlagQueue.get()
                if finishFlag:
                    break
    logging.info("Pic Downloader Closed")

# def picDownloader(workQueue,finishFlagQueue,threadNum=5):
#     logging.info("Pic Downloader Ready To Download")
#     with ThreadPoolExecutor(max_workers=threadNum) as ex:
#         while True:
#             if not workQueue.empty():
#                 pic = workQueue.get()
#                 ex.submit(_downloadImg,pic.url,pic.fileName,pic.filePath)
#             else:
#                 finishFlag = finishFlagQueue.get()
#                 if finishFlag:
#                     break
#     logging.info("Pic Downloader Closed")

def main():
    m3u8List = [
            "https://video.twimg.com/ext_tw_video/1505580634068205573/pu/pl/ZvLOy2FtR8k4fxIy.m3u8?tag=12&container=fmp4",
            "https://video.twimg.com/ext_tw_video/1505672682494382089/pu/pl/bKj-JoQNBxSmnWeI.m3u8?tag=12&container=fmp4",
            "https://video.twimg.com/ext_tw_video/1505202647439056898/pu/pl/HzOJWOb45lua6Fu-.m3u8?tag=12&container=fmp4"
            ]
    i = 0
    for m3u8 in m3u8List:
        _downloadM3u8(m3u8,"vid" + str(i) + ".mp4",os.path.expanduser("~/vid/"))
        i += 1

if __name__ == "__main__":
    main()
