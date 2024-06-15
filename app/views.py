from django.shortcuts import redirect, render
import requests

from app.models import SearchLog
from urbanjango import settings
import datetime


def index(request):
    return render(request, 'urbanjango/index.html')


def about(request):
    return render(request, 'urbanjango/about.html')


def define(request):
    if not request.method == 'GET':
        return redirect('index')
    
    term = request.GET.get('term', '')
    term = term.strip()[:255]  # limit to 255 characters
    if not term:
        return redirect('index')
    else:
        log_search(request)

    querystring = { 'term': term }
    headers = {
        "X-RapidAPI-Host": settings.RAPID_API_HOST,
        "X-RapidAPI-Key": settings.RAPID_API_KEY
    }
    response = requests.request("GET", settings.RAPID_API_URL, headers=headers, params=querystring)

    '''
    {
        "list": [
            {
                "definition": "[Exactly] [what you need], [exactly] when you [need it]. ",
                "permalink": "http://clutch.urbanup.com/1581805",
                "thumbs_up": 4022,
                "author": "FtG",
                "word": "clutch",
                "defid": 1581805,
                "current_vote": "",
                "written_on": "2006-01-09T02:33:28.000Z",
                "example": "\"The other day I was really hungry but thought I had [no money] on me. Then I found five [dollars] in my [jacket] pocket--that was clutch.\"",
                "thumbs_down": 1716
            },
            {
                "definition": "to [perform] [under pressure]",
                "permalink": "http://clutch.urbanup.com/268879",
                "thumbs_up": 4797,
                "author": "CPD",
                "word": "clutch",
                "defid": 268879,
                "current_vote": "",
                "written_on": "2003-09-29T00:54:47.000Z",
                "example": "In the last few seconds of a [close game], only a player with clutch can lead [the team] to [victory]. ",
                "thumbs_down": 2131
            },
            {
                "definition": "[coming in] [handy], [just what] was needed, essential or sweet",
                "permalink": "http://clutch.urbanup.com/789115",
                "thumbs_up": 109,
                "author": "P Meister",
                "word": "clutch",
                "defid": 789115,
                "current_vote": "",
                "written_on": "2004-08-10T22:52:35.000Z",
                "example": "Mike: Good thing we packed [the umbrella] [b4] we left\r\n[Cory]: Yeah def dude, it came clutch",
                "thumbs_down": 46
            },
        ]
    }
    '''

    if response.status_code == 200:
        results = response.json()['list']
        results.sort(key=lambda x: x['thumbs_up'], reverse=True)  # order by most thumbs_up

        # truncate the share_description to 200 characters
        share_description = results[0]['example'] if len(results) > 0 else ''
        share_description = share_description.replace('\r\n', ' ')[:200] + '...' if share_description else ''

    return render(request, 'urbanjango/define.html', {
        'term': term,
        'results': results if response.status_code == 200 else [],
        'results_count': len(results) if response.status_code == 200 else 0,
        'share_description': share_description
    })


def log_search(request):
    query = request.GET.get('term', '')
    if query:
        print(f"Logging search query: {query}, from IP: {request.META.get('REMOTE_ADDR', '')}, referrer: {request.META.get('HTTP_REFERER', '')}")
        ip_address = request.META.get('REMOTE_ADDR', '')
        referrer = request.META.get('HTTP_REFERER', '')

        log = SearchLog(query=query, ip_address=ip_address, referrer=referrer)
        log.save()