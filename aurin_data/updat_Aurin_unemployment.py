import couchdb
import json
"""
Last Updated: 2021.05.25
By: Yulun Huang
Content: Upload the unemployment data from AURIN to CouchDB database with preprocessed format.
CouchDB Databsae: aurin_unemp
"""
couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
datainfo = "aurin_unemp"
if couchclient.__contains__(datainfo):
    couchclient.delete(datainfo)
couchclient.create(datainfo)
db = couchclient[datainfo]

with open("enp.json") as f:
    data = json.load(f)


feature = data['features']
state_name = set();
li_name = list()
li_working_pop = []
li_youth_unemp_pop = []
li_unemp_pop = []
li_unemp_rate = []
li_youth_unemp_rate = []
for f in feature:
    test = f['properties']
    key = test.pop('sa4_name_2016')
    sa2_name = test.pop('gccsa_name_2016')
    if sa2_name not in state_name:
        print(sa2_name)
        state_name.add(sa2_name)
        li_name.append(sa2_name)
        li_unemp_pop += [0]
        li_working_pop += [0]
        li_youth_unemp_pop += [0]
        li_unemp_rate += [0.0]
        li_unemp_rate += [0.0]

    working_pop = int(test.pop('working_age_pop_15_64'))
    li_working_pop[li_name.index(sa2_name)] += working_pop
    # emp_pop = int(working_pop * float(test.pop('mpy_rt_15_64')))
    youth_unemp_pop = int(working_pop * float(test.pop('yth_unemp_rt_15_24'))/100)
    li_youth_unemp_pop[li_name.index(sa2_name)] += youth_unemp_pop
    unemp_pop = int(working_pop * float(test.pop('unemp_rt_15'))/100)
    li_unemp_pop[li_name.index(sa2_name)] += unemp_pop

li_unemp_rate = [i / j*100 for i, j in zip(li_unemp_pop, li_working_pop)]
li_youth_unemp_rate = [i / j*100 for i, j in zip(li_youth_unemp_pop, li_working_pop)]

for i in range(li_name.__len__()):
    db.save({"city":li_name[i],"work_population": li_working_pop[i],"youth_unemployment_total":li_youth_unemp_pop[i],"unemployment_total":li_unemp_pop[i], "unemployment_rate": li_unemp_rate[i],"youth_unemployment_rate":li_youth_unemp_rate[i]})
