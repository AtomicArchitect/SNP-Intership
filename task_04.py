def sort_list(source_list):
    if source_list is not None and len(source_list) > 0:
        min_item = source_list[0]
        if len(source_list) > 1:
            min_item, max_item = min_max(source_list)
            for idx, item in enumerate(source_list):
                if item == min_item:
                    source_list[idx] = max_item
                elif item == max_item:
                    source_list[idx] = min_item
        source_list.append(min_item)
    return source_list

def min_max(source_list):
    min_item, max_item = source_list[0], source_list[-1]
    for item in source_list:
        if item < min_item: min_item = item
        elif item > max_item: max_item = item
    return min_item, max_item

assert sort_list([]) == []
assert sort_list([2, 4, 6, 8]) == [8, 4, 6, 2, 2]
assert sort_list([1]) == [1, 1]
assert sort_list([1, 2, 1, 3]) == [3, 2, 3, 1, 1]
assert sort_list([1, 2, 1, 3, 5, 6, 7, 24, 300, 13143124, 1]) == [13143124, 2, 13143124, 3, 5, 6, 7, 24, 300, 1, 13143124, 1]