from pydantic import BaseModel


class User(BaseModel):
    # colimn in chap-secrets file
    client: str
    server: str
    secret: str
    ip: str = '*'
