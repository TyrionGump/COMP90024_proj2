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
# Related DB Name:
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


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele + " "
        # return string
    return str1


# source data for l1
def source_time_plot():
    view_detail = db['_design/source_analysis']['views']['source_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_time_plot = db.iterview('source_analysis/source_polarity', db1.__len__(), group=True, group_level=2)
    #mat=np.zeros((2,24))
    IOS=[]
    android=[]
    for row in review_source_time_plot:
        if row.key[0] in source_list[0]:
            android.append(row.value['count'])
        else:
            IOS.append(row.value['count'])
    output=[]
    output.append(android)
    output.append(IOS)
    return output
#print(source_time_plot())

# source data for l2
def source_polarity_subjectivity():
    view_detail = db['_design/source_analysis']['views']['source_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_pol = db.iterview('source_analysis/source_polarity', db1.__len__(), group=True, group_level=1)
    view_detail = db['_design/source_analysis']['views']['source_sub']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_sub = db.iterview('source_analysis/source_sub', db1.__len__(), group=True, group_level=1)
    IOS=[]
    android=[]
    for row in review_source_pol:
        if row.key[0] in source_list[0]:
            android.append(round(row.value['average'], 2))
        else:
            IOS.append(round(row.value['average'], 2))
    for rows in review_source_sub:
        if rows.key[0] in source_list[0]:
            android.append(round(rows.value['average'], 2))
        else:
            IOS.append(round(rows.value['average'], 2))
    output = []
    for i in range(len(IOS)):
        output.append([android[i], IOS[i]])


    return output


# source data for c1
def source_region_pol():
    view_detail = db1['_design/source_analysis']['views']['source_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_region = db1.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=2)
    mat = np.zeros((8, 2))
    output_Andriod = []
    output_IOS = []
    for row in review_source_region:
        mat[eight_key.index(listToString(row.key[0]))][source_key.index(listToString(row.key[1]))] = row.value[
            'average']
    for i in range(len(eight_largest_city)):
        temp = []
        temp.append(eight_largest_city_index[i][0])
        temp.append(eight_largest_city_index[i][1])
        temp.append(mat[i][0])
        output_Andriod.append({'name': eight_largest_city[i].strip(), 'value': temp})
    for i in range(len(eight_largest_city)):
        temp1 = []
        temp1.append(eight_largest_city_index[i][0])
        temp1.append(eight_largest_city_index[i][1])
        temp1.append(mat[i][1])
        output_IOS.append({'name': eight_largest_city[i].strip(), 'value': temp1})
    return output_Andriod, output_IOS

#print(source_region_pol())

# source data for r1
def source_region_percentage():
    view_detail = db2['_design/source_analysis']['views']['source_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_region1 = db2.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=1)
    review_source_region2 = db2.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=2)
    mat = np.zeros((2, 8))
    total_count_region=np.zeros(len(eight_largest_city))
    for row in review_source_region1:
        total_count_region[eight_key.index(listToString(row.key[0]))]=row.value['count']
    output = []
    for rows in review_source_region2:
        mat[source_key.index(listToString(rows.key[1]))][eight_key.index(listToString(rows.key[0]))]=rows.value['count']
    for i in range(len(source_list)):
        temp = []
        for j in range(len(mat[0])):
            temp.append(mat[i][j]/total_count_region[j])
        output.append(temp)
    return output


# source data for r2
def source_cloud():
    view_detail = db3['_design/source_analysis']['views']['source_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #review_source_region1 = db.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=1)
    review_source_cloud = db3.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=2)
    mat = np.zeros((2, 8))
    total_count_region = []
    output = []
    for row in review_source_cloud:
        mat[source_key.index(listToString(row.key[1]))][eight_key.index(listToString(row.key[0]))] = row.value['average']
    for i in range(len(source_list)):
        temp = []
        for j in range(len(mat[0])):
            temp.append({'name':eight_largest_city[j].strip(),'value':mat[i][j]})
        output.append({source_list[i].strip():temp})
    return output


