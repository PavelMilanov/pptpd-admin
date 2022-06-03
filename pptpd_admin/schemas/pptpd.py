from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .shell import Shell
from models.base import User


router = APIRouter(
    prefix='/api/v1/pptpd',
    tags=['pptpd']
)


@router.on_event('startup')
def startup_event():  # noqa: D103
    bash = Shell()
    bash.check_chap_secrets_file()


@router.get('/')
def get_users():
    """Read /etc/ppp/chap-secrets file.

    Returns: lines file.
    """
    config = Shell()
    return config.read_chap_secrets_file()


@router.get('/{client}')
def get_user_by_client(client: str):
    """Search and get request data in config file.

    Args:
        client (str): client name for  config file

    Returns: Responce User model for client
    """
    config = Shell()
    try:
        data = config.get_user_by_client(client)
        response = User(**data)
        return response
    except TypeError:
        return JSONResponse(
            status_code=404,
            content={'error': 'client not found'}
        )


@router.delete('/{client}')
def delete_user_by_client(client: str):
    """Delete request data in config file.

    Args:
        client (str): client name for config file

    Returns: Responce User model for client
    """
    config = Shell()
    try:
        data = config.delete_user_by_client(client)
        response = User(**data)
        return response
    except TypeError:
        return JSONResponse(
            status_code=404,
            content={'error': 'client not found'}
        )


@router.post('/')
def add_user_by_client(client: User):
    """Add request data in config file.

    Args:
        client (User)

    Returns: Responce User model for client
    """
    config = Shell()
    try:
        data = config.create_user(client.dict())
        response = User(**data)
        return response
    except TypeError:
        return JSONResponse(
            status_code=404,
            content={'error': 'client not found'}
        )
