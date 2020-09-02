from google.oauth2 import id_token
from google.auth.transport import requests
import requests as http_client

from injector import inject, singleton

import urllib.request
from .interfaces import Repository

from .interfaces import Settings
from .interfaces import Authorizer, JWTService


@singleton
class GCEAuthorizer(Authorizer):

    @inject
    def __init__(self, s: Settings, repo: Repository, jwt: JWTService):
        self.settings = s
        self.repo = repo
        self.jwt = jwt

    def authorize(self, token: str) -> dict:
        # https://developers.google.com/identity/sign-in/web/backend-auth
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token,
                                              requests.Request(),
                                              self.settings.CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com',
                                 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID
        # from the decoded token.
        # userid = idinfo['sub']

        payload = {'id_token': token}
        r = http_client.get('https://www.googleapis.com/oauth2/v3/tokeninfo',
                            params=payload)
        data = r.json()

        user_email = data["email"]
        role = self.repo.get_role(user_email)
        payload = {'role': role}
        resp_token = self.jwt.sign(payload)

        return {"token": resp_token}
