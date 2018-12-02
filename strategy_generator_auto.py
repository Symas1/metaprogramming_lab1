import string

import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_context():
    print('You are creating a context class for Strategy pattern.')

    context = meta_class.MetaClass()

    class_name = 'Context'

    commands = [class_name]
    wrap(context._add_class_name, commands)

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(context._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, False)

    curr_func = '__init__'
    curr_params = ['strategy']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'context_interface'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return context


def create_base_strategy():
    print('You are creating a base class for Strategy in Strategy pattern.')

    strategy = meta_class.MetaClass()

    class_name = 'BaseStrategy'

    commands = [class_name]
    wrap(strategy._add_class_name, commands)

    base_names = ['ABCMeta']
    commands = generate_commands_add_base(base_names)
    wrap(strategy._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    curr_func = 'algorithm_interface'
    curr_params = []
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(strategy._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return strategy


def create_concrete_strategy(base_state_name, concrete_state_name):
    print('You are creating a concrete class for Strategy in Strategy pattern.')

    strategy = meta_class.MetaClass()

    class_name = concrete_state_name

    commands = [class_name]
    wrap(strategy._add_class_name, commands)

    base_names = [base_state_name]
    commands = generate_commands_add_base(base_names)
    wrap(strategy._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    curr_func = 'algorithm_interface'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(strategy._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return strategy


def state_generator():
    context = create_context()
    base_strategy = create_base_strategy()
    concrete_strategies = []
    for i in string.ascii_uppercase[:5]:
        concrete_strategy = create_concrete_strategy(base_strategy.name, f'ConcreteStrategy{i}')
        concrete_strategies.append(concrete_strategy)

    commands = ['strategy_pattern_auto', 'strategy']
    folder, file = wrap(context.write_class, commands)
    base_strategy.write_class(folder, file)
    for concrete_strategy in concrete_strategies:
        concrete_strategy.write_class(folder, file)


state_generator()
