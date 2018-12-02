import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_context():
    print('You are creating a context class for Strategy pattern.')

    context = meta_class.MetaClass()

    context._add_class_name()
    class_name = context.name

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(context._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    context._add_base_names()

    curr_func = '__init__'
    curr_params = ['strategy']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(context._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    context._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    context._add_method_decorator(curr_func)

    curr_func = 'context_interface'
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


def create_base_strategy():
    print('You are creating a base class for Strategy in Strategy pattern.')

    strategy = meta_class.MetaClass()

    strategy._add_class_name()
    class_name = strategy.name

    base_names = ['ABCMeta']
    commands = generate_commands_add_base(base_names)
    wrap(strategy._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    strategy._add_base_names()

    curr_func = 'algorithm_interface'
    curr_params = []
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(strategy._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    strategy._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    strategy._add_method_decorator(curr_func)

    strategy._add_methods()

    return strategy


def create_concrete_strategy(base_state_name):
    print('You are creating a concrete class for Strategy in Strategy pattern.')

    strategy = meta_class.MetaClass()

    strategy._add_class_name()
    class_name = strategy.name

    base_names = [base_state_name]
    commands = generate_commands_add_base(base_names)
    wrap(strategy._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, True)
    strategy._add_base_names()

    curr_func = 'algorithm_interface'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(strategy._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    strategy._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    strategy._add_method_decorator(curr_func)

    strategy._add_methods()

    return strategy


def state_generator():
    context = create_context()
    base_strategy = create_base_strategy()
    concrete_strategies = []
    for i in range(int(input('Enter number of concrete Strategy classes: '))):
        concrete_strategy = create_concrete_strategy(base_strategy.name)
        concrete_strategies.append(concrete_strategy)

    folder, file = context.write_class()
    base_strategy.write_class(folder, file)
    for concrete_strategy in concrete_strategies:
        concrete_strategy.write_class(folder, file)


state_generator()
