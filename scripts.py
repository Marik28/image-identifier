from secrets import token_urlsafe


def generate_jwt_secret() -> str:
    return token_urlsafe(32)
