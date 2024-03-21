class Hashmap:
    def __init__(self, size:int = 7) -> None:
        self.hashmap = [None] * size

    def hash_table(self) -> None:
        if all(ele for ele in self.hashmap if ele is not None):
            for t in self.hashmap:
                if t is not None:
                    print(t)
        else: print("Hash table has no data")

    def __hash(self, key:str) -> int:
        hash = 0
        for letter in key:
            hash = (hash * ord(letter)) % len(self.hashmap)
        return hash

    def set_item(self, key:str, value) -> None:
        index = self.__hash(key)
        if self.hashmap[index] == None:
            self.hashmap[index] = []
        self.hashmap[index].append( (key, value) )

    def get_item(self, key:str) -> list|None:
        index = self.__hash(key)
        if self.hashmap[index] is not None:
            for i in range(len(self.hashmap[index])):
                if self.hashmap[index][i][0] == key:
                    return self.hashmap[index][i][1]
        return None

    def keys(self) -> list[str]:
        keys = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i] is not None:
                for j in range(len(self.hashmap[i])):
                    keys.append(self.hashmap[i][j][0])
        return keys

    def find_duplicates(self, iter:list) -> list:
        count = {}
        for ele in iter:
            count[ele] = count.get(ele, 0) + 1
        dup = []
        for ele, count in count.items():
            if count > 1:
                dup.append(ele)
        return dup

    def first_non_repeating_characters(self, string:str) -> str|None:
        chars_count = {}
        for char in string:
            chars_count[char] = chars_count.get(char, 0) + 1
        for char in string:
            if chars_count[char] == 1:
                return char
        return None

    def group_anagrams(self, strings:list[str]) -> list[str]:
        anagrams = {}
        for string in strings:
            canonical = "".join(sorted(string))
            if canonical in anagrams:
                anagrams[canonical].append(string)
            else:
                anagrams[canonical] = [string]
        return list(anagrams.values())
    
    def found_items_in_common(self, list1:list, list2:list) -> bool:
        hash = {}
        for i in list1:
            hash[i] = True

        for i in list2:
            if i in hash:
                return True
        return False

    def get_common_items(self, list1:list, list2:list) -> list:
        count = {}
        for ele in list1:
            count[ele] = count.get(ele, 0) + 1
        items = []
        for ele in list2:
            if ele in count:
                items.append(ele)
        return items
    
    def subarray_sum(self, nums:list[int], target:int) -> int:
        sum_index = {0:1}
        current_sum = 0
        count = 0
        for n in nums:
            current_sum += n
            if current_sum - target in sum_index:
                count += sum_index[current_sum-target]
            sum_index[current_sum] = sum_index.get(current_sum, 0) + 1
        return count 

    def two_sums(self, nums:list[int], target:int) -> int:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

mds = Hashmap()

mds.set_item('add', [1, 2, 3])
mds.set_item('delete', [3, 6, 7])
mds.set_item('push', [1, 1, 2, 3, 4, 4])
mds.set_item('chars', ['a', 'b', 'c', 'a'])
mds.set_item('anagrams', ["eat", "tea", "tan", "ate", "nat", "bat"])
mds.hash_table()
print(mds.get_item('add'))
print(mds.keys())

print(mds.find_duplicates( mds.get_item('push') ))

print(mds.find_duplicates( mds.get_item('add') ))

print(mds.first_non_repeating_characters("takeit"))

print(mds.first_non_repeating_characters(''.join(mds.get_item('chars'))))

print(mds.group_anagrams(mds.get_item('anagrams')))

if mds.found_items_in_common(mds.get_item('add'), mds.get_item('push')):
    print("True, found common items")
    print(mds.get_common_items(mds.get_item('add'), mds.get_item('push')))
else:
    print("No items found in common")

print(mds.subarray_sum(mds.get_item('push'), 5))

print(mds.two_sums(mds.get_item('push'), 5))
