def max_odd(source_list = None):
    max_odd_number = 0
    for item in source_list:
        if type(item) == float: item = round(item)
        if type(item) == int and item % 2 != 0 and item > max_odd_number: max_odd_number = item
        if type(item) == list:
            max_odd_number_temp = max_odd(item)
            if max_odd_number_temp > max_odd_number: max_odd_number = max_odd_number_temp
    return max_odd_number if max_odd_number != 0 else None

assert max_odd([1, 2, 3, 4, 4]) == 3
assert max_odd([21.0, 2, 3, 4, 4]) == 21
assert max_odd(['ololo', 2, 3, 4, [1, 2], None]) == 3
assert max_odd(['ololo', 'fufufu']) is None
assert max_odd([2, 2, 4]) is None