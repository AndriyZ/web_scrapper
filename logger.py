'''
Module contains logging functionality
'''
import logging

import sys


def get_logger():
    '''
    Functions creates and return logger for application
    '''
    logger = logging.getLogger('web_scrapper')
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger

