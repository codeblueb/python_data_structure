def two_sums(num, target):
    num_map = {}
    for i, num in enumerate(num):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
