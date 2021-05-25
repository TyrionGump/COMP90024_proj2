# ====================================
# COMP90024 Cluster and Cloud Computing
# Group 22 - Assignment 2
# Ran Liang 1162222
# Yulun Huang 910398
# Yubo Sun 1048638
# Yanhao Wang 1142087
# Xindi Fang 749394
# Last Updated: 2021-05-25
# Description: data for language scenario
# ====================================

import couchdb

try:
    couch_client = couchdb.Server('http://admin:admin@172.26.128.226:5984/')

    couch_client1 = couchdb.Server('http://admin:admin@172.26.130.226:5984/')

    couch_client2 = couchdb.Server('http://admin:admin@172.26.131.179:5984/')

    couch_client3 = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
except:
    print("Cannot find CouchDB Server ... Exiting\n")
    print("----_Stack Trace_-----\n")
    raise

db1 = couch_client['language_place_number']
db2 = couch_client1['language_placename']
db3 = couch_client2['language_psavg']

mango1 = {"selector": {}, "limit": db1.__len__()}
mango2 = {"selector": {}, "limit": db2.__len__()}
mango3 = {"selector": {}, "limit": db3.__len__()}

def get_language_l1_data():
    list8 = []
    for i in db1.find(mango1):
        list8.append(["Sydney",i["Sydney"]])
        list8.append(["Melbourne", i["Melbourne"]])
        list8.append(["Brisbane",i["Brisbane"]])
        list8.append(["Perth",i["Perth (WA)"]])
        list8.append(["Adelaide", i["Adelaide"]])
        list8.append(["GoldCoast",i["Gold Coast"]])
        list8.append(["Canberra",i["Canberra"]])
        list8.append(["Newcastle",i["Newcastle"]])
    dict = {}
    list2 = []
    for items in list8:
        list = []
        for i in items[1]:
            list.append({'name':i[0],'value':i[1]})
        dict.update({items[0]:list})
    return dict


def get_language_l2_data():
    for i in db3.find(mango3):
        i.pop("_id")
        i.pop("_rev")
        i3 = (i.copy())
    dict3 = {'name':'score',
             'legend':['polarity','subjective'],
             'xAxis': [i for i in i3.keys()],
             'data':[[round(j[0], 4) for j in i3.values()],[round(j[1], 4) for j in i3.values()]]
             }
    return dict3


def get_language_r2_data():
    for i in db2.find(mango2):
        i.pop("_id")
        i.pop("_rev")
        i2 = (i.copy())
    # print("_______")
    list3 = []
    for items in i2.items():
        list3.append({'name':items[0],'value':items[1]})
    return list3


def get_language_c1_data():
    dbworld = couch_client['lan_worldmap']
    mango1 = {"selector": {}, "limit": dbworld.__len__()}
    i2 = None
    for items in dbworld.find(mango1):
        items.pop("_id")
        items.pop("_rev")
        i2 = items.copy()
    return i2


def get_language_r1_data():
    db_aurin = couch_client3['aurin_language']
    dictaurin = {}
    mango_aurin = {"selector": {}, "limit": db_aurin.__len__()}
    for items in db_aurin.find(mango_aurin):
        if items['city'] in ["Sydney", "Melbourne", "Brisbane", "Adelaide"]:
            items.pop("_id")
            items.pop("_rev")
            i = items.copy()
            city = i["city"]
            del i['city']
            dc = {k: v for k, v in sorted(i.items(), key=lambda item: item[1], reverse=True)}
            five = {k: dc[k] for k in list(dc)[:5]}
            dictaurin.update({city: five})

    db_twitter = couch_client3['language_place_number']
    mango_twitter = {"selector": {}, "limit": db_twitter.__len__()}
    listtwitter = []
    for items in db_twitter.find(mango_twitter):
        listtwitter.append(['Sydney', items['Sydney']])
        listtwitter.append(['Melbourne', items['Melbourne']])
        listtwitter.append(['Brisbane', items['Brisbane']])
        listtwitter.append(['Adelaide', items['Adelaide']])

    dicttwifinal = {}
    for items in listtwitter:
        city = items[0]
        langlist = items[1]
        langlist.sort(key=lambda x: x[1], reverse=True)
        langlist = [x for x in langlist if x[0] != 'und']
        dict1 = {}
        for k in langlist[:5]:
            dict1.update({k[0]: k[1]})
        dicttwifinal.update({city: dict1})
    dicttwiaurin = {}
    for k, v in dictaurin.items():
        if k in dicttwifinal.keys():
            keys = []
            values = [{"value": 5, "itemStyle": {"color": '#f15c80'}},
                      {"value": 4, "itemStyle": {"color": '#f15c80'}},
                      {"value": 3, "itemStyle": {"color": '#f15c80'}},
                      {"value": 2, "itemStyle": {"color": '#f15c80'}},
                      {"value": 1, "itemStyle": {"color": '#f15c80'}},
                      {"value": 5, "itemStyle": {"color": '#40e0d0'}},
                      {"value": 4, "itemStyle": {"color": '#40e0d0'}},
                      {"value": 3, "itemStyle": {"color": '#40e0d0'}},
                      {"value": 2, "itemStyle": {"color": '#40e0d0'}},
                      {"value": 1, "itemStyle": {"color": '#40e0d0'}}
                      ]
            data = []
            for items in v.items():
                keys.append(items[0])
            for items in dicttwifinal[k].items():
                keys.append(items[0])
            dicttwiaurin.update({k: {'xAxis': keys, 'data': values}})
    return dicttwiaurin
