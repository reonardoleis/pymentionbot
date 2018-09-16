#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from auth import info


auth = tweepy.OAuthHandler(info.consumer_key,
                           info.consumer_secret
                           )
auth.set_access_token(info.access_token
                      , info.access_token_secret)
api = tweepy.API(auth)

MY_TWITTER_ID = "@MPBotBR"

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
                createImage(status.text[len(MY_TWITTER_ID)+1:])
                api.update_with_media('output.jpg' ,'@'+status.user.screen_name)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@MPBotBR'])

			
