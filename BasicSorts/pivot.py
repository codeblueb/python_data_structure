def swap(mlist, index1, index2):
    temp = mlist[index1]
    mlist[index1] = mlist[index2]
    mlist[index2] = temp


def pivot(mlist, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if mlist[i] < mlist[pivot_index]:
            swap_index += 1
            swap(mlist, swap_index, i)
    swap(mlist, pivot_index, swap_index)
    return swap_index
