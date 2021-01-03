def bubble_sort(alist):
    n = len(alist)
    for i in range(0, n-1):
        count = 0
        for j in range(0, n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    a = [1, 5, 6, 3, 2, 7, 4, 3, 66, 44, 23]
    print(a)
    bubble_sort(a)
    print(a)
