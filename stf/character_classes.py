import re

#############################
#   Custom character sets   #
#############################
"""
Enclosing characters inside [] creates a character set or class
Matches any of the enclosed characters once
Similar to single character alternation e.g. (a|b)
"""
words = ["cute", "cat", "cot", "coat", "cost", "scuttle"]

# same as: r'cot|cut' or r'c(o|u)t'
print([w for w in words if re.search(r"c[ou]t", w)])
# ['cute', 'cot', 'scuttle']

# r'.(a|e|o)+t' won't work as capture group prevents getting the entire match
print(re.findall(r".(a|e|o)+t", "meeting cute boat site foot cat net"))
# ['e', 'a', 'o', 'a', 'e']
print(re.findall(r".[aeo]+t", "meeting cute boat site foot cat net"))
# ["meet", "boat", "foot", "cat", "net"]

########################
#   Character ranges   #
########################
"""
- (dash) metacharacter denotes a character range
"""
# Match all digits
print(re.findall(r"[0123456789]+", "Sample123string42with777numbers"))
print(re.findall(r"[0-9]+", "Sample123string42with777numbers"))
# ['123', '42', '777']

# Match whole words made up of lowercase alphabets and digits only
print(
    re.findall(
        r"\b[abcdefghijklmnopqrstuzwxyz0123456789]+\b",
        "coat Bin food tar12 best Apple fig_42",
    )
)
print(re.findall(r"\b[a-z0-9]+\b", "coat Bin food tar12 best Apple fig_42"))
# ['coat', 'food', 'tar12', 'best']

# Match whole words starting with 'p' to 'z' and consisting only of lowercase letters
print(re.findall(r"\b[p-z][a-z]*\b", "coat tin food put stoop best fig_42 Pet"))
# ['tin', 'put', 'stoop']

# Match whole words consisting of only lowercase letters 'a' to 'f' and 'p' to 't'
print(re.findall(r"\b[a-fp-t]+\b", "coat tin food put stoop best fig_42 Pet"))
# ['best']

###############################
#   Negating character sets   #
###############################
"""
^ metacharacter at the start of a character set negates the contents of the set
Matches everything except the characters in the set
"""
# Match all non-digits
print(re.findall(r"[^0-9]+", "Sample123string42with777numbers"))
# ['Sample', 'string', 'with', 'numbers']

# Remove the first two sections where : is the delimiter
print(re.sub(r"\A([^:]+:){2}", "", "apple:123:banana:cherry"))
# banana:cherry

# Delete characters at the end of string based on a delimiter
print(re.sub(r"=[^=]+\Z", "", "apple=42; cherry=123"))
# apple=42; cherry

# Note that the third character set negates comma and comma is matched optionally outside the capture groups
dates = "2023/04/25,1986/Mar/02,77/12/31"
print(re.findall(r"([^/]+)/([^/]+)/([^,]+),?", dates))
# [('2023', '04', '25'), ('1986', 'Mar', '02'), ('77', '12', '31')]

words = ["tryst", "fun", "glyph", "pity", "why", ""]
# Words not containing vowel characters
print([w for w in words if re.search(r"\A[^aeiou]+\Z", w)])
# ['tryst', 'glyph', 'why']

# Use a positive character class and negate result of re.search()
print([w for w in words if not re.search(r"[aeiou]", w)])

# Above would also match on empty strings
print([w for w in words if w and not re.search(r"[aeiou]", w)])

#########################################
#   Matching metacharacters literally   #
#########################################
"""
Prefix metacharacter with \ to escape it
- can be matched without escaping if at start or end of character set
^ can be matched without escaping if not at start of character set
[ can be matched without escaping if at end of character set
] can be matched without escaping if at start of character set
"""
print(re.findall(r"\b[a-z-]{2,}\b", "ab-cd gh-c 12-423 x-yz"))
print(re.findall(r"\b[-a-z]{2,}\b", "ab-cd gh-c 12-423 x-yz"))
# ['ab-cd', 'gh-c', 'x-yz']

print(re.findall(r"\b[a-z\-0-9]{2,}\b", "ab-cd gh-c 12-423 x-yz"))
# ['ab-cd', 'gh-c', '12-423', 'x-yz']

print(re.findall(r"a[+^]b", "f*(a^b) - 3*(a+b)"))
print(re.findall(r"a[\^+]b", "f*(a^b) - 3*(a+b)"))
# ['a^b', 'a+b']

s = "words[5] = tea"
print(re.search(r"[]a-z0-9[]+", s)[0])
print(re.search(r"[a-z\[\]0-9]+", s)[0])
# words[5]
print(re.sub(r"[][]", "", s))
# words5 = tea

