import couchdb

dict = {}
dict2 = {}

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
mango_placewithlanguage = {"selector": {}, "fields": ["lang", "placename"], "limit": db.__len__()}
mango_languagewithpands = {"selector": {}, "fields": ["lang", "polarity", "subjectivity"], "limit": db.__len__()}

for rows in db.find(mango_placewithlanguage):
    if list(rows.values())[0] not in dict.keys():
        dict.update({list(rows.values())[0]: 1})
    else:
        dict[list(rows.values())[0]] += 1

db_language = couchclient['language_placename']
db_language.save(dict)

# for rows in db.find(mango_languagewithpands):
#     print(rows)
#     print(list(rows.values())[0], list(rows.values())[1], list(rows.values())[2])

for rows in db.find(mango_languagewithpands):
    if list(rows.values())[0] not in dict2.keys():
        dict2.update({list(rows.values())[0]: [0, 0]})
    else:
        dict2[list(rows.values())[0]][0] += list(rows.values())[1]
        dict2[list(rows.values())[0]][1] += list(rows.values())[2]
# print(dict2)
db_language2 = couchclient['language_polarity_subjectivity']
db_language2.save(dict2)
# print(dict)
#
# sum = 0
# for values in dict.values():
#     sum += values
# print(sum)
# print(mango)
# print(list(rows.values())[0])
# print(list(rows.values())[1])
# print(rows["lang"], rows["placename"])
# for items in dict.items():
#     print(items)
