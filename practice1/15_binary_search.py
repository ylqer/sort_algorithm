def binary_search(a: list, item: int):
    """递归"""
    n = len(a)
    if n > 0:
        mid = n // 2
        if a[mid] == item:
            return True
        elif item > a[mid]:
            return binary_search(a[mid+1:], item)
        else:
            return binary_search(a[:mid], item)
    return False


def binary_search_2(alist: list, item: int):
    """非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item > alist[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return False


if __name__ == '__main__':
    li = [3, 4, 5, 23, 45, 345, 990]
    print(binary_search(li, 5))
    print(binary_search_2(li, 13))