print(re.search(r"[a\\b]+", r"5ba\babc2")[0])
# ba\bab

##############################
#   Special character sets   #
##############################
"""
\w equivalent to [a-zA-Z0-9_]
\d equivalent to [0-9]
\s equivalent to [ \t\n\r\f\v] (all whitespace characters)
\W equivalent to [^a-zA-Z0-9_]
\D equivalent to [^0-9]
\S equivalent to [^ \t\n\r\f\v]
"""
# Match any digit
print(re.split(r"\d+", "Sample123string42with777numbers"))
# ['Sample', 'string', 'with', 'numbers']

print(re.findall(r"\d+", "apple=5, banana=3; x=83, y=120"))
# ['5', '3', '83', '120']

# Match any word character at the start of a word boundary
print("".join(re.findall(r"\b\w", "sea eat car rat eel tea")))
# secret

# Match any word or whitespace character
print(re.findall(r"[\w\s]+", "tea sea-Pit Sit;(lean_2\tbean_3)"))
# ['tea sea', 'Pit Sit', 'lean_2\tbean_3']

# Match any non-digit
print(re.sub(r"\D+", "-", "Sample123string42with777numbers"))
# -123-42-777-

# Match any non-word character
print(re.sub(r"\W+", ":", "apple=5, banana=3; x=83, y=120"))
# apple:5:banana:3:x:83:y:120

# Match any non-whitespace character
print(re.findall(r"\S+", "   7..9  \v\f  fig_tea 42\tzzz   \r\n1-2-3  "))

# Match strings where the first non-whitespace character is not #
ip = ["#comment", "c = '#'", "\t #comment", "fig", "", " \t "]

# Fails because \s* can backtrack and [^#] matches on whitespace
print([s for s in ip if re.search(r"\A\s*[^#]", s)])
# ["c = '#'", '\t #comment', 'fig', ' \t ']

# Using possessive quantifier ensures \s* doesn't backtrack
print([s for s in ip if re.search(r"\A\s*+[^#]", s)])
# ["c = '#'", 'fig']

# If possessive quantifier is not supported
print([s for s in ip if re.search(r"\A\s*[^#\s]", s)])
# ["c = '#'", 'fig']

######################
#   Numeric ranges   #
######################
"""
Can fail on edge cases - use re.finditer() if necessary to convert strings to numerical values
"""
# Match numbers between 10 and 29
print(re.findall(r"\b[12]\d\b", "23 154 12 26 98234"))
# ["23", "12", "26"]

# Match numbers >= 100
print(re.findall(r"\b\d{3,}\b", "23 154 12 26 98234"))
# ["154", "98234"]

# Match numbers >= 100 with leading zeroes
print(re.findall(r"\b0*+\d{3,}\b", "0501 035 154 12 26 98234"))

# Match numbers < 350
m_iter = re.finditer(r"\d+", "45 349 651 593 4 204 350")
print([m[0] for m in m_iter if int(m[0]) < 350])
# ['45', '349', '4', '204']


# Passing a callable to re.sub()
def num_range(s):
    return "1" if 200 <= int(s[0]) < 650 else "0"


# num_range passed to repl argument as a Match object and returns a replacement string to be used
print(re.sub(r"\d+", num_range, "45 349 651 593 4 204"))
# 0 1 0 1 0 1

#################
#   Exercises   #
#################

# For the list items, filter all elements starting with hand and ending immediately with s or y or le.

items = ["-handy", "hand", "handy", "unhand", "hands", "hand-icy", "handle"]
print([i for i in items if re.search(r"\Ahand[sy]|le", i)])
# ['handy', 'hands', 'handle']

# Replace all whole words reed or read or red with X.

ip = "redo red credible :read: rod reed"
print(re.sub(r"\b[read]+\b", "X", ip))
# redo X credible :X: rod X
# \bre[ae]?d\b

# For the list words, filter all elements containing e or i followed by l or n. Note that the order mentioned should be followed.

words = ["surrender", "unicorn", "newer", "door", "empty", "eel", "pest"]
print([w for w in words if re.search(r"(e|i).*(l|n)", w)])
# ['surrender', 'unicorn', 'eel']
# [ei].*[ln]

# For the list words, filter all elements containing e or i and l or n in any order.
print([w for w in words if re.search(r"[ei].*[ln]|[ln].*[ei]", w)])
# ['surrender', 'unicorn', 'newer', 'eel']

