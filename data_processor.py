# data_processor.py
def process_large_dataset(data):
    data = data.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    # Additional processing
    processed_data = []
    for value in data:
        processed_data.append(int(str(value) + "0"))

    return processed_data