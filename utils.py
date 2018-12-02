import re
import sys
from io import StringIO
from keyword import iskeyword

import constants


def input_identifier(prompt):
    while True:
        name = input(prompt)
        if not is_correct_name(name):
            print(f'{name} - is an incorrect name, please, try again')
            continue
        break
    return name


def input_agrument(prompt):
    while True:
        name = input(prompt)

        cut_name = name
        if cut_name.startswith('**'):
            cut_name = cut_name[2:]
        elif cut_name.startswith('*'):
            cut_name = cut_name[1:]

        if not is_correct_name(cut_name):
            print(f'{name} - is an incorrect name, please, try again')
            continue
        break
    return name


def is_correct_name(name):
    return name.isidentifier() and not iskeyword(name)


def is_continue(text):
    return input(f'Do you want to add {text}?\n'
                 f'{constants.continue_key} - add\n'
                 f'Other button - leave: ') == constants.continue_key


def starts_with_symbol(text, times, symbol='*'):
    pattern = r'^(' + rf'\{symbol}' * times + r')' + rf'[^\{symbol}]'
    return bool(re.match(pattern, text))


def wrap(callable_, commands):
    f1 = sys.stdin
    with StringIO('\n'.join(commands)) as f:
        sys.stdin = f
        value = callable_()
    sys.stdin = f1
    return value


def print_class_must_have_func(class_name, method_name, params, other_params=True):
    print(f"Class - {class_name} must have a function - {method_name} with ", end='')
    if len(params) == 0:
        print('no default parameters. ', end='')
    elif len(params) == 1:
        print(f"default parameter: {', '.join(params)}. ", end='')
    else:
        print(f"default parameters: {', '.join(params)}. ", end='')

    if other_params:
        print('Would you like to add other parameters?')
    else:
        print()


def print_class_must_have_decors(class_name, method_name, decors, other_decors=True):
    print(f"Class - {class_name} must have a function - {method_name} with ", end='')
    if len(decors) == 0:
        print('no default decorators. ', end='')
    elif len(decors) == 1:
        print(f"default decorator: {', '.join(decors)}. ", end='')
    else:
        print(f"default decorators: {', '.join(decors)}. ", end='')

    if other_decors:
        print('Would you like to add other decorators?')
    else:
        print()


def print_class_must_have_base(class_name, base_classes, other_base=True):
    print(f"Class - {class_name} must have ", end='')
    if len(base_classes) == 0:
        print('no base classes. ', end='')
    elif len(base_classes) == 1:
        print(f"base class: {', '.join(base_classes)}. ", end='')
    else:
        print(f"base classes: {', '.join(base_classes)}. ", end='')

    if other_base:
        print('Would you like to add other base classes?')
    else:
        print()


def generate_commands_add_func(method_name, params, decorators):
    commands = [f'{constants.continue_key}']
    commands.append(str(method_name))

    for idx in range(len(params)):
        commands.append(f'{constants.continue_key}')
        commands.append(params[idx])

    commands.append('2')

    for idx in range(len(decorators)):
        commands.append(f'{constants.continue_key}')
        commands.append(decorators[idx])

    commands.append('2')

    return commands


def generate_commands_add_base(base_names):
    if len(base_names) == 0:
        return ['2']

    commands = [f'{constants.continue_key}']

    for idx in range(len(base_names)):
        commands.append(base_names[idx])
        if idx + 1 != len(base_names):
            commands.append(f'{constants.continue_key}')

    commands.append('2')

    return commands