# Extract all hex character sequences, with 0x optional prefix. Match the characters case insensitively, and the sequences shouldn't be surrounded by other word characters.
str1 = "128A foo 0xfe32 34 0xbar"
str2 = "0XDEADBEEF place 0x0ff1ce bad"

pat = re.compile(r"\b(0x)?[\da-f]+\b", flags=re.I)

hex_iter = pat.finditer(str1)
print([h[0] for h in hex_iter])
# ["128A", "0xfe32", "34"]

hex_iter = pat.finditer(str2)
print([h[0] for h in hex_iter])
# ["0XDEADBEEF", "0x0ff1ce", "bad"]

# Delete from ( to the next occurrence of ) unless they contain parentheses characters in between.

str1 = "def factorial()"
str2 = "a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)"
str3 = "Hi there(greeting). Nice day(a(b)"

del_paren = re.compile(r"\([^()]*\)")

print(del_paren.sub("", str1))
# def factorial

print(del_paren.sub("", str2))
# a/b + c%d - (e+*4)

print(del_paren.sub("", str3))
# Hi there. Nice day(a

# For the list words, filter all elements not starting with e or p or u.
words = ["surrender", "unicorn", "newer", "door", "empty", "eel", "(pest)"]

not_epu = re.compile(r"\b[^epu]")

print([w for w in words if not_epu.search(w)])
# ['surrender', 'newer', 'door', '(pest)']

# For the list words, filter all elements not containing u or w or ee or -.
words = ["p-t", "you", "tea", "heel", "owe", "new", "reed", "ear"]

print([w for w in words if not re.search(r"[uw-]|ee", w)])
# ['tea', 'ear']

# The given input strings contain fields separated by , and fields can be empty too. Replace last three fields with WHTSZ323.

row1 = "(2),kite,12,,D,C,,"
row2 = "hi,bye,sun,moon"

pat = re.compile(r"(,[^,]*){3}\Z")

print(pat.sub(",WHTSZ323", row1))
# (2),kite,12,,D,WHTSZ323

print(pat.sub(",WHTSZ323", row2))
# hi,WHTSZ323

# Split the given strings based on consecutive sequence of digit or whitespace characters.

str1 = "lion \t Ink32onion Nice"
str2 = "**1\f2\n3star\t7 77\r**"

pat = re.compile(r"[\d\s]+")

print(pat.split(str1))
# ["lion", "Ink", "onion", "Nice"]

print(pat.split(str2))
# ["**", "star", "**"]

# Delete all occurrences of the sequence <characters> where characters is one or more non > characters and cannot be empty.

ip = "a<ap\nple> 1<> b<bye> 2<> c<cat>"

pat = re.compile(r"<[^>]+>")
print(pat.sub("", ip))
# "a 1<> b 2<> c"

# \b[a-z](on|no)[a-z]\b is same as \b[a-z][on]{2}[a-z]\b. True or False? Sample input lines shown below might help to understand the differences, if any.

words = ["known", "mood", "know", "pony", "inns"]

pat1 = re.compile(r"\b[a-z](on|no)[a-z]\b")
pat2 = re.compile(r"\b[a-z][on]{2}[a-z]\b")

print([w for w in words if pat1.search(w)])
# ["know", "pony"]
print([w for w in words if pat2.search(w)])
# ["mood", "know", "pony", "inns"]

# For the given list, filter all elements containing any number sequence greater than 624.

items = ["hi0000432abcd", "car00625", "42_624 0512", "3.14 96 2 foo1234baz"]

print([i for i in items if any(int(m[0]) > 624 for m in re.finditer(r"\d+", i))])
# ['car00625', '3.14 96 2 foo1234baz']

# By default, the str.split() method will split on whitespace and remove empty strings from the result. Which re module function would you use to replicate this functionality?

ip = " \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f"

print(re.findall(r"\S+", ip))

# Convert the given input string to two different lists as shown below.

ip = "price_42 roast^\t\n^-ice==cat\neast"

print(re.split(r"\W+", ip))
# ["price_42", "roast", "ice", "cat", "east"]

print(re.split(r"(\W+)", ip))
# ["price_42", " ", "roast", "^\t\n^-", "ice", "==", "cat", "\n", "east"]

# Filter all whole elements with optional whitespaces at the start followed by three to five non-digit characters. Whitespaces at the start should not be part of the calculation for non-digit characters.

words = ["\t \ncat", "goal", " oh", "he-he", "goal2", "ok ", "sparrow"]

print([w for w in words if re.fullmatch(r"\s*+\D{3,5}", w)])
# ['\t \ncat', 'goal', 'he-he', 'ok ']
