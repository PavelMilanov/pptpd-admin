import argparse
import toml
from typing import Optional, Literal


parser = argparse.ArgumentParser(description='Poetry converter')
parser.add_argument(
    '-p',
    dest='path',
    required=True,
    default='.',
    help='Path to create a requirements.txt'
)
parser.add_argument(
    '-f',
    dest='flag',
    default=None,
    help='None = dependencies, dev = dev-dependencies'
)

class TomlConverter:
    """Genarate requirements.txt from pyproject.toml file.
    
    USAGE: python converter.py [FLAG] [PARAMETER]
    
    Print python converter.py --help for more information.
    """

    def __init__(self, file: str, path: str, mode: Literal['dev', None]):
        """Class constructor."""
        self.__parse_flags(mode)
        self.dependencies = toml.load(file)['tool']['poetry'][self.__parse_flags(mode)]
        self.__generate_list_dependencies(path)

    def __generate_list_dependencies(self, path: str):
        """Generate list of modules fron dict, then create requirements.txt file."""
        modules = [f'{module}=={version[1:]}' for module, version in self.dependencies.items()]
        with open(f'{path}/requirements.txt', 'w') as file:
            for line in modules[1:]:
                file.write(f'{line}\n')
    
    def __parse_flags(self, flag: str | None) -> str:
        """Parse flags from CLI from generate requirements file."""
        return 'dependencies' if flag is None else 'dev-dependencies'


if __name__ == '__main__':
    args = parser.parse_args()
    converter = TomlConverter(file='pyproject.toml', path=args.path, mode=args.flag)
