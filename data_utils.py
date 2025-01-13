# data_utils.py
import time
import copy

def transform_number(value):
    """Intentionally inefficient number transformation function"""
    # Create unnecessary copies and string operations
    temp_value = copy.deepcopy(str(value))
    transformed = ""

    # Unnecessary loop and string concatenation
    for char in temp_value:
        transformed = transformed + char + ""

    # Fix the conversion issue while keeping it inefficient
    result = float(transformed)
    result = int(result)  # Convert float to int safely

    # Add artificial delay
    # time.sleep(0.001)

    return result * 10

def sort_list_inefficiently(data):
    """Extremely inefficient sorting implementation"""
    # Make multiple unnecessary copies
    temp_data = copy.deepcopy(data)
    result = []

    while temp_data:
        # Find min value with unnecessary iterations
        current_min = float('inf')
        min_idx = 0

        # Unnecessary nested loops
        for i in range(len(temp_data)):
            for j in range(len(temp_data)):
                if temp_data[i] < current_min:
                    current_min = temp_data[i]
                    min_idx = i

        # Remove and append one at a time
        result.append(temp_data.pop(min_idx))

        # Unnecessary sleep
        # time.sleep(0.0005)

    return result