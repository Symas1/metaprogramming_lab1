import utils


class MetaMethod:
    def __init__(self):
        self.name = utils.input_identifier('Enter method\'s name: ')

        self.arguments = []
        self.add_arguments()

    def add_arguments(self):
        if utils.is_continue('arguments'):
            while True:
                name = utils.input_agrument('Enter argument\'s name: ')

                if name in self.arguments:
                    print(f'An argument with name: {name} already exists, '
                          f'please, try again')
                elif utils.starts_with_symbol(name, 1, '*') and any(
                        utils.starts_with_symbol(arg_name, 1, '*') for arg_name in self.arguments):
                    print(f'Can\'t have more than one argument with * at the beginning: {name}, '
                          f'please, try again')
                elif utils.starts_with_symbol(name, 2, '*') and any(
                        utils.starts_with_symbol(arg_name, 2, '*') for arg_name in self.arguments):
                    print(f'Can\'t have more than one argument with ** at the beginning: {name}, '
                          f'please, try again')
                else:
                    self.arguments.append(name)

                if utils.is_continue('another argument'):
                    continue
                break

    def get_arguments(self):
        return self.arguments

    def set_arguments(self, arguments):
        self.arguments = arguments
