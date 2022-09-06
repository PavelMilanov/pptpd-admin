import subprocess
import re
import os
from typing import Dict


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
    _VPN_USERS: Dict[int, Dict] = {}

    def get_vpn_name(self) -> None:
        with open ('/etc/ppp/pptpd-options', 'r') as config:
            for line in config.readlines():
                pattern = re.search('^name *', line)                
                if pattern:
                    return line.strip().split()[1]  # "name pptpd\n"
    
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
        user vpn password *

        Returns: dick based on User model
        """
        with open(self._CHAP_SECRETS_FILE) as file:
            for count, line in enumerate(file.readlines(), start=-1):  # 2 lines config pass
                if not line.startswith('#'):
                    try:
                        config_string = line.strip().split()
                        self._VPN_USERS[(count-2)] = {
                            'client': config_string[0],
                            'server': config_string[1],
                            'secret': config_string[2],
                            'ip': config_string[3]
                        }
                    except IndexError:
                        pass
        return self._VPN_USERS

    def get_user_by_client(self, request: str):
        """Get client, server, secret and ip from /etc/ppp/chap-secrets by request.

        Args:
            request (str): client string in config file

        Returns: dick based on User model
        """
        with open(self._CHAP_SECRETS_FILE) as file:
            for line in file.readlines():
                if not line.startswith('#'):
                    try:
                        text = line.strip().split()
                        if text[0] == request:
                            return {
                                'client': text[0],
                                'server': text[1],
                                'secret': text[2],
                                'ip': text[3]
                            }
                    except IndexError:
                        pass

    def delete_user_by_client(self, request: str) -> dict:
        """Delete string from /etc/ppp/chap-secrets by request.

        Args:
            request (str): client string in config file

        Returns: dick based on User model
        """
        with open(self._CHAP_SECRETS_FILE) as file:
            for count, line in enumerate(file.readlines(), start=1):  # cat -n /etc/ppp/chap-secrets
                try:
                    text = line.strip().split()
                    if text[0] == request:
                        output = {
                            'client': text[0],
                            'server': text[1],
                            'secret': text[2],
                            'ip': text[3]
                        }
                        os.system(f"sed -i '{count}d' /etc/ppp/chap-secrets")
                except IndexError:
                    pass
            return output

    def create_user(self, user: dict) -> dict:
        """Add string from /etc/ppp/chap-secrets by request.

        Args:
            user (dict): dict based on User model

        Returns: dick based on User model
        """
        text = ''
        for word in user.values():
            text += f'{word} '
        os.system(f"echo '{text.strip()}' >> {self._CHAP_SECRETS_FILE}")
        return user


bash = Shell()