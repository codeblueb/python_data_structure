
def buckets(commands:list[str]) -> str|None:
    """
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

    return mas(buckets, key=buckets.get, default=None)

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
