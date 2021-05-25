# ====================================
# COMP90024 Cluster and Cloud Computing
# Group 22 - Assignment 2
# Ran Liang 1162222
# Yulun Huang 910398
# Yubo Sun 1048638
# Yanhao Wang 1142087
# Xindi Fang 749394
# Last Updated: 2021-05-25
# Description:
# This document is divided into four parts:
# Part one:
# Part two:
# Part three:
# Part four: save the average score which uses total polarity/total number of people to lan_worldmap database
# Related DB Name: language_place_number, language_placename, language_psavg, lan_worldmap
# ====================================
import couchdb

dictt = {}
dict2 = {}
dict3 = {}
try:
    couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
except:
    print("Cannot find CouchDB Server ... Exiting\n")
    print("----_Stack Trace_-----\n")
    raise

try:
    db = couchclient['no_duplicate_twitter']
    print("Connected to the user database")
except:
    db = couchclient['default']
    print("Connected to the default database")
mango_placewithlanguage = {"selector": {}, "fields": ["lang", "placename"], "limit": db.__len__()}
mango_languagewithpands = {"selector": {}, "fields": ["lang", "polarity", "subjectivity"], "limit": db.__len__()}


try:
    couchclient.delete('language_place_number')
    couchclient.create('language_place_number')
except:
    couchclient.create('language_place_number')
try:
    couchclient.delete('language_placename')
    couchclient.create('language_placename')
except:
    couchclient.create('language_placename')
try:
    couchclient.delete('language_psavg')
    couchclient.create('language_psavg')
except:
    couchclient.create('language_psavg')
try:
    couchclient.delete('lan_worldmap')
    couchclient.create('lan_worldmap')
except:
    couchclient.create('lan_worldmap')


for rows in db.find(mango_placewithlanguage):
    if list(rows.values())[0] not in dictt.keys():
        dictt.update({list(rows.values())[0]: 1})
    else:
        dictt[list(rows.values())[0]] += 1

db_language = couchclient['language_placename']
db_language.save(dictt)

#

for rows in db.find(mango_languagewithpands):
    if list(rows.values())[0] not in dict2.keys():
        dict2.update({list(rows.values())[0]: [0, 0]})
    else:
        dict2[list(rows.values())[0]][0] += list(rows.values())[1]
        dict2[list(rows.values())[0]][1] += list(rows.values())[2]

dict_avg = {}

for key in list(set(dictt) | set(dict2)):
    if dictt.get(key) and dict2.get(key):
        dict_avg.update({key:[dict2.get(key)[0]/dictt.get(key),dict2.get(key)[1]/dictt.get(key)]})
    else:
        if key == "_id" or "_rev":
            continue
        dict_avg.update({key:dictt.get(key) or dict2.get(key)})
# print(len(dict_avg))
# print(len(dict))
# print(len(dict2))
db_language2 = couchclient['language_psavg']
db_language2.save(dict_avg)
#





for rows in db.find(mango_placewithlanguage):
    if list(rows.values())[1] not in dict3.keys():
        dict3.update({list(rows.values())[1]: [[list(rows.values())[0], 1]]})
    else:
        languagelist = [i[0] for i in dict3[list(rows.values())[1]]]
        if list(rows.values())[0] not in languagelist:
            dict3[list(rows.values())[1]].append([list(rows.values())[0], 1])
        else:
            for items in dict3[list(rows.values())[1]]:
                if items[0] == list(rows.values())[0]:
                    items[1] +=1
db_language_place_number = couchclient['language_place_number']
db_language_place_number.save(dict3)

#



db1 = couchclient['language_place_number']
mango1 = {"selector": {}, "limit": db1.__len__()}
db4 = couchclient['no_duplicate_twitter']
mango_polarity_placename = {"selector": {}, "fields": ["placename", "polarity"], "limit": db4.__len__()}
dict_allpolarity = {}
for i in db4.find(mango_polarity_placename):
    if i["placename"] in dict_allpolarity.keys():
        dict_allpolarity[i["placename"]] += i["polarity"]
    else:
        dict_allpolarity.update({i["placename"]:i["polarity"]})
dict_all_language_placenum = {}
list10 = []
for i in db1.find(mango1):
    list10.append(["Sydney",i["Sydney"]])
    list10.append(["Melbourne", i["Melbourne"]])
    list10.append(["Brisbane",i["Brisbane"]])
    list10.append(["Perth",i["Perth (WA)"]])
    list10.append(["Adelaide", i["Adelaide"]])
    list10.append(["Gold Coast",i["Gold Coast"]])
    list10.append(["Canberra",i["Canberra"]])
    list10.append(["Newcastle",i["Newcastle"]])
list11 = []
for items in list10:
    y = sum(x[1] for x in items[1])
    list11.append(y)
dict_all_language_placenum = dict(zip([x[0] for x in list10],list11))
dict_polaritydividedbytotal = {}
for items in dict_all_language_placenum.keys():
    if items in dict_allpolarity.keys():
        avg = dict_allpolarity[items]/dict_all_language_placenum[items]
        dict_all_language_placenum[items] = avg
listfinal = []
eight_largest_city_index = [[151.207, -33.868], [144.963, -37.814], [153.028, -27.468], [115.861, -31.952],
                            [138.599, -34.929],
                            [153.431, -28], [149.128, -35.283], [151.78, -32.93]]
listadd = []
for key, value in dict_all_language_placenum.items():
    listadd.append([key,value])
listfinal2=[]
listfinal = [list(l) for l in zip(eight_largest_city_index,listadd)]
for items in listfinal:
    x = items[0][0]
    y = items[0][1]
    i2 = items[1]

    listfinal2.append({'name':i2[0],"value":[x,y,i2[1]]})
dbworld = couchclient['lan_worldmap']
dictworld = {'data_name':'world',
         'data':listfinal2
         }
dbworld.save(dictworld)






