# main.py
from data_analyzer import DataAnalyzer
import time
import copy

def main():
    # Initialize analyzer
    analyzer = DataAnalyzer()

    # Generate large dataset
    print("Generating sample data...")
    data = analyzer.generate_sample_data(1000)  # Reduced size due to inefficiency

    # Unnecessary copy of data
    data_copy = copy.deepcopy(data)

    # Process data
    print("Processing data...")
    start_time = time.time()
    processed_data = analyzer.process_large_dataset(data_copy)
    processing_time = time.time() - start_time
    print(f"Processing time: {processing_time:.2f} seconds")

    # Calculate statistics
    print("Calculating statistics...")
    start_time = time.time()
    stats = analyzer.calculate_statistics()
    stats_time = time.time() - start_time
    print(f"Statistics calculation time: {stats_time:.2f} seconds")

    # Unnecessary string operations for output
    stats_str = str(stats)
    final_stats = eval(stats_str)
    print("Final statistics:", final_stats)

if __name__ == "__main__":
    main()