def selection_sort(mlist):

    for i in range(len(mlist) - 1):
        min_index = i

        for j in range(i + 1, len(mlist)):
            if mlist[j] < mlist[min_index]:
                min_index = j
        if i != min_index:
            temp = mlist[i]
            mlist[i] = mlist[min_index]
            mlist[min_index] = temp
    return mlist
