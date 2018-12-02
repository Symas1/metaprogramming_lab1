import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_context():
    print('You are creating a context class for State pattern.')

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
    print('You are creating a base class for State in State pattern.')

    state = meta_class.MetaClass()

    state._add_class_name()
    class_name = state.name

    base_names = ['ABCMeta']
    commands = generate_commands_add_base(base_names)
    wrap(state._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    state._add_base_names()

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
    print('You are creating a concrete class for State in State pattern.')

    state = meta_class.MetaClass()

    state._add_class_name()
    class_name = state.name

    base_names = [base_state_name]
    commands = generate_commands_add_base(base_names)
    wrap(state._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    state._add_base_names()

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


def state_generator():
    context = create_context()
    base_state = create_base_state()

    concrete_states = []
    for i in range(int(input('Enter number of concrete State classes: '))):
        concrete_state = create_concrete_state(base_state.name)
        concrete_states.append(concrete_state)

    folder, file = context.write_class()
    base_state.write_class(folder, file)
    for concrete_state in concrete_states:
        concrete_state.write_class(folder, file)


state_generator()