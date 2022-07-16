from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse
from isodate import parse_duration
from django.conf import settings
from youtube.Utils.cloud_util import write
from youtube.Utils.search_util import search_query,sort_entires
from django.core.paginator import Paginator

# Create your views here.
def request_video():
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
        print(res)
        dict_vd['id']=res['id']
        dict_vd['title']=res['snippet']['title']
        dict_vd['duration']=(parse_duration(res['contentDetails']['duration']).total_seconds())/60
        dict_vd['url']=res['snippet']['thumbnails']['default']['url']
        dict_vd['publish_date']=res['snippet']['publishedAt'][0:10]
        dict_vd['publish_time']=res['snippet']['publishedAt'][11:19]
        dict_vd['description']=res['snippet']['description']
        dict_res[res['id']]=dict_vd
    write(dict_res)
    return HttpResponse('Requested')

def parse_json(dict_res):
    list_res=[]
    for key in dict_res.keys():
        list_res.append(dict_res[key])
    return list_res

def search(request):

    data = json.loads(request.body.decode("utf-8"))
    q_name = data.get('query')
    match_description=0
    try:
        match_description = data.get('match_description',0)
    except:
        pass
    result=search_query(q_name,match_description)
    res=result['object']
    res['Key_Word_Match']=result['matches']
    return JsonResponse(res, status=201)


def sort_query(request):
    data = json.loads(request.body.decode("utf-8"))
    page_num = data.get('page',1)
    result=sort_entires()
    res=result
    ls=parse_json(res)
    ln_list=len(ls)
    if(page_num>ln_list):
        return HttpResponse(f"Number of page {page_num} is greater than total entries {ln_list}")
    p = Paginator(ls,1,allow_empty_first_page=False)
    page = p.page(page_num)
    return HttpResponse(page)
    
