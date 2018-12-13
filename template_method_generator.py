import meta_class
import os
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_template():
    print('You are creating a Template class for Template method pattern.')

    template = meta_class.MetaClass()

    template._add_class_name()
    class_name = template.name

    base_classes = ['ABC']
    commands = generate_commands_add_base(base_classes)
    wrap(template._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    template._add_base_names()

    curr_func = 'template_method'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(template._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    template._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    template._add_method_decorator(curr_func)

    n_steps = int(input('How many algorithm steps do you want: '))
    for i in range(n_steps):
        curr_func = f'_primitive_operation_{i}'
        curr_params = []
        curr_decors = ['abstractmethod']
        commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
        wrap(template._add_method, commands)
        print_class_must_have_func(class_name, curr_func, curr_params, True)
        template._add_args_to_method(curr_func)
        print_class_must_have_decors(class_name, curr_func, curr_decors, True)
        template._add_method_decorator(curr_func)

    template._add_methods()

    return template, n_steps


def create_concrete_class(base_name, n_steps):
    print('You are creating a concrete class for Template method pattern.')

    concrete = meta_class.MetaClass()

    concrete._add_class_name()
    class_name = concrete.name

    base_names = [base_name]
    commands = generate_commands_add_base(base_names)
    wrap(concrete._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    concrete._add_base_names()

    for i in range(n_steps):
        curr_func = f'_primitive_operation_{i}'
        curr_params = []
        curr_decors = []
        commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
        wrap(concrete._add_method, commands)
        print_class_must_have_func(class_name, curr_func, curr_params, True)
        concrete._add_args_to_method(curr_func)
        print_class_must_have_decors(class_name, curr_func, curr_decors, True)
        concrete._add_method_decorator(curr_func)

    concrete._add_methods()

    return concrete


def template_method_generator():
    template, n_steps = create_template()
    concrete_classes = []

    n_classes = int(input('How many concrete classes do you want: '))
    for i in range(n_classes):
        concrete_class = create_concrete_class(template.name, n_steps)
        concrete_classes.append(concrete_class)

    folder, file = template.write_class()
    for concrete_class in concrete_classes:
        concrete_class.write_class(folder, file)
    path = os.path.join(os.getcwd(), folder)
    with open(os.path.join(path, file + '.py'), 'r') as f:
        lines = f.readlines()
        lines.insert(0, 'from abc import ABC, abstractmethod\n')
    with open(os.path.join(path, file + '.py'), 'w') as f:
        f.writelines(lines)
    return folder, file, n_classes


if __name__ == '__main__':
    template_method_generator()
