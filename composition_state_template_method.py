import state_generator
import template_method_generator
import meta_class
import os
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_context():
    print('You are creating a context class for State in composition of State and Template Method.')

    context = meta_class.MetaClass()

    context._add_class_name()

    class_name = context.name

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(context._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    context._add_base_names()

    curr_func = '__init__'
    curr_params = ['state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    context._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    context._add_method_decorator(curr_func)

    curr_func = 'request'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    context._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    context._add_method_decorator(curr_func)

    context._add_methods()

    return context


def create_base_state():
    print('You are creating a base class for State in composition of State and Template Method.')

    state = meta_class.MetaClass()

    state._add_class_name()
    class_name = state.name

    base_names = ['ABC']
    commands = generate_commands_add_base(base_names)
    wrap(state._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    state._add_base_names()

    curr_func = '__init__'
    curr_params = ['template_method_instance']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(state._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    state._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    state._add_method_decorator(curr_func)

    curr_func = 'handle'
    curr_params = []
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(state._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    state._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    state._add_method_decorator(curr_func)

    state._add_methods()

    return state


def create_concrete_state(base_state_name):
    print('You are creating a concrete class for State in composition of State and Template Method.')

    state = meta_class.MetaClass()

    state._add_class_name()
    class_name = state.name

    base_names = [base_state_name]
    commands = generate_commands_add_base(base_names)
    wrap(state._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    state._add_base_names()

    curr_func = '__init__'
    curr_params = ['template_method_instance']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(state._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    state._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    state._add_method_decorator(curr_func)

    curr_func = 'handle'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(state._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    state._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    state._add_method_decorator(curr_func)

    state._add_methods()

    return state


def add_super(path_to_file, class_name):
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        selected_idx = [idx for idx, line in enumerate(lines) if f'class {class_name}' in line][0]
        for i in range(selected_idx, len(lines)):
            if 'def __init__' in lines[i]:
                selected_idx = i
                break
        lines.insert(selected_idx + 1, '\t\tsuper().__init__(template_method_instance)\n')
    with open(path_to_file, 'w') as f:
        f.writelines(lines)


def generate_comp_state_template_method():
    folder, file, n_classes = template_method_generator.template_method_generator()

    context = create_context()
    base_state = create_base_state()

    concrete_states = []
    for i in range(n_classes):
        concrete_state = create_concrete_state(base_state.name)
        concrete_states.append(concrete_state)

    context.write_class(folder, file)
    base_state.write_class(folder, file)
    for concrete_state in concrete_states:
        concrete_state.write_class(folder, file)

    for concrete_state in concrete_states:
        curr_name = concrete_state.name
        add_super(os.path.join(folder, f'{file}.py'), curr_name)


generate_comp_state_template_method()
