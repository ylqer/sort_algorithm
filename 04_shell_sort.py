def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j-1] > alist[j]:
                    alist[j-1], alist[j] = alist[j], alist[j-1]
                j -= gap
        gap //= 2


if __name__ == '__main__':
    a = [1, 20, 0, 34, 3, 5, 6, 4]
    print(a)
    shell_sort(a)
    print(a)
