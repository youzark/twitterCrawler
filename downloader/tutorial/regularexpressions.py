#!/usr/bin/env python
import re

textToSearch = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIHKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped)
. ^ $ + ? {  } [  ] \ | ()

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

Mytext = """
https://video.twimg.com/ext_tw_video/1505580634068205573/pu/pl/ZvLOy2FtR8k4fxIy.m3u8?tag=12&container=fmp4
https://video.twimg.com/ext_tw_video/1505580634068205573/pu/pl/480x270/6w26AX8jzFESGFJZ.m3u8?container=fmp4
"""

pattern = re.compile(r"/\d+x\d+/[0-9a-zA-Z\-_]*.m3u8")

matches = pattern.finditer(Mytext)

for text in matches:
    print(text)
