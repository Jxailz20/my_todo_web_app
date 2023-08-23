FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    :param filepath: default file path is todos.txt
    :return: Returns list of todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    :param todos_arg: list of todos from get_todos()
    :param filepath: default file path is todos.txt
    :return: does not return value as it only performs write operation to file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)