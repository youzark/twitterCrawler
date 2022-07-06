#!/usr/bin/env python
import requests
from concurrent.futures import ThreadPoolExecutor 
from myLog import threadLogger
import os
import logging

@threadLogger
def _downloadGIF(url,fileName,filePath):
    if not os.path.exists(filePath+fileName):
        GIFContent = requests.get(url).content
        fullPath = filePath + fileName
        with open(fullPath, "wb") as f:
            f.write(GIFContent)

def GIFDownloader(workQueue,finishFlagQueue,threadNum=5):
    logging.info("GIF Downloader Ready To Download")
    with ThreadPoolExecutor(max_workers=threadNum) as ex:
        while True:
            if not workQueue.empty():
                pic = workQueue.get()
                ex.submit(_downloadGIF,pic.url,pic.fileName,pic.filePath)
            else:
                finishFlag = finishFlagQueue.get()
                if finishFlag:
                    break
    logging.info("Pic Downloader Closed")
