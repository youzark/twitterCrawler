#!/usr/bin/env python
import requests
import os
import m3u8
from bs4 import BeautifulSoup


url = "https://twitter.com/ArthurFamous1/status/1504464757851508737"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
        }
response = requests.get(url=url,headers=headers).text
bf = BeautifulSoup(response)
print(bf.prettify())
# with open(os.path.expanduser("~/Computer/crawler/twitter/httpPage.txt"),"w") as f:
#     f.write(response.text)

# playList = m3u8.load("https://video.twimg.com/ext_tw_video/1503001566713810949/pu/pl/1280x720/mlrcw2aE2KQ5yNRc.m3u8?container=fmp4")
# print(playList.dumps())
