# data_utils.py
import time
import copy

def transform_number(value):
    """ transformation function"""
    # Since we receive integers, directly multiply without conversion
    return value * 10

def sort_list(data):
    # Modify to use Python's efficient built-in sort
    return sorted(data)