#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import base64
from io import BytesIO


auth = tweepy.OAuthHandler('vF9I1Rnnu97hreQ0c5Sy93OyZ',
                           'uxRgJmGin3GhHiSQGc2OjvW2NvSTKCtSVnJDBflIWLlFMoh0Ib'
                           )
auth.set_access_token('1040048344792530954-hqr9PjcKzbofDjScvlPLRSPSCqDE77'
                      , 'md6jlC46Bj8YrZiIYVLaIIUGpt27TsOUeWd6qE6PLydu1')
api = tweepy.API(auth)


def createImage(txt):

    img = Image.open('img.jpg')
    drawer = ImageDraw.Draw(img)
    font = ImageFont.truetype('sans-serif.ttf', 25)
    words = txt.split()
    phrase = ''
    for x in range(0, len(words)):
        if x % 3 == 0 and x != 0:
            words[x] += '\n'

    for x in range(0, len(words)):
        if x % 3 == 0 and x != 0:
            phrase += words[x]
        else:
            phrase += words[x] + ' '

    drawer.text((10, img.height / 4), phrase, (255, 255, 255), font=font)
    img.save('output.jpg')
   

   

class MyStreamListener(tweepy.StreamListener):
        def on_status(self, status):
                createImage(status.text[8:])
                api.update_with_media('output.jpg' ,'@'+status.user.screen_name)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@MPBotBR'])

			
