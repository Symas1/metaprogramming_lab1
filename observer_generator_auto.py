import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_subject():
    print('You are creating a Subject class for Observer pattern.')

    subject = meta_class.MetaClass()

    class_name = 'Subject'

    commands = [class_name]
    wrap(subject._add_class_name, commands)

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(subject._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, False)

    curr_func = '__init__'
    curr_params = ['observers', 'state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'attach'
    curr_params = ['observer']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'detach'
    curr_params = ['observer']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = '_notify'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'set_state'
    curr_params = ['new_state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'get_state'
    curr_params = []
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(subject._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return subject


def create_observer():
    print('You are creating a base class for Observer in Observer pattern.')

    observer = meta_class.MetaClass()

    class_name = 'BaseObserver'

    commands = [class_name]
    wrap(observer._add_class_name, commands)

    base_names = ['ABCMeta']
    commands = generate_commands_add_base(base_names)
    wrap(observer._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    curr_func = '__init__'
    curr_params = ['_subject', '_observer_state']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(observer._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    curr_func = 'update'
    curr_params = ['arg']
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(observer._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return observer


def create_concrete_observer(base_observer_name):
    print('You are creating a concrete class for Observer in Observer pattern.')

    observer = meta_class.MetaClass()

    class_name = 'ConcreteObserver'

    commands = [class_name]
    wrap(observer._add_class_name, commands)

    base_names = [base_observer_name]
    commands = generate_commands_add_base(base_names)
    wrap(observer._add_base_names, commands)
    print_class_must_have_base(class_name, base_names, False)

    curr_func = 'update'
    curr_params = ['arg']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(observer._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, False)
    print_class_must_have_decors(class_name, curr_func, curr_decors, False)

    return observer


def observer_generator():
    subject = create_subject()
    base_observer = create_observer()
    concrete_observer = create_concrete_observer(base_observer.name)

    commands = ['observer_pattern_auto', 'observer']
    folder, file = wrap(subject.write_class, commands)
    base_observer.write_class(folder, file)
    concrete_observer.write_class(folder, file)


observer_generator()
