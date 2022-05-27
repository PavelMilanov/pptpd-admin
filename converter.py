import toml


class TomlConverter:
    """Convert *.toml file to requirements.txt file."""

    def __init__(self, filename):
        """Class constructor."""

        self.dependencies = toml.load(filename)['tool']['poetry']['dependencies']
        self.__generate_list_dependencies()

    def __generate_list_dependencies(self):
        """Generate list of modules fron dict, then create requirements.txt file."""

        modules = [f'{module}=={version[1:]}' for module, version in self.dependencies.items()]
        with open('pptpd_admin/requirements.txt', 'w') as file:
            for line in modules[1:]:
                file.write(f'{line}\n')


if __name__ == '__main__':
    converter = TomlConverter('pyproject.toml')
