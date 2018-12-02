import meta_class
from utils import wrap, print_class_must_have_base, generate_commands_add_base


def create_servant():
    print('You are creating a servant class for Servant pattern.')

    servant = meta_class.MetaClass()

    servant._add_class_name()

    class_name = servant.name

    base_classes = []
    commands = generate_commands_add_base(base_classes)
    wrap(servant._add_base_names, commands)
    print_class_must_have_base(class_name, base_classes, True)
    servant._add_base_names()

    servant._add_methods()

    return servant


def servant_generator():
    servant = create_servant()

    servant.write_class()


servant_generator()
