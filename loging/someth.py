import logging
from functools import wraps
from loging.common import configure_logging

# Настраиваем базовый логер
# logging.basicConfig(
#     format="[%(asctime)s.%(msecs)03d] %(name)s:%(module)-12s:%(lineno)-3d %(levelname)-7s - %(message)s"
# )
logger = logging.getLogger("function_logger")
# logger.setLevel(logging.DEBUG)


# Декоратор для логирования
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        configure_logging(level=logging.INFO)
        logger.info(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Функция {func.__name__} завершена")
        return result

    return wrapper


# Пример использования декоратора
@log_function
def example_function(x, y):
    return x + y


if __name__ == "__main__":
    # Вызов функции
    result = example_function(3, 4)
