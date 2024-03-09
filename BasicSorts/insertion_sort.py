def insertion_sort(mlist):

    for i in range(1, len(mlist)):
        temp = mlist[i]
        j = i - 1
        while temp < mlist[j] and j > -1:
            mlist[j + 1] = mlist[j]
            mlist[j] = temp
            j -= 1
    return mlist
