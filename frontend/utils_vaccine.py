# ====================================
# COMP90024 Cluster and Cloud Computing
# Group 22 - Assignment 2
# Ran Liang 1162222
# Yulun Huang 910398
# Yubo Sun 1048638
# Yanhao Wang 1142087
# Xindi Fang 749394
# Last Updated: 2021-05-25
# Description: data for vaccine scenario
# ====================================

import couchdb
import numpy as np

couch_client = couchdb.Server('http://admin:admin@172.26.128.226:5984/')
db = couch_client['no_duplicate_twitter']

couch_client1 = couchdb.Server('http://admin:admin@172.26.130.226:5984/')
db1 = couch_client1['no_duplicate_twitter']

couch_client2 = couchdb.Server('http://admin:admin@172.26.131.179:5984/')
db2 = couch_client2['no_duplicate_twitter']

couch_client3 = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
db3 = couch_client3['no_duplicate_twitter']

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


# vaccine data for l1
def vaccine_date_count():
    review = db.iterview('vaccine_analysis/vaccine_date', db1.__len__(), group=True, group_level=3)
    count = []
    date =[]
    for row in review:
        date.append(listToString(row.key).strip())
        count.append(row.value['count'])
    return date, count


# vaccine data for l2
def vaccine_date_polarity_sub():
    """
    view_detail = db['_design/vaccine_analysis']['views']['vaccine_date']
    mapping = view_detail['map']
    reducing = view_detail['reduce']"""
    review = db.iterview('vaccine_analysis/vaccine_date', db1.__len__(), group=True, group_level=3)
    pol = []
    date = []
    for row in review:
        date.append(listToString(row.key).strip())
        pol.append(row.value['average'])
    """
    view_detail2 = db['_design/vaccine_analysis']['views']['vaccine_date_sub']
    mapping = view_detail2['map']
    reducing = view_detail2['reduce']"""
    review1 = db.iterview('vaccine_analysis/vaccine_date_sub', db1.__len__(), group=True, group_level=3)
    sub=[]
    for row in review1:
        sub.append(row.value['average'])
    return date, pol, sub


# vaccine data for c1
def vaccine_map():
    review_loc = db1.iterview('vaccine_analysis/vaccine_region', db1.__len__(), group=True, group_level=1)
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


# vaccine data for r1
def vaccine_aurin_compare():
    db_aurin = couch_client2['aurin_vaccine']
    state = ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'ACT']
    mango = {
        "selector": {},
        "fields": [
            "city",
            "response to recommend: disagree",
            "response to recommend: neutral",
            "response to recommend: agree",
            "response to early bird: disagree",
            "response to early bird: neutral",
            "response to early bird: agree",
        ],
        "limit": db.__len__()
    }
    contains = db_aurin.find(mango)
    mat = np.zeros((len(state), 9))
    for info in contains:
        mat[state.index(info['city'])][0] = info['response to recommend: disagree']
        mat[state.index(info['city'])][1] = info['response to recommend: neutral']
        mat[state.index(info['city'])][2] = info['response to recommend: agree']
        mat[state.index(info['city'])][3] = info['response to early bird: disagree']
        mat[state.index(info['city'])][4] = info['response to early bird: neutral']
        mat[state.index(info['city'])][5] = info['response to early bird: agree']

    review_loc = db2.iterview('vaccine_analysis/vaccine_aurin', db1.__len__(), group=True, group_level=1)
    eight_city_key= ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide', 'Gold Coast', 'Canberra',
                          'Newcastle']
    count_region=np.zeros(len(eight_largest_city))
    for row in review_loc:
        count_region[eight_city_key.index(row.key[0])]+=row.value['count']
    count_state=np.zeros(len(state))
    for item in range(len(eight_largest_city)):
        count_state[state.index(eight_largest_city_state[item])]+=count_region[item]
    review_loc1 = db2.iterview('vaccine_analysis/vaccine_aurin', db1.__len__(), group=True, group_level=2)
    attitude=['negative','neutral','positive']
    output = []
    for row in review_loc1:
        #print(eight_largest_city_index[eight_largest_city.index(listToString(row.key))])
        row_in_mat=state.index(eight_largest_city_state[eight_key.index(listToString(row.key[0]))])
        mat[row_in_mat][attitude.index(row.key[1])+6]+=row.value['count']
        #mat[row_in_mat][attitude.index(row.key[1])+6] += row.value['count']/count_state[row_in_mat]
    for i in range(len(mat)):
        mat[i][6]=mat[i][6]/count_state[i]*100
        mat[i][7] = mat[i][7] / count_state[i]*100
        mat[i][8] = mat[i][8] / count_state[i]*100
    for n_lengend in range(6):
        legend=[]
        if n_lengend<3:
            for i in range(len(mat)):
                legend.append([mat[i][n_lengend],mat[i][n_lengend+6]])
        else:
            for i in range(len(mat)):
                legend.append([mat[i][n_lengend],mat[i][n_lengend+3]])
        output.append(legend)

    return output

#print(vaccine_aurin_compare())


# vaccine data for r2
def vaccine_cloud():

    review_loc = db3.iterview('vaccine_analysis/vaccine_region', db1.__len__(), group=True, group_level=1)
    output = []
    for row in review_loc:
        if listToString(row.key) in eight_largest_city:
            output.append({'name': listToString(row.key), 'value': row.value['average']})
    return output

#print(vaccine_cloud())


