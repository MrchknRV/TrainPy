import app_logger
logger = app_logger.get_logger(__name__)


def process(msg):
    logger.info("After process")
    print(msg)
    logger.info("Late process")
