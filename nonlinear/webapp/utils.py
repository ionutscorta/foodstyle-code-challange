import logging


def init_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
