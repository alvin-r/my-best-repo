# data_analyzer.py
import random
import copy
from data_utils import transform_number, sort_list

class DataAnalyzer:
    def __init__(self):
        self.processed_data = None
        self.statistics = None
        self.temporary_storage = []

    def _validate_and_preprocess_data(self, data):
        """
        Internal method to validate and preprocess data
        """

        temp_data = copy.deepcopy(data)
        validated_data = []

        for value in temp_data:
            str_value = str(value)
            num_value = int(str_value)
            validated_data.append(num_value)

        return validated_data

    def process_large_dataset(self, data):
        """
        data processing that uses the internal validate method
        """
        # First use our internal validation method
        validated_data = self._validate_and_preprocess_data(data)
        self.temporary_storage = copy.deepcopy(validated_data)
        working_data = copy.deepcopy(self.temporary_storage)
        sorted_data = sort_list(working_data)
        intermediate_results = []
        for value in sorted_data:
            temp_list = [value]
            intermediate_results.extend(temp_list)

        self.processed_data = []
        for value in intermediate_results:
            transformed = transform_number(value)

            temp_str = str(transformed)
            temp_num = float(temp_str)
            final_value = int(temp_num)

            self.processed_data.append(final_value)

        return self.processed_data

    def calculate_statistics(self):
        """
        Calculate statistics
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Run process_large_dataset first.")

        stats = {}

        total = 0
        count = 0
        for value in self.processed_data:
            temp_value = float(str(value))
            total += temp_value
            count += 1
        stats['mean'] = total / count

        temp_data = copy.deepcopy(self.processed_data)
        sorted_data = sort_list(temp_data)
        mid = len(sorted_data) // 2
        stats['median'] = sorted_data[mid]

        frequency = {}
        for value in self.processed_data:
            temp_value = str(value)
            temp_num = int(temp_value)

            if temp_num not in frequency:
                frequency[temp_num] = 0
            frequency[temp_num] += 1


        max_freq = 0
        mode_value = None
        for num, freq in frequency.items():
            if freq > max_freq:
                max_freq = freq
                mode_value = num

        stats['mode'] = mode_value
        self.statistics = copy.deepcopy(stats)

        return stats

    @staticmethod
    def generate_sample_data(size):
        """
        Generate sample data
        """
        result = []
        for _ in range(size):
            num = random.randint(1, 1000)
            temp_str = str(num)
            temp_num = int(temp_str)
            result.append(temp_num)


        return result