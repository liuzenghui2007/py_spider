import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# OAuth 2.0 配置
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
CLIENT_SECRET_FILE = './client_secret_755162217688-0o3oofinpplkfksae81otqho4mm8jd0q.apps.googleusercontent.com.json'  # 替换为你的 JSON 文件路径
TOKEN_PICKLE_FILE = 'token.pickle'

def get_authenticated_service():
    creds = None
    # 检查是否已有有效的凭据
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)
    # 如果没有有效的凭据，进行 OAuth 2.0 流程
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # 保存凭据以供下次使用
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

if __name__ == "__main__":
    get_authenticated_service()