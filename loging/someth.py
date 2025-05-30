from functools import wraps
from common import get_logger

logger = get_logger(__name__)


def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Вызов функции %s", func.__name__)
        results = func(*args, **kwargs)
        logger.warning("Функция %s была вызвана с аргументами %s, %s", func.__name__, args, kwargs)
        logger.info("Функция %s завершена", func.__name__)
        logger.warning("Выход из функции %s", func.__name__)
        return results

    return wrapper


# Пример использования декоратора
@log_function
def example_function(x, y):
    return x + y


if __name__ == "__main__":
    # Вызов функции
    result = example_function(3, 4)
