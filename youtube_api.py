import os
import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# OAuth 2.0 配置
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
CLIENT_SECRET_FILE = './client_secret_755162217688-0o3oofinpplkfksae81otqho4mm8jd0q.apps.googleusercontent.com.json'
TOKEN_PICKLE_FILE = 'token.pickle'

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return googleapiclient.discovery.build('youtube', 'v3', credentials=creds) 