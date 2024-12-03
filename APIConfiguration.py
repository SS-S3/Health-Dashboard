import os
from dotenv import load_dotenv
import requests
from requests_oauthlib import OAuth2Session

class StravaAPIClient:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Strava API credentials
        self.client_id = os.getenv('STRAVA_CLIENT_ID')
        self.client_secret = os.getenv('STRAVA_CLIENT_SECRET')
        self.redirect_uri = 'http://localhost:8000/exchange_token'
        
        # OAuth2 authorization URLs
        self.authorization_base_url = 'https://www.strava.com/oauth/authorize'
        self.token_url = 'https://www.strava.com/oauth/token'

    def get_authorization_url(self):
       
        oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri)
        authorization_url, state = oauth.authorization_url(
            self.authorization_base_url,
            scope=['activity:read_all,profile:read_all']
        )
        return authorization_url, state

    def exchange_token(self, authorization_response):
     
        oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri)
        token = oauth.fetch_token(
            self.token_url,
            client_secret=self.client_secret,
            authorization_response=authorization_response
        )
        return token

    def refresh_token(self, refresh_token):
    
        # Refresh the access token when it expires
    
        extra = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        oauth = OAuth2Session(self.client_id, token={'refresh_token': refresh_token, 'grant_type': 'refresh_token'})
        token = oauth.refresh_token(self.token_url, **extra)
        return token

    def get_athlete_activities(self, access_token, limit=10):
       
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(
            f'https://www.strava.com/api/v3/athlete/activities?per_page={limit}', 
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch activities: {response.text}")