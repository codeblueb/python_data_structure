def convert_word(word):
    arr = list(word)
    end = len(arr) - 1
    i = 1
    while i < end:  # current end is the second to the last string
        # check for underscores from the second index.
        if word[i] == "_":
            if (
                arr[i - 1].isalpha() and arr[i + 1].isalpha()
            ):  # use two pointers to check for leading and trailing alphabets.
                arr[i + 1] = arr[i + 1].capitalize()
                arr.pop(i)
                end -= 1
        i += 1
    arr = arr[: end + 1]
    return "".join(arr)


def snake_to_camel(text):
    words = text.split()
    converted_words = [convert_word(word) for word in words]
    result = " ".join(converted_words)
    return result


txt = "__variable_one__ _variable_two variable_three"
print(snake_to_camel(txt))  # output: __variableOne__ _variableTwo variableThree


