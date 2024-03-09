def first_non_repeating_char(string:str) -> str|None:
    chars_count = {}
    for c in string:
        chars_count[c] = chars_count.get(c, 0) + 1

    for char in string:
        if chars_count[char] == 1:
            return c
    return None
