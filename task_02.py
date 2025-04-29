def coincidence(source_list = None, rng = range(0, 0)):
    result = []
    if source_list is not None and len(source_list) != 0:
        for item in source_list:
            if item is None: continue
            if type(item) == int and item in rng: result.append(item)
            elif type(item) == float and round(item) in rng: result.append(item)
            elif type(item) == list: result.extend(coincidence(item, rng))
    return result

assert (coincidence([1, 2, 3, 4, 5], range(3, 6)) == [3, 4, 5])
assert (coincidence() == [])
assert (coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) == [1, 2, 2.5])
assert (coincidence([1, 4, 5, [2.5, 25, 2, 3]], range(3, 6)) == [4, 5, 3])
