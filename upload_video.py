# Code from:
# https://learndataanalysis.org/how-to-upload-a-video-to-youtube-using-youtube-data-api-in-python/

import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# FIX: Change this (automate)
upload_date_time = datetime.datetime(2021, 12, 8).isoformat() + '.000Z'

request_body = {
    'snippet': {
        'categoryId': 28, 
        # TODO: Change this (automate)
        'title': 'Test video', 
        # TODO: Change this (automate)
        'description': 'Testing Youtube API', 
        # TODO: Figure out proper tags
        'tags': ['Travel', 'video test', 'Travel Tips']
    },
    'status': {
        'privacyStatus': 'unlisted',
        'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('/home/jose/Videos/ScreenCasts/2021-12-08_08-55-47.mkv')

response_upload = service.videos().insert(part='snippet,status', body=request_body, media_body=mediaFile).execute()

service.thumbnails().set(videoId=response_upload.get('id'), media_body=MediaFileUpload('/home/jose/Pictures/thumbnail.jpg')
).execute()
