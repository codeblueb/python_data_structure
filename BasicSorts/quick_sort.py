def quick_sort_helper(mlist, left, right):
    if left < right:
        pivot_index = pivot(mlist, left, right)
        quick_sort_helper(mlist, left, pivot_index - 1)
        quick_sort_helper(mlist, pivot_index + 1, right)
    return mlist


def quick_sort(mlist):
    return quick_sort_helper(mlist, 0, len(mlist) - 1)
