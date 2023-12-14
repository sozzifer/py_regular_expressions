import re

######################
#   String anchors   #
######################
"""
\A (prefix): Match pattern at start of the search string
\Z (suffix): Match pattern at end of the search string
"""
# # Match pattern at start of the search string
# print(bool(re.search(r"\Acat", "cater")))  # Returns True
# print(bool(re.search(r"\Acat", "concatenation")))  # Returns False
# print(bool(re.search(r"\Ahi", "hi    hello\ntop spot")))  # Returns True
# print(bool(re.search(r"\Atop", "hi    hello\ntop spot")))  # Returns False

# # Match pattern at end of the search string
# print(bool(re.search(r"are\Z", "spare")))  # Returns True
# print(bool(re.search(r"are\Z", "nearest")))  # Returns False

# words = ["surrender", "unicorn", "under", "door", "erase", "eel", "spun"]
# print([w for w in words if re.search(r"\Aun", w)])
# print([w for w in words if re.search(r"er\Z", w)])
# print([w for w in words if re.search(r"\Aun", w) and re.search(r"er\Z", w)])
# print([w for w in words if re.search(r"\Aun", w) or re.search(r"er\Z", w)])

# # Use anchors as patterns on their own
# print(re.sub(r"\A", "re", "send"))  # "resend"
# print(re.sub(r"\A", "re", "live"))  # "relive"
# print(re.sub(r"\Z", "er", "cat"))  # "cater"
# print(re.sub(r"\Z", "er", "hack"))  # "hacker"

# # When specifying the pos and endpos arguments in re.search() using anchors, use slice notation
# pat = re.compile(r"\Aat")
# print(bool(pat.search(r"cater", 1)))  # Returns False
# print(
#     bool(pat.search(r"cater"[1:]))
# )  # Returns True as "cater"[1:] is a new string object

# # Combine the \A and \Z anchors to match an entire string
# pat = re.compile(r"\Acat\Z")
# print(bool(pat.search("cat")))  # Returns True
# print(bool(pat.search("concatenation")))  # Returns False

# # re.fullmatch() also allows matching of an entire string
# pat = re.compile(r"cat", flags=re.I)
# print(bool(pat.fullmatch("Cat")))  # Returns True
# print(bool(pat.fullmatch("Scatter")))  # Returns False

####################
#   Line anchors   #
####################
"""
\n: newline separator
^ (prefix): Match at the start of a line
$ (suffix): Match at the end of a line
"""

# pets = "cat and dog"
# print(bool(re.search(r"^cat", pets)))  # Returns True
# print(bool(re.search(r"^dog", pets)))  # Returns False
# print(bool(re.search(r"dog$", pets)))  # Returns True
# print(bool(re.search(r"^dog$", pets)))  # Returns False

# cat_start = re.compile(r"^cat")
# cat_end = re.compile(r"cat$")
# print(bool(cat_start.search("cat and dog")))  # Returns True
# print(bool(cat_end.search("cat and dog")))  # Returns False

# # By default, input string interpreted as a single line, even if multiple newline characters included
# greeting = "hi there\nhave a nice day\n"

# # $ ignores \n at the end of a multiline string
# print(bool(re.search(r"day$", greeting)))  # Returns True
# print(bool(re.search(r"day\n$", greeting)))  # Returns True

# # \Z does not ignore \n at the end of a multiline string
# print(bool(re.search(r"day\Z", greeting)))  # Returns False
# print(bool(re.search(r"day\n\Z", greeting)))  # Returns True

# # re.MULTILINE flag (re.M)
# # Match if pattern found at start of any line
# print(bool(re.search(r"^top", "hi hello\ntop spot", flags=re.M)))  # Returns True
# # Match if pattern found at end of any line
# print(bool(re.search(r"ar$", "spare\npar\ndare", re.M)))  # Returns True

# # Match all elements with pattern at end of line
# elements = ["spare\ntool", "par\n", "dare"]
# print(
#     [e for e in elements if re.search(r"are$", e, flags=re.M)]
# )  # ['spare\ntool', 'dare']

# # Use anchors as patterns on their own
# ip = "catapults\nconcatenate\ncat"

# # Append "* " to the start of each line
# print(re.sub(r"^", "* ", ip, flags=re.M))
# # * catapults
# # * concatenate
# # * cat

