def quick_sort(alist, first, last):
    if first >= last:
        return
    middle_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= middle_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] <= middle_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = middle_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    # a = [1, 0, 2, 5, 3, 4, 23, 44, 32, 50]
    a = [3, 5, 54, 34, 66, 45, 3, 6, 5, 0]
    print(a)
    quick_sort(a, 0, len(a)-1)
    print(a)
