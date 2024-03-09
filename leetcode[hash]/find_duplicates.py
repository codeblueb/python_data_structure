def find_duplicates(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    dups = []
    for num, count in counts.items():
        if count > 1:
            dups.append(num)
    return dups
