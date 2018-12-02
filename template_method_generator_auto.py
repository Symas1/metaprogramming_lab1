import string

import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_template(n_steps=2):
    print('You are creating a Template class for Template method pattern.')

    template = meta_class.MetaClass()

    class_name = 'TemplateMethod'

    commands = [class_name]
    wrap(template._add_class_name, commands)

    base_classes = ['ABCMeta']
    commands = generate_commands_add_base(base_classes)
    wrap(template._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, False)

    curr_func = 'template_method'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(template._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    for i in range(n_steps):
        curr_func = f'_primitive_operation_{i}'
        curr_params = []
        curr_decors = ['abstractmethod']
        commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
        wrap(template._add_method, commands)
        print_class_must_have_func(class_name, curr_func, curr_params, False)
        print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return template


def create_concrete_class(base_name, name,n_steps=2):
    print('You are creating a concrete class for Template method pattern.')

    concrete = meta_class.MetaClass()

    class_name = name

    commands = [class_name]
    wrap(concrete._add_class_name, commands)

    base_names = [base_name]
    commands = generate_commands_add_base(base_names)
    wrap(concrete._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    for i in range(n_steps):
        curr_func = f'_primitive_operation_{i}'
        curr_params = []
        curr_decors = []
        commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
        wrap(concrete._add_method, commands)
        print_class_must_have_func(class_name, curr_func, curr_params, False)
        print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return concrete


def template_method_generator():
    n_steps = 2
    template = create_template(n_steps)
    concrete_classes = []
    for i in range(2):
        concrete_class = create_concrete_class(template.name, f'ConcreteClass{i}',n_steps)
        concrete_classes.append(concrete_class)

    commands = ['template_method_pattern_auto', 'template_method']
    folder, file = wrap(template.write_class, commands)
    for concrete_class in concrete_classes:
        concrete_class.write_class(folder, file)


template_method_generator()
