import couchdb
import time
import json
import numpy as np
import pandas as pd
couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
db = couchclient['no_duplicate_twitter']


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
source_list=["Twitter for Android ", "Twitter for iPhone "]
time_list=['0 0 ','0 1 ','0 2 ','0 3 ','0 4 ','0 5 ','0 6 ','0 7 ','0 8 ','0 9 ','1 0 ','1 1 ','1 2 ','1 3 ','1 4 ','1 5 ','1 6 ','1 7 ','1 8 ','1 9 ','2 0 ','2 1 ','2 2 ','2 3 ']
source_key=['T w i t t e r   f o r   A n d r o i d ','T w i t t e r   f o r   i P h o n e ']

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele + " "
        # return string
    return str1

def vaccine_cloud():
    view_detail = db['_design/vaccine_analysis']['views']['vaccine_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    db1 = client['no_duplicate_twitter']
    review_loc = db.iterview('vaccine_analysis/vaccine_region', db1.__len__(), group=True, group_level=1)
    output=[]
    dict={}
    for row in review_loc:
        if listToString(row.key) in eight_largest_city:
            dict.update({'name':listToString(row.key).strip(),'value':row.value['count']})
            output.append(dict)
    return output


def vaccine_map():
    view_detail = db['_design/vaccine_analysis']['views']['vaccine_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    db1 = client['no_duplicate_twitter']
    review_loc = db.iterview('vaccine_analysis/vaccine_region', db1.__len__(), group=True, group_level=1)
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

#print(vaccine_map())

def vaccine_date_count():
    view_detail = db['_design/vaccine_analysis']['views']['vaccine_date']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    db1 = client['no_duplicate_twitter']
    review = db.iterview('vaccine_analysis/vaccine_date', db1.__len__(), group=True, group_level=3)
    count = []
    date =[]
    for row in review:
        date.append(listToString(row.key).strip())
        count.append(row.value['count'])
    return date,count


def vaccine_date_polarity_sub():
    """
    view_detail = db['_design/vaccine_analysis']['views']['vaccine_date']
    mapping = view_detail['map']
    reducing = view_detail['reduce']"""
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    #db1 = client['no_duplicate_twitter']
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
#print(vaccine_date_polarity_sub())

def vaccine_aurin_compare():
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    db1 = client['no_duplicate_twitter']
    review_loc = db.iterview('vaccine_analysis_region/vaccine_region', db1.__len__(), group=True, group_level=3)
    output = []
    for row in review_loc:
        if listToString(row.key) in eight_largest_city:
            temp = []
            dict = {}
            temp.append(eight_largest_city_index[eight_largest_city.index(listToString(row.key))][0])
            temp.append(eight_largest_city_index[eight_largest_city.index(listToString(row.key))][1])
            temp.append(row.value['average'])
            dict.update({'name': listToString(row.key).strip(), 'value': temp})
            output.append(dict)
    return output
"""
def time_cloud():
    time_slot=['morning','noon','evening']
    db_time_cloud = couchclient['no_duplicate_twitter']
    mango = {
        "selector": {},
        "fields": [
            "time_slot",
            "location cloud"
        ],
        "limit": db.__len__()
    }
    contains=db_time_cloud.find(mango)
    output={}
    for row in contains:
        temp=[]
        for i in row["location cloud"]:
            temp.append({'name':i[0],'value':i[1]})
        output.update({row['time_slot']:temp})
    return output"""

def time_count_trend():
    view_detail = db['_design/time_analysis']['views']['time_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    #db1 = client['no_duplicate_twitter']
    review_time = db.iterview('time_analysis/time_polarity', db1.__len__(), group=True, group_level=3)
    output=[]
    for row in review_time:
        output.append(row.value['count'])
    return output


def time_sub_pol_trend():
    view_detail = db['_design/time_analysis']['views']['time_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    #db1 = client['no_duplicate_twitter']
    review_time_pol = db.iterview('time_analysis/time_polarity', db1.__len__(), group=True, group_level=1)

    view_detail = db['_design/time_analysis']['views']['time_sub']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_time_sub = db.iterview('time_analysis/time_sub', db1.__len__(), group=True, group_level=1)
    pol=[]
    sub=[]
    output=[]
    for row in review_time_pol:
        pol.append(row.value['average'])
    for row in review_time_sub:
        sub.append(row.value['average'])
    output.append(pol)
    output.append(sub)
    return output


def time_map():
    view_detail = db['_design/time_analysis']['views']['time_region_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_time_pol = db.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=2)
    """
    view_detail = db['_design/time_analysis']['views']['time_region_sub']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_time_sub = db.iterview('time_analysis/time_region_sub', db1.__len__(), group=True, group_level=2)"""

    mat=np.zeros((8,24))
    output = []
    for row in review_time_pol:
        mat[eight_key.index(listToString(row.key[0]))][time_list.index(listToString(row.key[1]))]=row.value['average']
    for i in range(len(eight_largest_city)):
        temp=[]
        temp.append(eight_largest_city_index[i][0])
        temp.append(eight_largest_city_index[i][1])
        time=[]
        for j in range(len(mat[0])):
            time.append(mat[i][j])
        temp.append(time)
        output.append({'name': eight_largest_city[i].strip(), 'value': temp})
    return output
print(time_map())

def time_region_count_percent_plot():
    view_detail = db['_design/time_analysis']['views']['time_region_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    #db1 = client['no_duplicate_twitter']
    review_map1 = db.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=2)
    review_map2 = db.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=1)
    eight_key_l1 = [['Adelaide'],['Brisbane'],['Canberra'],['Gold Coast'],['Sydney'],['Melbourne'], ['Perth (WA)'],
                          ['Newcastle']]
    mat=np.zeros((24,8))
    output = []
    total=np.zeros(len(eight_largest_city))
    for row in review_map2:
        total[eight_key_l1.index(row.key)]=row.value['count']
    for row in review_map1:
        mat[time_list.index(listToString(row.key[1]))][eight_key.index(listToString(row.key[0]))]=row.value['count']
    for i in range(24):
        temp=[]
        for j in range(len(mat[0])):
            temp.append({'name':eight_largest_city[j].strip(),'value':mat[i][j]/total[j]})
        output.append({time_list[i].strip():temp})
    return output

#print(time_region_count_percent_plot())

def time_cloud():
    view_detail = db['_design/time_analysis']['views']['time_region_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    db1 = client['no_duplicate_twitter']
    review_map1 = db.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=2)
    #review_map2 = db.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=None)

    morning=['06','07','08 ','09 ','10','11','12']
    afternoon=['13','14','15','16','17','18','19']
    night=['20','21','22','23','00','01','02','03','04','05']
    mat = np.zeros((3, 8))
    output = []

    for row in review_map1:
        #print(row.key[1])
        if row.key[1] in morning:
            mat[0][eight_key.index(listToString(row.key[0]))] = row.value['count']
        elif row.key[1] in afternoon:
            mat[1][eight_key.index(listToString(row.key[0]))] = row.value['count']
        else:
            mat[2][eight_key.index(listToString(row.key[0]))] = row.value['count']
    for i in range(3):
        temp = []
        for j in range(len(mat[0])):
            temp.append({'name': eight_largest_city[j].strip(), 'value': mat[i][j]})
        if i==0:
            output.append({'morning': temp})
        elif i==1:
            output.append({'afternoon': temp})
        else:
            output.append({'night': temp})
    return output

#print(time_cloud())

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
    output.append(IOS)
    output.append(android)
    return output

#print(source_time_plot())

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
            android.append(row.value['average'])
        else:
            IOS.append(row.value['average'])
    for rows in review_source_sub:
        if rows.key[0] in source_list[0]:
            android.append(rows.value['average'])
        else:
            IOS.append(rows.value['average'])
    output=[]
    output.append(IOS)
    output.append(android)
    return output

#print(source_polarity_subjectivity())

def source_region_map():
    view_detail = db['_design/source_analysis']['views']['source_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_region = db.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=2)
    mat = np.zeros((8, 2))
    output = []
    for row in review_source_region:
        mat[eight_key.index(listToString(row.key[0]))][source_key.index(listToString(row.key[1]))] =row.value['average']
    for i in range(len(eight_largest_city)):
        temp = []
        temp.append(eight_largest_city_index[i][0])
        temp.append(eight_largest_city_index[i][1])
        source = []
        for j in range(len(mat[0])):
            source.append(mat[i][j])
        temp.append(source)
        output.append({'name': eight_largest_city[i].strip(), 'value': temp})
    return output

#print(source_region_map())

def source_region_percentage():
    view_detail = db['_design/source_analysis']['views']['source_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_source_region1 = db.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=1)
    review_source_region2 = db.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=2)
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

#print(source_region_percentage())

def source_cloud():
    view_detail = db['_design/source_analysis']['views']['source_region']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #review_source_region1 = db.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=1)
    review_source_cloud = db.iterview('source_analysis/source_region', db1.__len__(), group=True, group_level=2)
    mat = np.zeros((2, 8))
    total_count_region = []
    output = []
    for row in review_source_cloud:
        mat[source_key.index(listToString(row.key[1]))][eight_key.index(listToString(row.key[0]))] = row.value['count']
    for i in range(len(source_list)):
        temp = []
        for j in range(len(mat[0])):
            temp.append({'name':eight_largest_city[j].strip(),'value':mat[i][j]})
        output.append({source_list[i].strip():temp})
    return output

#print(source_cloud())
