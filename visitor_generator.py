import meta_class
from utils import wrap, print_class_must_have_func, generate_commands_add_func, print_class_must_have_decors, \
    print_class_must_have_base, generate_commands_add_base


def create_base_element():
    print('You are creating a base element class for Visitor pattern.')

    base_element = meta_class.MetaClass()

    base_element._add_class_name()

    class_name = base_element.name

    base_classes = ['ABCMeta']
    commands = generate_commands_add_base(base_classes)
    wrap(base_element._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    base_element._add_base_names()

    curr_func = 'accept'
    curr_params = ['visitor']
    curr_decors = ['abstractmethod']
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(base_element._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    base_element._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    base_element._add_method_decorator(curr_func)

    base_element._add_methods()

    return base_element

def create_concrete_element(base_element_name):
    print('You are creating a concrete element class for Visitor pattern.')

    concrete_element = meta_class.MetaClass()

    concrete_element._add_class_name()

    class_name = concrete_element.name

    base_classes = [base_element_name]
    commands = generate_commands_add_base(base_classes)
    wrap(concrete_element._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    concrete_element._add_base_names()

    curr_func = 'accept'
    curr_params = ['visitor']
    curr_decors = []
    commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
    wrap(concrete_element._add_method, commands)
    print_class_must_have_func(class_name, curr_func, curr_params, True)
    concrete_element._add_args_to_method(curr_func)
    print_class_must_have_decors(class_name, curr_func, curr_decors, True)
    concrete_element._add_method_decorator(curr_func)

    concrete_element._add_methods()

    return concrete_element

def create_base_visitor():
    print('You are creating a base visitor class for Visitor pattern.')

    base_visitor = meta_class.MetaClass()

    base_visitor._add_class_name()

    class_name = base_visitor.name

    base_classes = ['ABCMeta']
    commands = generate_commands_add_base(base_classes)
    wrap(base_visitor._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    base_visitor._add_base_names()

    n_visit_func = int(input('How many visitor functions do you want: '))
    for i in range(n_visit_func):
        curr_func = f'visit_concrete_element_{i}'
        curr_params = [f'concrete_element_{i}']
        curr_decors = ['abstractmethod']
        commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
        wrap(base_visitor._add_method, commands)
        print_class_must_have_func(class_name, curr_func, curr_params, True)
        base_visitor._add_args_to_method(curr_func)
        print_class_must_have_decors(class_name, curr_func, curr_decors, True)
        base_visitor._add_method_decorator(curr_func)

    base_visitor._add_methods()

    return base_visitor, n_visit_func

def create_concrete_visitor(base_visitor_name, n_visit_func):
    print('You are creating a concrete visitor class for Visitor pattern.')

    concrete_visitor = meta_class.MetaClass()

    concrete_visitor._add_class_name()

    class_name = concrete_visitor.name

    base_classes = [base_visitor_name]
    commands = generate_commands_add_base(base_classes)
    wrap(concrete_visitor._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    concrete_visitor._add_base_names()

    for i in range(n_visit_func):
        curr_func = f'visit_concrete_element_{i}'
        curr_params = [f'concrete_element_{i}']
        curr_decors = []
        commands = generate_commands_add_func(curr_func, curr_params, curr_decors)
        wrap(concrete_visitor._add_method, commands)
        print_class_must_have_func(class_name, curr_func, curr_params, True)
        concrete_visitor._add_args_to_method(curr_func)
        print_class_must_have_decors(class_name, curr_func, curr_decors, True)
        concrete_visitor._add_method_decorator(curr_func)

    concrete_visitor._add_methods()

    return concrete_visitor


def visitor_generator():
    base_element = create_base_element()
    concrete_elements = []
    for i in range(int(input('How many concrete elements do you want: '))):
        concrete_element = create_concrete_element(base_element.name)
        concrete_elements.append(concrete_element)

    base_visitor, n_funcs = create_base_visitor()
    concrete_visitors = []
    for i in range(int(input('How many concrete visitors do you want: '))):
        concrete_visitor = create_concrete_visitor(base_visitor.name,n_funcs)
        concrete_visitors.append(concrete_visitor)

    folder, file = base_element.write_class()
    for concrete_element in concrete_elements:
        concrete_element.write_class(folder, file)
    base_visitor.write_class(folder,file)
    for concrete_visitor in concrete_visitors:
        concrete_visitor.write_class(folder,file)

visitor_generator()
