import os
import pathlib

import numpy as np

import meta_method
import utils


class MetaClass():
    def __init__(self):
        self.name = ''

        self.base_names = []
        self.methods = []
        self.method_decorators = {}

    def _add_class_name(self):
        self.name = utils.input_identifier('Enter class\' name: ')

    def _add_base_names(self):
        if utils.is_continue('base classes'):
            while True:
                new_base_name = utils.input_identifier('Enter base class\' name: ')
                self.base_names.append(new_base_name)
                if utils.is_continue('another base class'):
                    continue
                break

    def _add_method(self):
        self._add_methods(once=True)

    def _add_args_to_method(self, method_name):
        names = [arg.name for arg in self.methods]
        if method_name in names:
            idx = names.index(method_name)
            self.methods[idx].add_arguments()
        else:
            print(f'There is no method with name {method_name}')

    def _add_methods(self, once=False):
        if utils.is_continue('methods'):
            while True:
                new_method = meta_method.MetaMethod()
                if new_method.name not in self.methods:
                    new_method = self._check_method(new_method)
                    self.methods.append(new_method)
                    self._add_method_decorator(new_method.name)
                else:
                    print(f'A method with name {new_method.name} already exists')
                if not once and utils.is_continue('another method'):
                    continue
                break

    def _add_method_decorator(self, method_name):
        self.method_decorators.setdefault(method_name, [])
        if utils.is_continue(f'decorator for method {method_name}'):
            while True:
                new_decorator = utils.input_identifier('Enter decorator\'s name: ')
                if new_decorator not in self.method_decorators[method_name]:
                    self.method_decorators[method_name].append(new_decorator)
                else:
                    print(f'Decorator with name {new_decorator} already exists')
                if utils.is_continue('another decorator'):
                    continue
                break

    def _check_method(self, method):
        def del_and_append_idx(arr, idx):
            save_name = arr[idx]
            del arr[idx]
            arr.append(save_name)
            return arr

        arguments = method.get_arguments()
        if 'self' in arguments:
            del arguments[arguments.index('self')]
        arguments.insert(0, 'self')

        idx = np.where([utils.starts_with_symbol(name, 1, '*') for name in arguments])[0]
        if len(idx) != 0:
            arguments = del_and_append_idx(arguments, idx[0])

        idx = np.where([utils.starts_with_symbol(name, 2, '*') for name in arguments])[0]
        if len(idx) != 0:
            arguments = del_and_append_idx(arguments, idx[0])

        method.set_arguments(arguments)

        return method

    def write_class(self, output_folder_name=None, output_file_name=None):
        def write_esc(file, symb, n_times):
            file.write(f'{symb}' * n_times)

        def write_args(file, args_list):
            args = ', '.join(str(arg) for arg in args_list)
            file.write(f'({args}):')
            write_esc(file, '\n', 1)

        def write_class_name(file):
            file.write(f'class {self.name}')
            write_args(file, self.base_names)

        def write_method_name(file, method):
            file.write(f"def {method.name}")
            write_args(file, method.get_arguments())

        def write_pass(file):
            file.write(f'pass')
            write_esc(file, '\n', 1)

        def write_init_helper(file, method):
            for arg in method.get_arguments():
                if arg == 'self':
                    continue

                strip_arg = arg.strip('*')

                write_esc(file, '\t', 2)
                file.write(f"self.{strip_arg} = {strip_arg}")
                write_esc(file, '\n', 1)

        def write_methods(file):
            for method in self.methods:
                write_decorators(file, method.name)

                write_esc(file, '\t', 1)
                write_method_name(file, method)

                if method.name == '__init__':
                    write_init_helper(file, method)

                write_esc(file, '\t', 2)
                write_pass(file)

        def write_decorators(file, method_name):
            for decorator_name in self.method_decorators[method_name][::-1]:
                write_esc(file, '\t', 1)
                file.write(f"@{decorator_name}")
                write_esc(file, '\n', 1)

        if output_folder_name is None:
            output_folder_name = input('Enter output folder name: ')
        if output_file_name is None:
            output_file_name = input('Enter output file name: ')

        path = os.path.join(os.getcwd(), output_folder_name)
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

        with open(os.path.join(path, output_file_name + '.py'), 'a+') as file:
            write_class_name(file)

            write_methods(file)

            write_esc(file, '\t', 1)
            write_pass(file)

        return output_folder_name, output_file_name
