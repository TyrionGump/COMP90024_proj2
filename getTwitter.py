import tweepy
from tweepy import StreamListener, Stream
import couchdb
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
ttstart = 0
ttend = 100000

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
        global ttstart
        global ttend
        print(status)
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
            if ttstart <= ttend:
                db.save({"id": id_str,"createtime":createtime,"source":source ,"text": text, "username": username,"userlocation":userlocation,"lang": lang, "placename": placename, "geo": geo,
                        "polarity": polarity, "subjectivity": subjectivity})
                ttstart += 1
            else:
                return True
        else:
            pass

    def on_error(self, status):
        if status == 420:
            return False


l = Std()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
api = tweepy.API(auth)
stream.filter(locations=[113.338953078, -43.6345972634, 153.569469029, -10.6681857235])
