# importando os módulos 
import os
import tweepy
import requests

  
# detalhes pessoais
consumer_key="AufMDq9xpSKJblq4jVXgMFlgh"
consumer_secret="OgQ9wEQUkl2b8ap2cR5oyFf0lJhjEIsc8Z7MHXT9pyNagQTQqm"
access_token="701080529924444161-2bt74SHc7odYT0ssb0rZpJqJESt4Qwe"
access_token_secret="VfocpVHSXAVdNH2FFDOwhGu5BG7IXeTKX9lYPRLZokifH"

client = tweepy.Client(consumer_key="AufMDq9xpSKJblq4jVXgMFlgh",
                    consumer_secret="OgQ9wEQUkl2b8ap2cR5oyFf0lJhjEIsc8Z7MHXT9pyNagQTQqm",
                    access_token="701080529924444161-2bt74SHc7odYT0ssb0rZpJqJESt4Qwe",
                    access_token_secret="VfocpVHSXAVdNH2FFDOwhGu5BG7IXeTKX9lYPRLZokifH")


url = ""
texto = "E vc que demora anos para escrever por ai?"
id= "1481965623378862080"


# Replace the text with whatever you want to Tweet about
like =  client.like(id)
response = client.create_tweet(in_reply_to_tweet_id = id,text= texto)