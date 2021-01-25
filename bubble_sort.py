def b_sort(l):
    length = len(l) - 1
    for i in range(length):
        for j in range(length - i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
