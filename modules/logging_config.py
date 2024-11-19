import logging
from colorlog import ColoredFormatter

def setup_logging():
    log_format = "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = ColoredFormatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler('../bot_logs.log')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set default logging level to DEBUG
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
import logging
from colorlog import ColoredFormatter

def setup_logging():
    log_format = "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = ColoredFormatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler('../bot_logs.log')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set default logging level to DEBUG
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
