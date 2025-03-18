from src.compute_and_sort import compute_and_sort
def test_compute_and_sort(benchmark):
    result = benchmark(compute_and_sort, list(reversed(range(5000))))
    assert result == 6247083.5
