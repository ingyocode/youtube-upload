import json
from google_auth_oauthlib.flow import InstalledAppFlow

# OAuth 2.0 클라이언트 ID 파일 경로
CLIENT_SECRETS_FILE = 'client_secrets.json'

# 인증 범위 설정
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    
    # 토큰을 JSON 파일로 저장
    with open('token.json', 'w') as token_file:
        token_data = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
        json.dump(token_data, token_file)

authenticate()