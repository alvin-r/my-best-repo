# analytics.py
def calculate_statistics(data):
    """Calculate various statistics from the processed data"""
    stats = {}

    # Basic statistics
    stats['mean'] = sum(data) / len(data)

    # Median
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    stats['median'] = sorted_data[mid]

    # Mode
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    stats['mode'] = max(frequency.items(), key=lambda x: x[1])[0]

    return stats