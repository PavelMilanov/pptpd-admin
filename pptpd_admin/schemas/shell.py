import subprocess
import re
from models.base import User


SUPPORT_OS = ('ubuntu', 'debian')


def check_os(func):  # noqa: D103
    def wrapped(*args):
        """Check os-release file."""
        try:
            info = subprocess.check_output(
                ['cat', '/etc/os-release'],
                text=True
            )
            os_name = re.search('ID=[a-z]+', info)[0][3:]  # os_name[0]>ID=ubuntu
            if os_name in SUPPORT_OS:
                func(*args)
            else:
                raise subprocess.CalledProcessError('Your operating system not supported')
        except subprocess.CalledProcessError:
            print('Your operating system not supported')
    return wrapped


class Shell:
    """Use shell-command over Python."""

    _CHAP_SECRETS_FILE = '/etc/ppp/chap-secrets'
    _PPTDP_OPTIONS_FILE = '/etc/pp/pptpd-options'
    _VPN_USERS = {}


    @check_os
    def _get_vpnserver_name(self) -> str:
        """Return name vpn server on /etc/ppp/pptpd-options file.
        
        Line: name <vpn-name>
        """
        with open(self._PPTDP_OPTIONS_FILE) as file:
            text = re.search('name [a-z]+', file.read())[0]
            return text.split()[1]

    @check_os
    def check_chap_secrets_file(self) -> None:
        """Check chap-secrets file on ppp/ direcrory."""
        status_code = subprocess.call(
            ['cat', self._CHAP_SECRETS_FILE],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        if status_code != 0:
            raise FileNotFoundError('pptpd package not installed')

    def read_chap_secrets_file(self) -> dict:
        """Read chap-secrets file.
   
        # Secrets for authentication using CHAP
        # client  server  secret  IP addresses
        # user vpn password *

        Returns: dict
        """
        with open(self._CHAP_SECRETS_FILE) as file:
            vpnname_from_config = self._get_vpnserver_name()
            for count,line in enumerate(file.readlines(), start=-1):  # 2 lines config pass
                if not line.startswith('#'):
                    config_string = line.strip().split()
                    self._VPN_USERS[count] = {
                        'client': config_string[0],
                        'server': vpnname_from_config,
                        'secret': config_string[2],
                        'ip': config_string[3]
                                }
        return self._VPN_USERS
