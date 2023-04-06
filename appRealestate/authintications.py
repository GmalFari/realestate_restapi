from rest_framework.authentication import TokenAuthentication as BaseAuthenticate


class TokenAuthentication(BaseAuthenticate):
    keyword = 'Bearer'