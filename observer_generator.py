import meta_class
import os
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_subject():
    print('You are creating a Subject class for Observer pattern.')

    subject = meta_class.MetaClass()

    subject._add_class_name()
    class_name = subject.name

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(subject._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    subject._add_base_names()

    curr_func = '__init__'
    curr_params = ['observers', 'state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    subject._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    subject._add_method_decorator(curr_func)

    curr_func = 'attach'
    curr_params = ['observer']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    subject._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    subject._add_method_decorator(curr_func)

    curr_func = 'detach'
    curr_params = ['observer']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    subject._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    subject._add_method_decorator(curr_func)

    curr_func = '_notify'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    subject._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    subject._add_method_decorator(curr_func)

    curr_func = 'set_state'
    curr_params = ['new_state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    subject._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    subject._add_method_decorator(curr_func)

    curr_func = 'get_state'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    subject._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    subject._add_method_decorator(curr_func)

    return subject


def create_observer():
    print('You are creating a base class for Observer in Observer pattern.')

    observer = meta_class.MetaClass()

    observer._add_class_name()
    class_name = observer.name

    base_names = ['ABC']
    commands = generate_commands_add_base(base_names)
    wrap(observer._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    observer._add_base_names()

    curr_func = '__init__'
    curr_params = ['_subject', '_observer_state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(observer._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    observer._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    observer._add_method_decorator(curr_func)

    curr_func = 'update'
    curr_params = ['arg']
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(observer._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    observer._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    observer._add_method_decorator(curr_func)

    return observer


def create_concrete_observer(base_observer_name):
    print('You are creating a concrete class for Observer in Observer pattern.')

    observer = meta_class.MetaClass()

    observer._add_class_name()
    class_name = observer.name

    base_names = [base_observer_name]
    commands = generate_commands_add_base(base_names)
    wrap(observer._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    observer._add_base_names()

    curr_func = 'update'
    curr_params = ['arg']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(observer._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    observer._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    observer._add_method_decorator(curr_func)

    return observer


def observer_generator():
    subject = create_subject()
    base_observer = create_observer()
    concrete_observer = create_concrete_observer(base_observer.name)

    folder, file = subject.write_class()
    base_observer.write_class(folder, file)
    concrete_observer.write_class(folder, file)
    path = os.path.join(os.getcwd(), folder)
    with open(os.path.join(path, file + '.py'), 'r') as f:
        lines = f.readlines()
        lines.insert(0, 'from abc import ABC, abstractmethod\n')
    with open(os.path.join(path, file + '.py'), 'w') as f:
        f.writelines(lines)


observer_generator()
