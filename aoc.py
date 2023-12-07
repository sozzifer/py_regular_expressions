import re


with open("aoc.txt", "r") as f:
    ex = f.read().splitlines()

print(len(ex))
DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


ex1 = ex[0]
pat = re.compile("|".join(k for k in DIGITS.keys()))
print(pat.search(ex1).match)
# print(pat.sub(DIGITS[pat.search(ex1)]))

replace_first = []
# for e in ex:
#     replace_first.append(pat.sub())