# # Append "." to the end of each line
# print(re.sub(r"$", ".", ip, flags=re.M))
# # catapults.
# # concatenate.
# # cat.

####################
#   Word anchors   #
####################
"""
Words consist of letters (A-Z, a-z), digits (0-9) and underscores (_)
\b (prefix or suffix): Word boundary (start or end)
\B (prefix or suffix): !Word boundary (start or end)
\b (prefix): previous character is a non-word value or start of string (no preceding characters)
\b (suffix): next character is a non-word value or end of string (no subsequent characters)
\B (prefix): previous character is a word
\B (suffix): next character is a word
"""

# words = "par spar apparent spare part"

# # \b
# # Replace all instances of "par" with "X"
# print(re.sub(r"par", "X", words))
# # X sX apXent sXe Xt

# # Replace "par" at the start of word
# print(re.sub(r"\bpar", "X", words))
# # X spar apparent spare Xt

# # Replace "par" at end of word
# print(re.sub(r"par\b", "X", words))
# # X sX apparent spare part

# # Replace "par" only if not part of another word
# print(re.sub(r"\bpar\b", "X", words))
# # X spar apparent spare part

# # Use anchors as patterns on their own

# # Space separated words to double quoted words
# print(re.sub(r"\b", "'", words))
# # 'par' 'spar' 'apparent' 'spare' 'part'

# # Space separated words to double quoted csv
# print(re.sub(r"\b", "'", words).replace(" ", ","))  # replace() str method
# # 'par','spar','apparent','spare','part'

# # \B
# # Replace "par" if not at the start of a word
# print(re.sub(r"\Bpar", "X", words))
# # par sX apXent sXe part

# # Replace "par" at the end of a word, but not "par" itself
# print(re.sub(r"\Bpar\b", "X", words))

# # Replace "par" only in the middle of words
# print(re.sub(r"\Bpar\B", "X", words))

print(re.sub(r"\b", ":", "copper"))
# :copper:
print(re.sub(r"\B", ":", "copper"))
# c:o:p:p:e:r
print(re.sub(r"\b", ":", "-----hello-----"))
# -----:hello:-----
print(re.sub(r"\B", ":", "-----hello-----"))
# :-:-:-:-:-h:e:l:l:o-:-:-:-:-:

#################
#   Exercises   #
#################

line1 = "be nice"
line2 = "'best!'"
line3 = "better?"
line4 = "oh no\nbear spotted"
pat = re.compile(r"\Abe")
print(bool(pat.search(line1)))
print(bool(pat.search(line2)))
print(bool(pat.search(line3)))
print(bool(pat.search(line4)))

words = "bred red spread credible red."
print(re.sub(r"\bred\b", "brown", words))

words = ["hi42bye", "nice1423", "bad42", "cool_42a", "42fake", "_42_"]
print([w for w in words if re.search(r"\B42\B", w)])

items = ["lovely", "1\ndentist", "2 lonely", "eden", "fly\nfar", "dent"]
print([i for i in items if re.search(r"\Aden", i) or re.search(r"ly\Z", i)])
print([i for i in items if re.search(r"^den", i, re.M) or re.search(r"ly$", i, re.M)])

para = """
(mall) call ball pall\n
ball fall wall tall\n
mall call ball pall\n
wall mall ball fall\n
mallet wallet malls\n
mall:call:ball:pall
"""
print(re.sub(r"^\bmall\b", "1234", para, flags=re.M))
# print(re.sub(r'^mall\b', '1234', para, flags=re.M))

items = ["12\nthree\n", "12\nThree", "12\nthree\n4", "12\nthree"]
print([i for i in items if re.search(r"\A\b12\nthree\b\Z", i, flags=re.I)])
# [e for e in items if re.fullmatch(r'12\nthree', e, flags=re.I)]

items = ["handed", "hand", "handy", "un-handed", "handle", "hand-2"]
print([re.sub(r"^hand\B", "X", i) for i in items])
# [re.sub(r'\Ahand\B', 'X', w) for w in items]

print([re.sub(r"e", "X", i) for i in items if re.search(r"^h", i)])
# [re.sub(r'e', 'X', w) for w in items if re.search(r'\Ah', w)]
