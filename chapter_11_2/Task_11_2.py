import time


def int_num(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) is float:
            return round(res)
        if type(res) in (list, tuple):
            return [round(x) if isinstance(x, float) else x for x in res]

    return inner


@int_num
def numeric():
    return [1, 7.6, 13.1, 5]


print(numeric())


def print_third(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
        raise Exception("Function call failed")

    return wrapper


@print_third
def sample_func():
    pass


def gen_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) in (tuple, list):
            for item in res:
                yield item
        else:
            yield res

    return wrapper


@gen_decorator
def get_numbers():
    return "[1, 2, 4, 5]"


for num in get_numbers():
    print(num)


def words_cutter(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) is str:
            return " ".join(el[:8] + "." if len(el) > 8 else el for el in res.split())
        else:
            return " ".join(el[:8] + "." if len(el) > 8 else el for el in res)

    return wrapper


@words_cutter
def get_words():
    return ["Hello", "this", "is", "a", "verylongword", "example"]


print(get_words())


def replace_exclamation_mark(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if "!" in res:
            return res.replace("!", "!!!")
        return res

    return wrapper


def replace_question_mark(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if "?" in res:
            return res.replace("?", "???")
        return res

    return wrapper


def replace_point(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if "." in res:
            return res.replace(".", "...")
        return res

    return wrapper


@replace_exclamation_mark
@replace_question_mark
@replace_point
def get_text():
    return "This is a sentence It has a question Does it need more exclamation"


print(get_text())
