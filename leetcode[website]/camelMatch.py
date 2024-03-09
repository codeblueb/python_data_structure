def camelMatch(queries: list[str], pattern: str) -> list[bool]:

    def match(s, p):
        i, j = 0, 0
        while True:
            if i == len(s):
                break

            if j == len(p):
                return s[i:].islower()

            if s[i] == p[j]:
                i += 1
                j += 1
            elif s[i].islower():
                i += 1
            else:
                return False

        return j == len(p)

    res = []
    for s in queries:
        res.append(match(s, pattern))
    return res


# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]

queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FB"

print(camelMatch(queries, pattern))
