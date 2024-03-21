def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


print(subarray_sum([1, 2, 3, 4], 9))

def subarray_sum2(nums: list[int], k:int) -> int:
    res = 0
    cur_sum = 0
    prefix_sums = {0:1}

    for n in nums:
        cur_sum += n
        diff = cur_sum - k
        res += prefix_sums.get(diff, 0)
        prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)
    return res

print(subarray_sum2([1, 2, 3, 4], 9))

