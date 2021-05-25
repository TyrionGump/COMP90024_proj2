import couchdb
import json
from textblob import TextBlob
from language_tags import tags

couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
datainfo = "aurin_language"
if couchclient.__contains__(datainfo):
    couchclient.delete(datainfo)
couchclient.create(datainfo)
db = couchclient[datainfo]

with open("language.json") as f:
    data = json.load(f)


feature = data['features']


with open("meta_language.json") as g:
    data1 = json.load(g)


meta = data1['selectedAttributes']
language_name = ['Chinese','English','Croatian','French','Dutch','Arabic','Afrikaans','Australian','German']
for fl in feature:
    language_list = fl['properties']
    city = language_list.pop('gcc_name16')
    name = []
    num_list = []
    while language_list.__len__() > 0:
        item = language_list.popitem()
        att_meta = meta.copy()
        for mt in range(att_meta.__len__()):
            if item[0] == att_meta[mt]['name']:
                des = att_meta[mt]['title']
                subCheck1 = "And"
                subCheck2 = "Total"
                if subCheck1 not in des and subCheck2 in des:
                    name.append(des)
                    num_list.append(item[1])
                # name.append(des)
                # num_list.append(item[1])
                att_meta.pop(mt)
                break;
    city = city.replace('Greater ','').replace('Australian Capital Territory','Canberra')
    doc = {'city': city}

    BCP_code = []
    BCP_count = []
    for i in range(name.__len__()):
        doc_split = name[i].split(" ")
        for token in doc_split:
            if token in language_name:
                language_code = tags.search(token)[0].__str__()
                if language_code not in BCP_code:
                    BCP_code.append(language_code)
                    BCP_count.append(num_list[i])
                else:
                    BCP_count[BCP_code.index(language_code)]+= num_list[i]
                break;

    for j in range(BCP_code.__len__()):
        doc[BCP_code[j]] = BCP_count[j]
    print(doc)
    db.save(doc)

