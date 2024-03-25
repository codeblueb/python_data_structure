
def summary_ranges(nums:list[int]) -> list[str]:
    """
        The idea is to iterate through the list
        and numbers will be ordered and you have to 
        get the range of a, b when b is not a. 
        so technically you are just told to get the range of 
        integers if end is not == next iteration
    """
    if len(nums) == 0: return []
    
    def format(start:int, end:int) -> None:
        if start == end:
            return str(start)
        else:
            return f"{start}->{end}"

    result = []
    start = end = nums[0]
    for num in nums[1:]: # O(N)
        if num == end + 1:
            end = num
        else:
            result.append(format(start, end))
            start = end = num

    result.append(format(start, end))
    return result

print(summary_ranges([0,1,2,4,5,7]))
print(summary_ranges([0,2,3,4,6,8,9]))


