#! /usr/bin/env python3

import logging
import logging.handlers

# logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

logger = logging.getLogger("MyLogger")

his_logger = logging.getLogger("HisLogger")

str_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="./test.log")
# file_rotate_handler = logging.handlers.RotatingFileHandler("test.log", mode="w", maxBytes=1000, backupCount=3, encoding="utf-8")
# time_rotate_handler = logging.handlers.TimedRotatingFileHandler("test.log", when="H", interval=1, backupCount=10)

logger.setLevel(logging.NOTSET)
his_logger.setLevel(logging.NOTSET)

str_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)


str_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

str_handler.setFormatter(str_formatter)
file_handler.setFormatter(file_format)

logger.addHandler(str_handler)
logger.addHandler(file_handler)
his_logger.addHandler(str_handler)

logger.debug('This is a customer debug message')
logger.info('This is an customer info message')
logger.warning('This is a customer warning message')
logger.error('This is an customer error message')
logger.critical('This is a customer critical message')

his_logger.debug('This is a customer debug message')
his_logger.info('This is an customer info message')
his_logger.warning('This is a customer warning message')
his_logger.error('This is an customer error message')
his_logger.critical('This is a customer critical message')