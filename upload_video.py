# Code from:
# https://learndataanalysis.org/how-to-upload-a-video-to-youtube-using-youtube-data-api-in-python/

from Google import Create_Service
from googleapiclient.http import MediaFileUpload

from argparse import ArgumentParser as arg_parser
from os.path import basename as basename
from re import sub as sub

CLIENT_SECRET_FILE = '/home/jose/Documents/GithubProjects/VideoUploaderMachine/client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
THUMBNAIL_PATH = '/home/jose/Pictures/thumbnail.jpg'

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

parser = arg_parser("simple_parser")
# TODO: Add argument for thumbnail with THUMBNAIL_PATH as default 
parser.add_argument(
        "--file", 
        help="Name of the file to be uploaded including path", 
        action='store',
        type=str)
args = parser.parse_args()

file_path = args.file
file_name = basename(file_path)
title_name = sub(r"[_-]", ' ', file_name[:file_name.find('.')])

request_body = {
        'snippet': {
            'categoryId': 28,
            'title': title_name,
            'description': 'Daily grind',
            'tags': ['Studying', 'Computer Science', 'Math']
            },
        'status': {
            'privacyStatus': 'unlisted',
            'selfDeclaredMadeForKids': False,
            },
        'notifySubscribers': False
        }

media_file = MediaFileUpload(file_name)

response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
        ).execute()

service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload(THUMBNAIL_PATH)
        ).execute()
