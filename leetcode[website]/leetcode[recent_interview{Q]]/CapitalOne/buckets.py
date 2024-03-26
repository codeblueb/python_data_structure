
def buckets(commands:list[str]) -> str|None:
    """
        Example 1
        The idea : simple use hashmap
    """
    buckets = {}
    current_bucket = None

    for string in commands:
        cmd[0], name[1] = string.split()

        if cmd == "goto":
            current_bucket = name[1]
            if current_bucket not in buckets:
                buckets[current_bucket] = set() # make sure no dups file
        elif cmd == "create":
            if name not in buckets[name]:
                buckets[current_bucket].add(name[1])

    return max(buckets, key=buckets.get, default=None)

commands = [
    "goto bucketA",
    "create fileA",
    "create fileB",
    "create fileC",
    "goto bucketB",
    "goto bucketC",
    "create fileA",
    "create fileB",
    "create fileC",
]

print(buckets(commands))

def file_buckets(commands:str) -> str|None:
    """
        Example 2
        Hashmap and stack
    """
    buckets = {}
    stack = []

    for string in commands:
        cmd, name = string.split()[0], string.split()[1]

        if cmd == "goto":
            stack.append(name)
            if stack.pop() not in buckets:
                buckets[name] = set()
        elif cmd == "create":
            if name not in buckets[name]:
                buckets[stack.pop()].add(name)

    return max(buckets, key=buckets.get, default=None)

print(file_buckets(commands))

