import subprocess
import re


def check_os(func):  # noqa: D103
    def wrapped(*args):
        """Check os-release file."""
        SUPPORT_OS = ('ubuntu', 'debian')
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

    @staticmethod
    def read_chap_secrets_file() -> list:
        """Read chap-secrets file.

        Returns:
            list: lines of chap-secrets file.
        """
        with open('/etc/ppp/chap-secrets') as file:
            return file.readlines()
