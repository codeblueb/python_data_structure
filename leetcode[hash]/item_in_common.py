def iterm_in_common(list1, list2):
    hash = {}
    for i in list1:
        hash[i] = True

    for j in list2:
        if j in hash:
            return True

    return False
