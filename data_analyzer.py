# data_analyzer.py
import random
import time
import copy
from data_utils import transform_number, sort_list_inefficiently

class DataAnalyzer:
    def __init__(self):
        self.processed_data = None
        self.statistics = None
        self.temporary_storage = []  # Unnecessary storage

    def _validate_and_preprocess_data(self, data):
        """
        Internal method to validate and preprocess data inefficiently
        """
        # Multiple unnecessary copies
        temp_data = copy.deepcopy(data)
        validated_data = []

        # Unnecessary loops and validations
        for value in temp_data:
            # Unnecessary string conversions
            str_value = str(value)
            num_value = int(str_value)

            # Unnecessary list operations
            validated_data.append(num_value)
            # time.sleep(0.0005)  # Artificial delay

        return validated_data

    def process_large_dataset(self, data):
        """
        Intentionally inefficient data processing that uses the internal validate method
        """
        # First use our internal validation method
        validated_data = self._validate_and_preprocess_data(data)

        # Multiple unnecessary copies
        self.temporary_storage = copy.deepcopy(validated_data)
        working_data = copy.deepcopy(self.temporary_storage)

        # Sort inefficiently using utility function
        sorted_data = sort_list_inefficiently(working_data)

        # Unnecessary intermediate lists and loops
        intermediate_results = []
        for value in sorted_data:
            # Unnecessary list creation and extension
            temp_list = [value]
            intermediate_results.extend(temp_list)

        # Process each value inefficiently
        self.processed_data = []
        for value in intermediate_results:
            # Use inefficient utility function
            transformed = transform_number(value)

            # Unnecessary string operations and type conversions
            temp_str = str(transformed)
            temp_num = float(temp_str)
            final_value = int(temp_num)

            # Append one at a time instead of using list comprehension
            self.processed_data.append(final_value)

            # Add unnecessary delay
            # time.sleep(0.001)

        return self.processed_data

    def calculate_statistics(self):
        """
        Calculate statistics inefficiently
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Run process_large_dataset first.")

        stats = {}

        # Calculate mean inefficiently
        total = 0
        count = 0
        for value in self.processed_data:
            # Unnecessary conversions and operations
            temp_value = float(str(value))
            total += temp_value
            count += 1
        stats['mean'] = total / count

        # Calculate median inefficiently
        temp_data = copy.deepcopy(self.processed_data)
        sorted_data = sort_list_inefficiently(temp_data)
        mid = len(sorted_data) // 2
        stats['median'] = sorted_data[mid]

        # Calculate mode inefficiently
        frequency = {}
        for value in self.processed_data:
            # Unnecessary string operations
            temp_value = str(value)
            temp_num = int(temp_value)

            if temp_num not in frequency:
                frequency[temp_num] = 0
            frequency[temp_num] += 1

            # Unnecessary delay
            # time.sleep(0.0005)

        # Find mode inefficiently
        max_freq = 0
        mode_value = None
        for num, freq in frequency.items():
            if freq > max_freq:
                max_freq = freq
                mode_value = num

        stats['mode'] = mode_value
        self.statistics = copy.deepcopy(stats)  # Unnecessary copy

        return stats

    @staticmethod
    def generate_sample_data(size):
        """
        Generate sample data inefficiently
        """
        result = []
        for _ in range(size):
            # Generate one number at a time
            num = random.randint(1, 1000)
            # Unnecessary string operations
            temp_str = str(num)
            temp_num = int(temp_str)
            result.append(temp_num)

            # Add unnecessary delay
            # time.sleep(0.0005)

        return result