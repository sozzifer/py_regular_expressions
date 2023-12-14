import re

###################
#   re.search()   #
###################

# re.search returns a Match object if a match is found
sentence = "This is a sample string"

# Returns True
"is" in sentence
bool(re.search(r"is", sentence))

# Returns False
"cat" in sentence
bool(re.search(r"cat", sentence))

# Set `flags=re.I` for case-insensitive search
print(bool(re.search(r"this", sentence, flags=re.I)))  # Returns True

words = ["cat", "attempt", "tattle"]
tt_words = [w for w in words if re.search(r"tt", w)]

print(all(re.search(r"tt", w) for w in words))
print(all(re.search(r"at", w) for w in words))
print(any(re.search(r"dog", w) for w in words))

################
#   re.sub()   #
################

# re.sub() returns a new string object (strings are immutable)
greeting = "Have a nice weekend"
new_greeting = re.sub(r"e", "E", greeting)
new_greeting2 = re.sub(r"e", "E", greeting, count=2)
# print(greeting)
# print(new_greeting)
# print(new_greeting2)

####################
#   re.compile()   #
####################

# re.compile returns a Pattern object which can be used to search and substitute
pet = re.compile(r"dog")

print(bool(pet.search("They bought a dog")))  # Returns True ("dog" found)
print(bool(pet.search("They bought a cat")))  # Returns False ("dog" not found)
print(pet.sub(r"cat", "They bought a dog"))  # Substitute "cat" for "dog"

# Pattern objects have a search() method with optional start/end arguments
word = re.compile(r"is")

print(bool(word.search(sentence, 4)))  # Search starting from the 5th character
print(bool(word.search(sentence, 6)))  # Search starting from the 7th character
print(bool(word.search(sentence, 2, 4)))  # Search from the 3rd to the 4th character

#################
#   Exercises   #
#################

line1 = "start address: 0xA0, func1 address: 0xC0"
line2 = "end address: 0xFF, func2 address: 0xB0"
print(bool(re.search(r"0xB0", line1)))
print(bool(re.search(r"0xB0", line2)))

ip = "They ate 5 apples and 5 oranges"
five = re.compile(r"5")
print(five.sub(r"five", ip, 1))

items = ["goal", "new", "user", "sit", "eat", "dinner"]
print([w for w in items if not re.search(r"e", w)])

ip = "This note should not be NoTeD"
print(re.sub(r"note", "X", ip, flags=re.I))

ip = b"tiger imp goat"
print(bool(re.search(rb"at", ip)))

para = """good start
Start working on that
project you always wanted
stars are shining brightly
hi there
start and try to
finish the book
bye"""

pat = re.compile(r"start", flags=re.I)
for line in para.split("\n"):
    if not pat.search(line):
        print(line)

# For the given list, filter all elements that contain either a or w.
items = ["goal", "new", "user", "sit", "eat", "dinner"]
# ['goal', 'new', 'eat']
print([w for w in items if re.search(r"a", w) or re.search(r"w", w)])
# ['new', 'dinner']
print([w for w in items if re.search(r"e", w) and re.search(r"n", w)])

# For the given string, replace 0xA0 with 0x7F and 0xC0 with 0x1F.
ip = "start address: 0xA0, func1 address: 0xC0"
# start address: 0x7F, func1 address: 0x1F
print(re.sub(r"0xC0", "0x1F", re.sub(r"0xA0", "0x7F", ip)))
