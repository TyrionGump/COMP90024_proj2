import couchdb
import numpy as np

couch_client = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
db = couch_client['no_duplicate_twitter']

client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
db1 = client['no_duplicate_twitter']
eight_largest_city = ['Sydney ', 'Melbourne ', 'Brisbane ', 'Perth (WA) ', 'Adelaide ', 'Gold Coast ', 'Canberra ',
                      'Newcastle ']
eight_key = ['S y d n e y ', 'M e l b o u r n e ', 'B r i s b a n e ', 'P e r t h   ( W A ) ', 'A d e l a i d e ',
             'G o l d   C o a s t ', 'C a n b e r r a ',
             'N e w c a s t l e ']

eight_largest_city_index = [[151.207, -33.868], [144.963, -37.814], [153.028, -27.468], [115.861, -31.952],
                            [138.599, -34.929],
                            [153.431, -28], [149.128, -35.283], [151.78, -32.93]]

source_list = ["Twitter for Android ", "Twitter for iPhone "]
time_list = ['0 0 ', '0 1 ', '0 2 ', '0 3 ', '0 4 ', '0 5 ', '0 6 ', '0 7 ', '0 8 ', '0 9 ', '1 0 ', '1 1 ', '1 2 ',
             '1 3 ', '1 4 ', '1 5 ', '1 6 ', '1 7 ', '1 8 ', '1 9 ', '2 0 ', '2 1 ', '2 2 ', '2 3 ']
source_key = ['T w i t t e r   f o r   A n d r o i d ', 'T w i t t e r   f o r   i P h o n e ']
eight_largest_city_state=['NSW','VIC','QLD','WA','SA','QLD','ACT','NSW']


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele + " "
        # return string
    return str1

# unemployment data for l1
def unemp_date_count():
    review = db.iterview('unemployment_analysis/unemp_polarity', db1.__len__(), group=True, group_level=3)
    count = []
    date =[]
    for row in review:
        date.append(listToString(row.key).strip())
        count.append(row.value['count'])
    return date, count

# unemployment data for l2
def unemp_date_polarity_sub():
    review = db.iterview('unemployment_analysis/unemp_polarity', db1.__len__(), group=True, group_level=3)
    pol = []
    date = []
    for row in review:
        date.append(listToString(row.key).strip())
        pol.append(row.value['average'])

    review1 = db.iterview('unemployment_analysis/unemp_sub', db1.__len__(), group=True, group_level=3)
    sub=[]
    for row in review1:
        sub.append(row.value['average'])
    return date, pol, sub


# unemployment data for c1
def unemp_map():
    review_loc = db.iterview('unemployment_analysis/unemp_region', db1.__len__(), group=True, group_level=1)
    output = []
    for row in review_loc:
        if listToString(row.key) in eight_largest_city:
            temp=[]
            dict = {}
            pol=[]
            temp.append(eight_largest_city_index[eight_largest_city.index(listToString(row.key))][0])
            temp.append(eight_largest_city_index[eight_largest_city.index(listToString(row.key))][1])
            pol.append(row.value['average'])
            temp.append(pol)
            dict.update({'name': listToString(row.key).strip(), 'value':temp})
            output.append(dict)
    return output


# unemployment data for r2
def unemployment_cloud():
    review_loc = db.iterview('unemployment_analysis/unemp_region', db1.__len__(), group=True, group_level=1)
    output=[]
    keyword = db.iterview('unemployment_analysis/unemp_mentioned', db1.__len__(), group=True, group_level=1)
    for row in review_loc:
        output.append({'name':listToString(row.key),'value':row.value['count']})
    for row in keyword:
        output.append({'name':listToString(row.key),'value':row.value['count']})
    return output

def unemp_with_aurin():
    review_loc = db.iterview('unemployment_analysis/unemp_region', db.__len__(), group=True, group_level=1)
    place = []
    polar = []
    for row in review_loc:
        placename = listToString(row.key).strip()
        if (placename == "Perth (WA)"):
            placename = "Perth"
        place.append(placename)
        polar.append(row.value['average'])

    db_unemp_aurin = couch_client['aurin_unemp']

    review_unemp = db_unemp_aurin.iterview('get_rate/get_unemp_rate',reduce = False, batch = True)
    sorted_place_unemp = []
    aurin_unemp_rate = []
    polar_unemp_rate = []
    for row in review_unemp:
        for pl in place:
            if row.key[1] == "Greater " + pl:
                polar_unemp_rate.append(round(polar[place.index(pl)], 3))
                sorted_place_unemp.append(pl)
                aurin_unemp_rate.append("%.3f" % round(row.value, 3))

    review_youth_unemp = db_unemp_aurin.iterview('get_rate/get_youth_unemp_rate', reduce=False, batch=True)
    sorted_place_youth_unemp = []
    aurin_youth_unemp_rate = []
    polar_youth_unemp_rate = []
    for row in review_youth_unemp:
        for pl in place:
            if row.key[1] == "Greater " + pl:
                polar_youth_unemp_rate.append(round(polar[place.index(pl)], 3))
                sorted_place_youth_unemp.append(pl)
                aurin_youth_unemp_rate.append("%.3f" % round(row.value, 3))
    legend = ["Youth Unemployment rate vs. Polarity", 'Unemployment Rate vs. Polarity']
    return legend, aurin_unemp_rate,aurin_youth_unemp_rate,polar_unemp_rate,polar_youth_unemp_rate

print(unemployment_cloud())