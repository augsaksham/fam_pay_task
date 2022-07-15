from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from isodate import parse_duration
from django.conf import settings
from youtube.Utils.upload_to_cloud import write,get_data

# Create your views here.
def request_video(request):
    search_url='https://www.googleapis.com/youtube/v3/search'
    video_url='https://www.googleapis.com/youtube/v3/videos'
    search_params={
        'part':'snippet',
        'q':settings.QUERY,
        'key':settings.DATA_API_KEY,
        'max_results':settings.NUM_QUERY,
        'type':'video',
        'order':'date'
    }
    r = requests.get(search_url,search_params)
    result=r.json()['items']
    video_ids=[]
    for res in result:
        video_ids.append(res['id']['videoId'])
    video_params={
        'part':'snippet,contentDetails',
        'id':','.join(video_ids),
        'key':settings.DATA_API_KEY,
        'max_results':settings.NUM_QUERY,
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
    print("retieved data ")
    get_data()
    
    return HttpResponse('Requested')


def search(request):
    data = json.loads(request.body.decode("utf-8"))
    q_name = data.get('query')

    print("got query as ",q_name)

    return HttpResponse("Succss")
    
