# ====================================
# COMP90024 Cluster and Cloud Computing
# Group 22 - Assignment 2
# Ran Liang 1162222
# Yulun Huang 910398
# Yubo Sun 1048638
# Yanhao Wang 1142087
# Xindi Fang 749394
# Last Updated: 2021-05-25
# Description: This document is used to fetch tweets through Twitter API and save them to the database
# Related DB Name: yanhao-test
# ====================================

import tweepy
from tweepy import StreamListener, Stream
import couchdb
from textblob import TextBlob

from urllib3.exceptions import ProtocolError

consumer_key = 'wCSI4LJMDch14ungsMlYBslkh'
consumer_secret = '7YwXY6WsrtRmOl3valX1Cj2ldHlq6BQUZGic6vEw3cLcl5fzII'
access_token = '1385200139061526540-6xhlSfy0gk6BSH33wwCUZ03y9SWJz1'
access_token_secret = 'qMzLZi2U4FuYnUTja0GTM6MSiKzeaxaayF588T5gD35SB'

count = 0

try:
    couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
except:
    print("Cannot find CouchDB Server ... Exiting\n")
    print("----_Stack Trace_-----\n")
    raise

try:
    db = couchclient['yanhao_test']
    print("Connected to the user database")
except:
    db = couchclient['default']
    print("Connected to the default database")


class Std(StreamListener):
    # def on_data(self, data):
    #     if data[0].isdigit():
    #         pass
    #     else:
    #         global ttstart
    #         global ttend
    #
    #         if ttstart <= ttend:
    #             if data[0].isdigit():
    #                 pass
    #             else:
    #                 jsondata = json.loads(data)
    #                 db.save(jsondata)
    #                 ttstart += 1
    #     return True

    def on_status(self, status):
        global count
        global ttend
        # print(status)
        text = status.text
        username = status.user.screen_name
        id_str = status.id_str
        createtime = str(status.created_at)
        source = status.source
        userlocation = status.user.location
        lang = status.lang
        retweeted = status.retweeted
        placename = status.place.name
        geo = status.geo
        blob = TextBlob(text)
        sent = blob.sentiment
        polarity = sent.polarity
        subjectivity = sent.subjectivity
        if retweeted == False:
            db.save({"id": id_str,"createtime":createtime,"source":source ,"text": text, "username": username,"userlocation":userlocation,"lang": lang, "placename": placename, "geo": geo,
                    "polarity": polarity, "subjectivity": subjectivity})
            count += 1
            print(count)
        else:
            pass

    def on_error(self, status):
        print(status)
        if status_code == 420:
            time.sleep(10)
        if status_code == 429:
            time.sleep(15*60 + 1)
        else:
            time.sleep(10)


l = Std()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
api = tweepy.API(auth)
while True:
    try:
        stream.filter(locations=[113.338953078, -43.6345972634, 153.569469029, -10.6681857235])
    except ProtocolError as e:
            print(f"{timestamp()} ProtocolError: {e}\n")
    except AttributeError as e:
        print(f"{timestamp()} AttributeError: {e}\n")
    except Exception as e:
        print(f"{timestamp()} Received unknown exception: {e}\n") 
    finally:
        continue
