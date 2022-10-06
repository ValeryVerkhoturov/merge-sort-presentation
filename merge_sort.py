from numbers import Number


def merge_sort(arr: list[Number]) \
        -> list[Number]:
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else [arr[1], arr[0]]
    mid = len(arr) // 2
    return merge([merge_sort(arr[:mid]), merge_sort(arr[mid:])])


def merge(arrays: list[list[Number]]) -> list[Number]:
    assert len(arrays) == 2
    x, y = arrays
    index_x = index_y = 0
    out = []
    while index_x < len(x) and \
            index_y < len(y):
        if x[index_x] < y[index_y]:
            out.append(x[index_x])
            index_x += 1
        else:
            out.append(y[index_y])
            index_y += 1
    out += x[index_x:] + y[index_y:]
    return out
