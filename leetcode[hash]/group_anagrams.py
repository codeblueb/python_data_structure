def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = "".join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())


check = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(check))
