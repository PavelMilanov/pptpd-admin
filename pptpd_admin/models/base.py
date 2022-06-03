from pydantic import BaseModel


class User(BaseModel):
    """Dataclass for users."""

    client: str
    server: str
    secret: str
    ip: str = '*'
