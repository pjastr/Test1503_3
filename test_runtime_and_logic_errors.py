import os


def unused_variables():
    unused_one = 42
    unused_two = "hello"
    unused_three = [1, 2, 3]
    result = 10
    return result


def uses_undefined():
    return undefined_variable + 10


def duplicate_definitions():
    x = 1
    x = 2
    x = 3
    return x


def bare_except_handler():
    try:
        result = 1 / 0
    except:
        result = -1

    try:
        data = open("nonexistent.txt")
    except:
        data = None

    return result, data


def bad_escape_sequences():
    regex_pattern = "\d+\s+\w+"
    path = "C:\new_folder\test"
    message = "Hello\World"
    return regex_pattern, path, message


def fstring_issues():
    name = "Alice"
    age = 30

    greeting = f"Hello there"
    empty_f = f""
    another = f"no placeholders here either"

    proper = f"Hello {name}, age {age}"
    return greeting, empty_f, another, proper


def messy_function(l, O):
    I = 10
    unused = "never read"
    x = l + O
    if x == None:
        pass
    if type(x) == int:
        pass
    try:
        return x
    except:
        return None


CONSTANT = 100
CONSTANT = 200

result = os.getcwd()
