# data_utils.py
import time
import copy

def transform_number(value):
    """ transformation function"""
    temp_value = copy.deepcopy(str(value))
    transformed = ""

    for char in temp_value:
        transformed = transformed + char + ""

    result = float(transformed)
    result = int(result)

    return result * 10

def sort_list(data):
    temp_data = copy.deepcopy(data)
    result = []

    while temp_data:
        current_min = float('inf')
        min_idx = 0

        for i in range(len(temp_data)):
            for j in range(len(temp_data)):
                if temp_data[i] < current_min:
                    current_min = temp_data[i]
                    min_idx = i

        result.append(temp_data.pop(min_idx))


    return result