def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1


if __name__ == '__main__':
    a = [1, 5, 3, 2, 5, 3, 0, 22, 34, 23, 88]
    print(a)
    insert_sort(a)
    print(a)
