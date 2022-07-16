from time import sleep
from isodate import parse_duration
from django.conf import settings
import requests
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials



databaseURL='https://youtubesearch-356406-default-rtdb.firebaseio.com/'
cred = credentials.Certificate("youtube/Utils/youtubesearch-356406-firebase-adminsdk-i3koy-976a3ded84.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':databaseURL
	})
ref = db.reference("/")

def write(dict_val):
    for key in dict_val.keys():
        ref.child('video').push().set(dict_val[key])
    print('written')

query_search='football'
data_api_key1='AIzaSyDJEndrDUdTtJ30w5wBP9pKPBZSaJyJuVM'
data_api_key2='AIzaSyDyR6yGuSudIu5d_49lIHIt7hEmY7My3H4'
num_query=5

def request_util(api_key):
    search_url='https://www.googleapis.com/youtube/v3/search'
    video_url='https://www.googleapis.com/youtube/v3/videos'
    search_params={
        'part':'snippet',
        'q':query_search,
        'key':api_key,
        'max_results':num_query,
        'type':'video',
        'order':'date'
    }
    r = requests.get(search_url,search_params)
    result=r.json()['items']
    result=r.json()['items']
    video_ids=[]
    for res in result:
        video_ids.append(res['id']['videoId'])
    video_params={
        'part':'snippet,contentDetails',
        'id':','.join(video_ids),
        'key':api_key,
        'max_results':num_query,
    }
    r=requests.get(video_url,video_params)
    result=r.json()['items']
    dict_res={}
    for res in result:
        dict_vd={}
        dict_vd['id']=res['id']
        dict_vd['title']=res['snippet']['title']
        dict_vd['duration']=(parse_duration(res['contentDetails']['duration']).total_seconds())/60
        dict_vd['url']=res['snippet']['thumbnails']['default']['url']
        dict_vd['publish_date']=res['snippet']['publishedAt'][0:10]
        dict_vd['publish_time']=res['snippet']['publishedAt'][11:19]
        dict_vd['description']=res['snippet']['description']
        dict_res[res['id']]=dict_vd
    write(dict_res)
    print("Requested for data")

def request_video():
    api_key_list=[data_api_key1,data_api_key2]
    try:
        request_util(api_key_list[0])
    except:
        print("Youtube API1 Error ..... Trying API2......")
        try:
            request_util(api_key_list[1])
        except:
            print("Youtube API2 Error")

def mn():
    while True:
        request_video()
        sleep(10)