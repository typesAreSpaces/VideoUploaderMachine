# Code from:
# https://learndataanalysis.org/how-to-upload-a-video-to-youtube-using-youtube-data-api-in-python/

from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
        'snippet': {
            'categoryId': 28,
            # TODO: Set 'title' from external argument
            'title': 'Test Video',
            'description': 'Daily grind',
            'tags': ['Studying', 'Computer Science', 'Math']
            },
        'status': {
            'privacyStatus': 'unlisted',
            'selfDeclaredMadeForKids': False,
            },
        'notifySubscribers': False
        }

# TODO: Set media file from external argument
mediaFile = MediaFileUpload('/home/jose/Videos/ScreenCasts/2021-12-08_08-34-16.mkv')

response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
        ).execute()

service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('/home/jose/Pictures/thumbnail.jpg')
        ).execute()
