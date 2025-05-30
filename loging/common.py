import logging
import os


_log_format = "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"

PATH_LIB = os.path.abspath(r"..\TrainPy")
LOG_DIR = os.path.join(os.path.dirname(PATH_LIB), "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def get_file_handler():
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, 'app.log'), "w", encoding="UTF-8")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
