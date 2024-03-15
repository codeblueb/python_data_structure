class Hashmap:
    def __init_-(self, size:int = 7) -> None:
        self.hashmap = [None] * size


    def print_hash_table(self) -> None:
        if len(self.hashmap) == 0:
            print(f"Empty Table")
            return None
    
    def set_item(self, key:str, value) -> None:
        """
            Compute the table in the hash table based on the key using the __hash method
        """
        index = self.__hash(key)

        # if the bucket at the index is empty, initialize it to an empty list
        if self.hashmap[index] == None:
            self.hashmap[index] = []

        # Append the [key, value] pair to the bucket at the index
        self.hashmap[index].append([key, value])
    
    def get_item(self, key):

        index = self.__hash(key)  # get the index of the key in the hash table

        #check if there is any value stored in the index of the hash table
        if self.hashmap[index] is not None:

            # iterate over the list of key-value pairs at the index
            for i in range(len(self.hashmap[index])):

                # check if the key in the pair is the same as the one passed to the method
                if self.hashmap[index][i][0] == key:

                    # if so, return the value associated with the key
                    return self.hashmap[index][i][1]
        # return none if the key is not found
        return None

    def keys(self) -> list[key, value]:

        keys = []

        for i in range(len(self.hashmap)):

            if self.hashmap[i] is not None:

                for j in range(len(self.hashmap[i])):   # the range to iterate is the [ i ]

                    keys.append(self.hashmap[i][j][0])
        return keys 

    def find_duplicates(self, nums:list[int]) ->list:
        count = {}
        for num  in nums:
            count[num] = count.get(num, 0) + 1
        dups = []

        for num, count in count.items():
            if count > 1:
                dups.append(num)
        return dups

    def first_non_repeating_chars(self, string:str) -> str|None:
        chars_count = {}
        for c in string:
            chars_count[c] = chars_count.get(c, 0) + 1

        for char in string:
            if char[char] == 1:
                return char
        return None












