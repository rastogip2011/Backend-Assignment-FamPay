from django.shortcuts import render
from .models import Feed
import requests
import json

def populate_db():

    Feed.objects.all().delete()
    link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&order=date&q=football&key=AIzaSyDXEUW-CXFFJtApIUgYPvW20FPf5BZUPew'

    data = requests.get(link).json()
    for feed in data['items']:
        Vid_id = feed['id']['videoId']
        snippet = feed['snippet']
        Title = snippet['title']
        Published_at = snippet['publishedAt']
        Description = snippet['description']
        Thumbnail = snippet['thumbnails']['medium']
        Thumbnail_url = Thumbnail['url']
        
        new_feed = Feed(vid_id=Vid_id, title=Title, description=Description, published_at=Published_at, thumbnail_url=Thumbnail_url)
        new_feed.save()


# Create your views here.
def index(request):
    
    populate_db()

    all_videos = Feed.objects.all()
    
    return render(request, 'index.html', {'Videos': all_videos})