from background_task import background
from .models import Feed
import requests
import json
import pprint

@background()
def populate_db():
    print("scheduled !!!!")
    
    keys = get_key()
    link = 'https://www.googleapis.com/youtube/v3/search/'

    # Automatic key selection

    existing_vid_ids = get_existing_vid_id()
    fetched_vid_ids = set()
    data_list = []

    nextPageToken = ""
    
    for i in range(0,5):
        verified_key = None
        data = None
        for key in keys:
            response = requests.get(link,
            params = {
                "part": 'snippet',
                "maxResults":50,
                "q":'football',
                "key" : key,
                "pageToken" : nextPageToken
            })
            
            if str(response) != '<Response [403]>':
                verified_key = key
                print(response)
                data = response.json()
                break

        if verified_key is None or data is None:
            print("All keys have expired, please add a new key in 'keys.txt'")
            return

        
        nextPageToken = data["nextPageToken"]

        for feed in data['items']:
            try:
                fetched_vid_ids.add(feed['id']['videoId'])
            except:
                print("exception")

        for fetched_feed in data['items']:
            try:
                vid_id = fetched_feed['id']['videoId']

                if (vid_id not in existing_vid_ids):

                    Vid_id = fetched_feed['id']['videoId']
                    snippet = fetched_feed['snippet']
                    Title = snippet['title']
                    Published_at = snippet['publishedAt']
                    Description = snippet['description']
                    Thumbnail = snippet['thumbnails']['default']
                    Thumbnail_url = Thumbnail['url']
                    
                    new_feed = Feed(vid_id=Vid_id, title=Title, description=Description, published_at=Published_at, thumbnail_url=Thumbnail_url)
                    # data_list.append(new_feed)
                    new_feed.save()
            except:
                pass
    
    print("Iteration completed!")
    feed = Feed.objects.all()

    for record in feed.iterator():
        if record.vid_id not in fetched_vid_ids:
            record.delete()


def get_key():
    key_file = open('keys.txt')
    keys = key_file.read().split('\n')
    return keys

def get_existing_vid_id():
    
    existing_vid_ids = set()
    feed = Feed.objects.all()

    for record in feed.iterator():
        existing_vid_ids.add(record.vid_id)

    return existing_vid_ids
