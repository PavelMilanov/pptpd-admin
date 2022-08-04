from pydantic import BaseModel
from typing import Union
from schemas.shell import bash


class User(BaseModel):
    """Dataclass for users."""

    client: str = 'login'
    server: Union[str, None] = bash.get_vpn_name()
    secret: str = 'password'
    ip: Union[str, None] = '*'
