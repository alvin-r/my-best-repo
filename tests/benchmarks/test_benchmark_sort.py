from src.bubble_sort import sorter
def test_benchmark_sort(benchmark):
    benchmark(sorter, list(range(1000)))