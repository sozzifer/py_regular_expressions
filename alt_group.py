import re

###################
#   Alternation   #
###################
"""
Combine multiple patterns using | (pipe)
Equivalent to logical OR
"""
# Match "cat" or "dog"
pet = re.compile(r"cat|dog")
print(bool(pet.search("I like cats")))
print(bool(pet.search("I like dogs")))
print(bool(pet.search("I like llamas")))

# Replace "cat" at start of string or end of word
print(re.sub(r"\Acat|cat\b", "X", "catapults concatenate cat scat cater"))

# Replace "cat" or "dog" or "fox" with "mammal"
print(re.sub(r"cat|dog|fox", "mammal", "cat dog bee parrot fox"))

# If alternative pattern has no special regex characters, string methods can be used
words = ["cat", "dog", "fox"]
print(re.sub("|".join(words), "mammal", "cat dog bee parrot fox"))

################
#   Grouping   #
################
"""
If alternative patterns share common features, these can be grouped using parentheses ()
"""
# Without grouping
print(re.sub(r"reform|rest", "X", "red reform read arrest"))
# With grouping
print(re.sub(r"re(form|st)", "X", "red reform read arrest"))
# red X read arX

# Without grouping
print(re.sub(r"\bpar\b|\bpart\b", "X", "par spare part party"))
# With grouping
print(re.sub(r"\b(par|part)\b", "X", "par spare part party"))
# Extract common characters
print(re.sub(r"\bpar(|t)\b", "X", "par spare part party"))
# X spare X party

# Combine raw strings and f strings for more complex expressions
words = ["cat", "par"]
alt = re.compile(rf"\b({'|'.join(words)})\b")
print(alt.pattern)
# \b(cat|par)\b
print(alt.sub("X", "cater cat concatenate par spare"))
# cater X concatenate X spare

# Using fullmatch() with string methods
terms = ["no", "ten", "it"]
items = ["dip", "nobody", "it", "oh", "no", "bitten"]
pat = re.compile("|".join(terms))

# Match full word
print([i for i in items if pat.fullmatch(i)])
# ['it', 'no']

# Match anywhere
print([i for i in items if pat.search(i)])
# ['nobody', 'it', 'no', 'bitten']

##################
#   Precedence   #
##################

words = "lion elephant are rope not"
print(re.search(r"on", words))
# <re.Match object; span=(2, 4), match='on'>
print(re.search(r"ant", words))
# <re.Match object; span=(10, 13), match='ant'>

# Starting index of "on" < starting index of "ant" (2<10) so "on" will be replaced regardless of the order they are specified in the alternative
print(re.sub(r"on|ant", "X", words, count=1))
print(re.sub(r"ant|on", "X", words, count=1))

# If alternatives have the same starting index, precedence is left-to-right in order of declaration
mood = "best years"
print(re.sub(r"year|years", "X", mood, count=1))
# best Xs
print(re.sub(r"years|year", "X", mood, count=1))
# best X

# Ordering alternatives
# https://www.regular-expressions.info/alternation.html
# Replace all instances of "ar" or "are" or "art"
words = "ear xerox at mare part learn eye"

# Substitutes "ar"
print(re.sub(r"ar|are|art", "X", words))
# eX xerox at mXe pXt leXn eye

# Substitutes "are|ar"
print(re.sub(r"are|ar|art", "X", words))
# eX xerox at mX pXt leXn eye

# Substitutes "are|art|ar"
print(re.sub(r"are|art|ar", "X", words))
# eX xerox at mX pX leXn eye

# Workaround - sort alternatives, longest first
words = ["hand", "handy", "handful"]
alt = re.compile("|".join(sorted(words, key=len, reverse=True)))

print(alt.pattern)
# handful|handy|hand
print(alt.sub("X", "hands handful handed handy"))
# Xs X Xed X

# Without sorting
print(re.sub("|".join(words), "X", "hands handful handed handy"))
# Xs Xful Xed Xy

#################
#   Exercises   #
#################

items = ["lovely", "1\ndentist", "2 lonely", "eden", "fly\nfar", "dent"]
print([i for i in items if re.search(r"\Aden|ly\Z", i)])
# ['lovely', '2 lonely', 'dent']

print([i for i in items if re.search(r"^den|ly$", i, flags=re.M)])
# ["lovely", "1\ndentist", "2 lonely", "fly\nfar", "dent"]

s1 = "creed refuse removed read"
s2 = "refused reed redo received"
pat = re.compile(r"re(moved|ed|ceived|fused)")
"""pat = re.compile(r're(mov|ceiv|fus|)ed')"""
print(pat.sub("X", s1))
# cX refuse X read
print(pat.sub("X", s2))
# X X redo X

s1 = "plate full of slate"
s2 = "slated for later, don't be late"
words = ["late", "later", "slated"]
pat = re.compile("|".join(sorted(words, key=len, reverse=True)))
print(pat.sub("A", s1))
# pA full of sA
print(pat.sub("A", s2))
# A for A, don't be A

items = ["slate", "later", "plate", "late", "slates", "slated "]
words = ["late", "later", "slated"]
pat = re.compile("|".join(sorted(words, key=len, reverse=True)))
"""pat = re.compile('|'.join(words))"""
print([i for i in items if pat.fullmatch(i)])
# ['later', 'late']
