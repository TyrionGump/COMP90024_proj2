# ====================================
# COMP90024 Cluster and Cloud Computing
# Group 22 - Assignment 2
# Ran Liang 1162222
# Yulun Huang 910398
# Yubo Sun 1048638
# Yanhao Wang 1142087
# Xindi Fang 749394
# Last Updated: 2021-05-25
# Description: Remove duplicate tweets
# ====================================

import time

import couchdb

start = time.time()
dic1 = {}
try:
    couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
except:
    print("Cannot connected to CouchDB Server\n")
    raise

try:
    db = couchclient['yanhao_test']
    print("Connected to the user database")
except:
    db = couchclient['default']
    print("Connected to the default database")

duplicate_mango = {"selector": {},
                   "fields": ["_rev", "_id", "id", "createtime", "source", "text", "username", "userlocation",
                              "lang", "placename", "geo", "polarity", "subjectivity"], "limit": db.__len__()}

db2 = couchclient['no_duplicate_twitter']


def save(database, mango):
    for items in database.find(mango):
        # print(items["_rev"])
        if items["_rev"] not in dic1.keys():
            dic1.update({items["_rev"]: items})
        else:
            continue
    # print(len(dic1))
    for items in dic1.values():
        db2.save(
            {"id": items["id"], "createtime": items["createtime"], "source": items["source"], "text": items["text"],
             "username": items["username"],
             "userlocation": items["userlocation"], "lang": items["lang"], "placename": items["placename"],
             "geo": items["geo"],
             "polarity": items["polarity"], "subjectivity": items["subjectivity"]})


if db2.__len__() == 0:
    try:
        couchclient.delete('lines_processed')
        couchclient.create('lines_processed')
    except:
        couchclient.create('lines_processed')
    db3 = couchclient['lines_processed']
    db3.save({"lines_processed": db.__len__()})
    save(db, duplicate_mango)
    # for items in db.find(duplicate_mango):
    #     # print(items["_rev"])
    #     if items["_rev"] not in dic1.keys():
    #         dic1.update({items["_rev"]: items})
    #     else:
    #         continue
    # # print(len(dic1))
    # for items in dic1.values():
    #     db2.save(
    #         {"id": items["id"], "createtime": items["createtime"], "source": items["source"], "text": items["text"],
    #          "username": items["username"],
    #          "userlocation": items["userlocation"], "lang": items["lang"], "placename": items["placename"],
    #          "geo": items["geo"],
    #          "polarity": items["polarity"], "subjectivity": items["subjectivity"]})


else:
    db3 = couchclient['lines_processed']
    lines_processedmango = {"selector": {}, "limit": db3.__len__()}
    for items in db3.find(lines_processedmango):
        lines_processed = (items["lines_processed"])
    if lines_processed != db.__len__():
        duplicate_mango2 = {"selector": {},
                            "fields": ["_rev", "_id", "id", "createtime", "source", "text", "username", "userlocation",
                                       "lang", "placename", "geo", "polarity", "subjectivity"], "limit": db.__len__(),
                            "skip": lines_processed}
    save(db, duplicate_mango2)
    couchclient.delete('lines_processed')
    couchclient.create('lines_processed')
    db4 = couchclient['lines_processed']
    db4.save({"lines_processed": db.__len__()})

end = time.time()
print(end - start)