from fastapi import APIRouter
from .shell import Shell


router = APIRouter(
    prefix='/api/v1/chap-secrets',
    tags=['chap-secrets']
)


@router.on_event('startup')
async def startup_event():  # noqa: D103
    bash = Shell()
    bash.check_chap_secrets_file()


@router.get('/')
async def get_users():
    """Read /etc/ppp/chap-secrets file.

    Returns: lines file.
    """
    return Shell.read_chap_secrets_file()
