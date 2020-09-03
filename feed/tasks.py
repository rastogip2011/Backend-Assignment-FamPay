from background_task import background
from .models import Feed
import requests
import json

@background(schedule=5)
def populate_db():

    keys = get_key()
    Feed.objects.all().delete()
    link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&order=date&q=football&key='

    for key in keys:

        response = requests.get(link+key)
        
        if str(response) == '<Response [403]>':
            continue
        
        data = response.json()

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
        
        break

def get_key():
    key_file = open('keys.txt')
    keys = key_file.read().split('\n')
    return keys