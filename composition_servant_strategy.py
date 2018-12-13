import strategy_generator
import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_servant(strategy_name):
    print('You are creating a servant class for the composition of Servant and Strategy.')

    servant = meta_class.MetaClass()

    servant._add_class_name()

    class_name = servant.name

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(servant._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    servant._add_base_names()

    curr_func = f'set_{strategy_name}'
    curr_params = [f'{strategy_name}_instance', 'new_strategy']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(servant._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    servant._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    servant._add_method_decorator(curr_func)

    curr_func = f'set_context_interface'
    curr_params = [f'{strategy_name}_instance', 'new_context_interface']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(servant._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    servant._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    servant._add_method_decorator(curr_func)

    servant._add_methods()

    return servant


def composition_servant_strategy_generator():
    folder, file, strategy_name = strategy_generator.strategy_generator()

    servant = create_servant(strategy_name)

    servant.write_class(folder, file)


composition_servant_strategy_generator()
