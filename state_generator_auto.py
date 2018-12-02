import string

import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_context():
    print('You are creating a context class for State pattern.')

    context = meta_class.MetaClass()

    class_name = 'Context'

    commands = [class_name]
    wrap(context._add_class_name, commands)

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(context._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, False)

    curr_func = '__init__'
    curr_params = ['state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'request'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return context


def create_base_state():
    print('You are creating a base class for State in State pattern.')

    state = meta_class.MetaClass()

    class_name = 'BaseState'

    commands = [class_name]
    wrap(state._add_class_name, commands)

    base_names = ['ABCMeta']
    commands = generate_commands_add_base(base_names)
    wrap(state._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    curr_func = 'handle'
    curr_params = []
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(state._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return state


def create_concrete_state(base_state_name, concrete_state_name):
    print('You are creating a concrete class for State in State pattern.')

    state = meta_class.MetaClass()

    class_name = concrete_state_name

    commands = [class_name]
    wrap(state._add_class_name, commands)

    base_names = [base_state_name]
    commands = generate_commands_add_base(base_names)
    wrap(state._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    curr_func = 'handle'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(state._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return state


def state_generator():
    context = create_context()
    base_state = create_base_state()
    concrete_states = []
    for i in string.ascii_uppercase[:5]:
        concrete_state = create_concrete_state(base_state.name, f'ConcreteState{i}')
        concrete_states.append(concrete_state)

    commands = ['state_pattern_auto', 'state']
    folder, file = wrap(context.write_class, commands)
    base_state.write_class(folder, file)
    for concrete_state in concrete_states:
        concrete_state.write_class(folder, file)


state_generator()
