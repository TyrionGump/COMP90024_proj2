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
    print(len(dict))
    return dict





def get_language_l2_data():
    for i in db3.find(mango3):
        i.pop("_id")
        i.pop("_rev")
        i3 = (i.copy())
    dict3 = {'name':'score',
             'legend':['polarity','subjective'],
             'xAxis': [i for i in i3.keys()],
             'data':[[j[0] for j in i3.values()],[j[1] for j in i3.values()]]
             }
    # print([i for i in i3.keys()])
    # print([j for j in i3.values()])
    # print([j[0] for j in i3.values()])
    # print([j[1] for j in i3.values()])
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
    # print(items[0])
    # print(items[1])
# print(list3)

def get_language_c1_data():
    dbworld = couch_client['lan_worldmap']
    mango1 = {"selector": {}, "limit": dbworld.__len__()}
    i2 = None
    for items in dbworld.find(mango1):
        items.pop("_id")
        items.pop("_rev")
        i2 = items.copy()
    return i2

print(get_language_c1_data())