def multiply_numbers(inputs = None):
    if inputs is None: return None
    elif type(inputs) == list:
        if len(inputs) == 0: return None
        else: inputs = ''.join(map(str, inputs))
    elif type(inputs) == int or type(inputs) == float: inputs = str(inputs)
    result = None
    for char in inputs:
        if char.isdigit():
            if result is None: result = int(char)
            else: result *= int(char)
    return result

assert multiply_numbers() is None
assert multiply_numbers('ss') is None
assert multiply_numbers('1234') == 24
assert multiply_numbers('sssdd34') == 12
assert multiply_numbers(2.3) == 6
assert multiply_numbers([5, 6, 4]) == 120
assert multiply_numbers([5, 6, 4, '1241345', 'sdfsdc2']) == 115200