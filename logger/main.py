import package1
import app_logger

logger = app_logger.get_logger(__name__)


def main():
    logger.info("Start program")
    package1.process(msg="message")
    logger.warning("This is should got on console and file")
    logger.info("Finish program")


if __name__ == "__main__":
    main()
