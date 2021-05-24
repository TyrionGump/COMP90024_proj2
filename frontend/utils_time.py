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


# time data for l1
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


# time data for l2
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


# time data for c1
def time_map_24():
    view_detail = db1['_design/time_analysis']['views']['time_region_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_time_pol = db1.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=2)
    """
    view_detail = db['_design/time_analysis']['views']['time_region_sub']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    review_time_sub = db.iterview('time_analysis/time_region_sub', db1.__len__(), group=True, group_level=2)"""

    mat = np.zeros((8, 24))

    output=[]
    for row in review_time_pol:
        mat[eight_key.index(listToString(row.key[0]))][time_list.index(listToString(row.key[1]))] = row.value['average']
    for j in range(len(time_list)):
        hourly_result = []
        for i in range(len(eight_largest_city)):
            temp = []
            temp.append(eight_largest_city_index[i][0])
            temp.append(eight_largest_city_index[i][1])
            temp.append(mat[i][j])
            hourly_result.append({'name': eight_largest_city[i].strip(), 'value': temp})
        output.append(hourly_result)
    return output


# time data for r1
def time_region_count_percent_plot():
    view_detail = db2['_design/time_analysis']['views']['time_region_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    #client = couchdb.client.Server('http://admin:admin@172.26.130.240:5984/')
    #db1 = client['no_duplicate_twitter']
    review_map1 = db2.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=2)
    review_map2 = db2.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=1)
    eight_key_l1 = ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide', 'Gold Coast', 'Canberra',
                    'Newcastle']
    mat=np.zeros((24,8))
    output = []
    total=np.zeros(len(eight_largest_city))
    for row in review_map2:
        total[eight_key_l1.index(row.key[0])]=row.value['count']
    # print(total)
    for row in review_map1:
        mat[time_list.index(listToString(row.key[1]))][eight_key.index(listToString(row.key[0]))]+=row.value['count']
    # print(mat)
    for i in range(24):
        temp=[]
        for j in range(len(mat[0])):
            print(eight_key_l1[j])
            print(mat[i][j])
            print(total[j])
            temp.append({'name':eight_largest_city[j].strip(),'value':mat[i][j]/total[j]})
        output.append({time_list[i].strip():temp})
    return output


# time data for r2
def time_cloud():
    view_detail = db3['_design/time_analysis']['views']['time_region_polarity']
    mapping = view_detail['map']
    reducing = view_detail['reduce']
    db1 = couch_client3['no_duplicate_twitter']
    review_map1 = db3.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=2)
    #review_map2 = db.iterview('time_analysis/time_region_polarity', db1.__len__(), group=True, group_level=None)

    morning=['06','07','08 ','09 ','10','11','12']
    afternoon=['13','14','15','16','17','18','19']
    night=['20','21','22','23','00','01','02','03','04','05']
    mat = np.zeros((3, 8))
    output = {}

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
            output['morning'] = temp
        elif i==1:
            output['afternoon'] = temp
        else:
            output['evening'] = temp
    return output
