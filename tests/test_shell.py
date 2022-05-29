from pptpd_admin.schemas.shell import SUPPORT_OS
import re
import pytest


def check_os_not_subprocess(systemname: str):
    ## systemname = ID=debian, ID=ubuntu,
    os_name = re.search('ID=[a-z]+', systemname)[0][3:]  # os_name[0]>ID=ubuntu
    if os_name in SUPPORT_OS:
        return 'Ok'
    else:
        raise ImportWarning('Your operating system not supported')
    
def check_chap_secrets_file_not_subprocess(status_code: int):
        if status_code == 0:
            return 'Ok'
        else:
            raise FileNotFoundError('pptpd package not installed') 

def test_check_os_not_subprocess():
    assert check_os_not_subprocess('ID=debian') == 'Ok'
    assert check_os_not_subprocess('ID=ubuntu') == 'Ok'
    with pytest.raises(ImportWarning):
        check_os_not_subprocess('ID=centos')
        
def test_check_chap_secrets_file_not_subprocess():
    assert check_chap_secrets_file_not_subprocess(0) == 'Ok'
    with pytest.raises(FileNotFoundError):
        check_chap_secrets_file_not_subprocess(1)
    