from injector import inject, singleton

import python_jwt as jwt, jwcrypto.jwk as jwk, datetime

from .interfaces import Settings
from .interfaces import JWTService

@singleton
class JWTServiceImpl(JWTService):

    @inject
    def __init__(self, s: Settings):
        self.settings = s

    def sign(self, payload: dict) -> str:
        ks = jwk.JWKSet()
        ks = self.settings.jwks(ks)

        k = list(ks["keys"])[0]

        resp_token = jwt.generate_jwt(payload, k, 'RS256',
                                      datetime.timedelta(minutes=5),
                                      datetime.datetime.now(),
                                      datetime.datetime.now(), 16,
                                      {"kid": "alg1"})

        return resp_token
