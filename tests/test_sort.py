from bubble_sort import sorter
def test_basic_sort():
    input_array = [64, 34, 25, 12, 22]
    expected = [12, 22, 25, 34, 64]
    assert sorter(input_array) == expected