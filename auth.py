import json
from google_auth_oauthlib.flow import InstalledAppFlow
import argparse
import os

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def authenticate(args):
    flow = InstalledAppFlow.from_client_secrets_file(args.clientSecret, SCOPES)
    credentials = flow.run_local_server(port=0)
    
    # 토큰을 JSON 파일로 저장
    with open(args.tokenFile, 'w') as token_file:
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
parser.add_argument("--clientSecret", required=True, help="OAuth Client Secrets file name")
parser.add_argument("--tokenFile", required=True, help="output token file name")
args = parser.parse_args()

if not os.path.exists(args.clientSecret):
    exit("Please specify a valid input file name using the --clientSecret= client secret file.")

authenticate(args)