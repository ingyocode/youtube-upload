import json
from google_auth_oauthlib.flow import InstalledAppFlow
import argparse
import os

# OAuth 2.0 클라이언트 ID 파일 경로
CLIENT_SECRETS_FILE = 'client_secrets.json'

# 인증 범위 설정
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def authenticate(args):
    flow = InstalledAppFlow.from_client_secrets_file(args.inputName, SCOPES)
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

parser = argparse.ArgumentParser(description='secret, token file name')
parser.add_argument("--inputName", required=True, help="OAuth Client Secrets file name")
parser.add_argument("--outputName", required=True, help="output token file name")
args = parser.parse_args()

if not os.path.exists(args.inputName):
    exit("Please specify a valid input file name using the --inputName= parameter.")

if not os.path.exists(args.outputName):
    exit("Please specify a valid input file name using the --inputName= parameter.")

authenticate(args)