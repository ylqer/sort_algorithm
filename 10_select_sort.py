def select_sort(alist):
    n = len(alist)
    for i in range(0, n-1):
        count = 0
        for j in range(i+1, n):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
        if count == 0:
            return


if __name__ == '__main__':
    a = [1, 4, 3, 2, 5, 6, 3, 6]
    print(a)
    select_sort(a)
    print(a)
