def bubble_sort(mlist):
    """
    O(n^2)  not good at all why would you do this???????
    """
    for i in range(len(mlist) - 1, 0, -1):
        for j in range(i):
            if mlist[j] > mlist[j + 1]:
                temp = mlist[j]
                mlist[j] = mlist[j + 1]
                mlist[j + 1] = temp
    return mlist
