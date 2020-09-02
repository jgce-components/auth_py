import typing
import abc


# tag::interfaces[]
class Authorizer(abc.ABC):
    @abc.abstractmethod
    def authorize(self, token: str) -> dict:
        """"""


class JWTService(abc.ABC):
    @abc.abstractmethod
    def sign(self, payload: dict) -> str:
        """"""


class Repository(abc.ABC):
    @abc.abstractmethod
    def get_role(self, email: str) -> str:
        """"""


class Settings(abc.ABC):
    @abc.abstractmethod
    def jwks(self, ks) -> str:
        """"""
# end::interfaces[]
