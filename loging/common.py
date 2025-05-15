import logging


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%m:%s",
        format="[%(asctime)s.%(msecs)03d] %(module)12s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
