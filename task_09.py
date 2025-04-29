def connect_dicts(first, second):
    if first is None and second is None: return None
    elif len(first) == 0 and len(second) == 0: return None
    if sum(first.values()) > sum(second.values()):
        main = first
        additional = second
    else:
        main = second
        additional = first
    for key, value in additional.items():
        if key not in main and value >= 10:
            main[key] = value
    for key in list(main.keys()):
        if main[key] < 10: del main[key]
    return dict(sorted(main.items(), key=lambda item: item[1]))

assert connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) == { "c": 11, "b": 12 }
assert connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) == { "d": 11, "c": 12, "a": 13 }
assert connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) == { "c": 11, "b": 12, "a": 15 }