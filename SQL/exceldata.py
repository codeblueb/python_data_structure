# https://youtu.be/1RCMYG8RUSE?si=sue8WBsvHqbCd7qU

import csv

from collections import Counter

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {} | Counter()

    for row in reader:
        fav = row["language"]
        if fav in counts:
            counts[fav] += 1
        else:
            counts[fav] = 1

    for row in reader:  # another better and faster way to the same thing as above
        fav = row["language"]
        Counter(fav) + 1

for fav in sorted(counts):
    print(f"{fav}: {counts[fav]}")

for fav in sorted(counts, key=counts.get):
    print(f"{fav}: {counts[fav]}")


for fav in sorted(counts, key=counts.get, reverse=True):
    print(f"{fav}: {counts[fav]}")
