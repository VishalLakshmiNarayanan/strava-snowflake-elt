import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def get_initial_tokens():
    client_id = os.getenv('STRAVA_CLIENT_ID')
    client_secret = os.getenv('STRAVA_CLIENT_SECRET')
    auth_code = os.getenv('STRAVA_AUTH_CODE')

    if not auth_code:
        print("Error: STRAVA_AUTH_CODE missing from .env")
        return

    url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'grant_type': 'authorization_code'
    }

    print(f"Requesting tokens for Client ID: {client_id}...")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        res_json = response.json()
        print("\n--- SUCCESS! Copy these to your .env ---")
        print(f"STRAVA_ACCESS_TOKEN={res_json['access_token']}")
        print(f"STRAVA_REFRESH_TOKEN={res_json['refresh_token']}")
    else:
        print(f"Failed! Status: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    get_initial_tokens()