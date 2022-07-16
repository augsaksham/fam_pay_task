import youtube.Utils.cloud_util as cloud
from functools import cmp_to_key
def search_query(query,match_description):
    query=query.lower()
    entries=cloud.get_data()
    entries=dict(entries)
    dict_res={'id':'null','object':{},'matches':0}
    words=query.split()
    for key in entries.keys():
        cnt=0
        title=entries[key]['title']
        title=title.lower()
        for word in words:
            if(word in title):
                cnt+=1
        if(match_description==1):
            description=entries[key]['description']
            description=description.lower()
            for word in words:
                if(word in description):
                    cnt+=1
        if(dict_res['matches']<cnt):
            dict_res['id']=key
            dict_res['matches']=cnt
            dict_res['object']=entries[key]
        elif (dict_res['matches']==cnt):
            if(title==query):
                dict_res['id']=key
                dict_res['matches']=cnt
                dict_res['object']=entries[key]
    return dict_res

def compare(pair1, pair2):
    id1,publish_date1, publish_time1 = pair1
    id2,publish_date2, publish_time2 = pair2
    if publish_date1>publish_date2:
        return 1
    elif publish_date1==publish_date2:
        if publish_time1>publish_time2:
            return 1
    return -1

def sort_entires():
    dict_res=cloud.get_data()
    dict_res=dict(dict_res)
    list_srt=[]
    for key in dict_res.keys():
        ls=[]
        ls.append(key)
        ls.append(dict_res[key]['publish_date'])
        ls.append(dict_res[key]['publish_time'])
        list_srt.append(ls)
    compare_key = cmp_to_key(compare)
    sorted_l = sorted(list_srt, key=compare_key,reverse=True)
    sorted_dict={}
    for en in sorted_l:
        id=dict_res[en[0]]['id']
        sorted_dict[id]=dict_res[en[0]]

    return sorted_dict


    