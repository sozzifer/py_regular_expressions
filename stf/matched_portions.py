import re
import math

#######################
#   re.Match object   #
#######################
"""
re.search() and re.fullmatch() return re.Match object
Can extract matched portion, location of match etc
Only for first match
"""
print(re.search(r"so+n", "too soon a song snatch"))
# <re.Match object; span=(4, 8), match='soon'>

print(re.fullmatch(r"1(2|3)*4", "1233224"))
# <re.Match object; span=(0, 7), match='1233224'>

sentence = "that is quite a fabricated tale"
m = re.search(r"q.*?t", sentence)
# span() method returns tuple of start and end+1 index of matching portion
print(m.span())
# (8, 12)

# group() method returns matched portion as defined in the RE
print(m.group())
# quit (matches RE r"q.*?t")

motivation = "Doing is often better than thinking of doing."
print(re.search(r"of.*ink", motivation))
# <re.Match object; span=(9, 32), match='often better than think'>

# Access the matched portion using indexing
print(re.search(r"of.*ink", motivation)[0])

# Access the matched portion using group(0) (default argument)
print(re.search(r"of.*ink", motivation).group(0))

######################
#   Capture groups   #
######################
"""
() - indicates capture group in RE
If multiple capture groups defined, re.Match[0] returns entire match
Subsequent indices return capture group matched portions
"""
purchase = "coffee:100g tea:250g sugar:75g chocolate:50g"
m = re.search(r":(.*?)g.*?:(.*?)g.*?chocolate:(.*?)g", purchase)
#                 [1]       [2]                [3]

# Entire matched portion
print(m.group())
print(m[0])
# :100g tea:250g sugar:75g chocolate:50g

# Matched portion of group 2
print(m.group(2))
print(m[2])
# 250

# Tuple of groups 3 and 1
print(m.group(3, 1))
# ('50', '100')

# Tuple of all capture groups (without entire matched portion)
print(m.groups())
# ('100', '250', '50')
print(len(m.groups()))
# 3

# Pass group numbers to span() to get matching locations (default 0)
print(m.span())
print(m.span(0))
# (6, 44)
print(m.span(1))
# (7, 10)
print(m.span(2))
# (16, 19)
print(m.span(3))
# (41, 43)

# Pass group numbers to start() and end() (default 0)
print(m.start())
print(m.start(0))
# 6
print(m.end())
print(m.end(0))
# 44

print(m.start(1))
# 7
print(m.end(1))
# 10

print(m.start(2))
# 16
print(m.end(2))
# 19

print(m.start(3))
# 41
print(m.end(3))
# 43

m = re.fullmatch(r"aw(.*)me", "awesome")

print(m.span(1))
# (2, 5)
print(m.start())
# 0
print(m.start(1))
# 2

##############################
#   Assignment expressions   #
##############################
if m := re.search(r"(.*)s", "oh"):
    print(m[1])

if m := re.search(r"(.*)s", "awesome"):
    print(m[1])

text = ["type: fruit", "date: 2023/04/28"]
for t in text:
    if m := re.search(r"type: (.+)", t):
        print(m[1])
    elif m := re.search(r"date: (.*?)/(.*?)/", t):
        print(f"month: {m[2]}, year: {m[1]}")
# fruit
# month: 04, year: 2023

###########################
#   Lambda replacements   #
###########################
"""
Use lambda function to replace matching portions and groups
"""

# m[0] contains the entire matched portion ("a^2" or "b^2")
print(re.sub(r"(a|b)\^2", lambda m: m[0].upper(), "a^2 + b^2 - c*3"))
# A^2 + B^2 - c*3

# m[0] contains the entire matched portion ("2" or "3")
print(re.sub(r"2|3", lambda m: str(int(m[0]) ** 2), "a^2 + b^2 - c*3"))
# a^4 + b^4 - c*9

# m[0] contains the entire matched portion ("a" or "b" or "c")
print(re.sub(r"a|b|c", lambda m: m[0] * 4, "a^2 + b^2 - c*3"))
# aaaa^2 + bbbb^2 - cccc*3

#########################
#   Dict replacements   #
#########################
"""
Use a dictionary to define mappings for replacement text
"""
d = {"1": "one", "2": "two", "4": "four"}
print(re.sub(r"1|2|4", lambda m: d[m[0]], "9234012"))
# 9two3four0onetwo

# If matched text not defined as dict key, default value used ("X")
print(re.sub(r"\d", lambda m: d.get(m[0], "X"), "9234012"))
# XtwoXfourXonetwo

# Dict can be used to avoid defining interim values
swap = {"tiger": "cat", "cat": "tiger"}
words = "cat tiger dog tiger cat"
print(re.sub(r"cat|tiger", lambda m: swap[m[0]], words))
# tiger cat dog cat tiger

####################
#   re.findall()   #
####################
"""
Returns all matched portions as a list of strings
"""
print(re.findall(r"so*n", "too soon a song snatch"))
# ['soon', 'son', 'sn']

print(re.findall(r"so+n", "too soon a song snatch"))
# ['soon', 'son']

print(re.findall(r"\bs?pare?\b", "PAR spar apparent SpArE part pare", flags=re.I))
# ['PAR', 'spar', 'SpArE', 'pare']

print(re.findall(r":.*:", "green:3.14:teal::brown:oh!:blue"))
# [":3.14:teal::brown:oh!:"]
print(re.findall(r":.*?:", "green:3.14:teal::brown:oh!:blue"))
# [":3.14:", "::", ":oh!:"]
print(re.findall(r":.*+:", "green:3.14:teal::brown:oh!:blue"))
# []

purchase = "coffee:100g tea:250g sugar:75g chocolate:50g salt:g"

# No capture group
# Output is a list of elements that match the entire RE pattern
print(re.findall(r":.*?g", purchase))
# [':100g', ':250g', ':75g', ':50g', ':g']

# One capture group
# Output is a list of elements which match the capture group
print(re.findall(r":(.*?)g", purchase))
# ['100', '250', '75', '50', '']

# Multiple capture groups
# Output is a list of tuples of elements matching each capturing group
print(re.findall(r"(.*?)/(.*?)/(.*?),", "2023/04/25,1986/Mar/02,77/12/31"))
# [('2023', '04', '25'), ('1986', 'Mar', '02')]
# Final date in input string (77/12/31) doesn't have comma, so is ignored

#####################
#   re.finditer()   #
#####################
"""
Returns iterator object where each element is a re.Match object
"""
m_iter = re.finditer(r"so+n", "song too soon snatch")
for m in m_iter:
    print(m)
# <re.Match object; span=(0, 3), match='son'>
# <re.Match object; span=(9, 13), match='soon'>

# re.Match methods can be combined with the re.finditer() iterator
m_iter = re.finditer(r"so+n", "song too soon snatch")
for m in m_iter:
    print(m[0].upper(), m.span(), sep="\t")
# SON   (0, 3)
# SOON  (9, 13)

m_iter = re.finditer(r"(.*?)/(.*?)/(.*?),", "2023/04/25,1986/Mar/02,77/12/31")
print([m.groups() for m in m_iter])
# [('2023', '04', '25'), ('1986', 'Mar', '02')]

#####################################
#   re.split() and capture groups   #
#####################################
"""
Capture groups passed to re.split() will be included in the returned list
"""
# Without capture group
print(re.split(r"1*4?2", "31111111111251111426"))
# ["3", "5", "6"]

# With capture group
print(re.split(r"(1*4?2)", "31111111111251111426"))
# ["3", "11111111112", "5", "111142", "6"]

# Partial capture group (1*)
# r"4?2" used to split input but not included in output
print(re.split(r"(1*)4?2", "31111111111251111426"))
# ["3", "1111111111", "5", "1111", "6"]

# Multiple capture groups (1*) and (4)?
# 4 isn't matched in first split match, so None included in output list
print(re.split(r"(1*)(4)?2", "31111111111251111426"))
# ['3', '1111111111', None, '5', '1111', '4', '6']

# Multiple capture groups (1*) and (4?)
# Why is idx[2] an empty string?
print(re.split(r"(1*)(4?)2", "31111111111251111426"))
# ['3', '1111111111', '', '5', '1111', '4', '6']

# Multiple capture groups (a+) and (c+)
# r"b+" ignored in output
print(re.split(r"(a+)b+(c+)", "3.14aabccc42"))
# ['3.14', 'aa', 'ccc', '42']

# Capture group and maxsplit=1 similar to str.partition()
# Result partitioned on "aabccc"
print(re.split(r"(a+b+c+)", "3.14aabccc42abc88", maxsplit=1))
# ['3.14', 'aabccc', '42abc88']

#################
#   re.subn()   #
#################
"""
Same as re.sub() but also returns number of substitutions made
"""
greeting = "Have a nice weekend"

print(re.sub(r"e", "E", greeting))
# HavE a nicE wEEkEnd

print(re.subn(r"e", "E", greeting))
# ('HavE a nicE wEEkEnd', 5)

# Recursively replace "fin" in "coffining"
word = "coffining"
while True:
    word, n = re.subn(r"fin", "", word)
    if n == 0:
        print(word)
        break

#################
#   Exercises   #
#################

# For the given strings, extract the matching portion from the first is to the last t.

str1 = "This the biggest fruit you have seen?"
str2 = "Your mission is to read and practice consistently"

pat = re.compile(r"is.*t")

s1 = pat.search(str1)
print(s1.group())
# is the biggest fruit

s2 = pat.search(str2)
print(s2.group())
# ission is to read and practice consistent

# Find the starting index of the first occurrence of "is" or "the" or "was" or "to" for the given input strings.

s1 = "match after the last newline character"
s2 = "and then you want to test"
s3 = "this is good bye then"
s4 = "who was there to see?"

pat = re.compile(r"(t(he|o)|is|was)")

print(pat.search(s1).start())
# 12
print(pat.search(s2).start())
# 4
print(pat.search(s3).start())
# 2
print(pat.search(s4).start())
# 4

# Find the starting index of the last occurrence of "is" or "the" or "was" or "to" for the given input strings.

pat = re.compile(r".*(t(he|o)|is|was)")

print(pat.search(s1).start(1))
# 12
print(pat.search(s2).start(1))
# 18
print(pat.search(s3).start(1))
# 17
print(pat.search(s4).start(1))
# 14

# The given input string contains ":" exactly once. Extract all characters after the ":" as output.

ip = "fruits:apple, mango, guava, blueberry"

print(re.split(r".*:", ip)[1])
# "apple, mango, guava, blueberry"
# re.search(r':(.*)', ip)[1]

# The given input strings contains some text followed by "-" followed by a number. Replace that number with its log value using math.log().

s1 = "first-3.14"
s2 = "next-123"

pat = re.compile(r"-(.*)")

print(pat.sub(lambda m: "-" + str(math.log(float(m[1]))), s1))
# first - 1.144222799920162

print(pat.sub(lambda m: "-" + str(math.log(float(m[1]))), s2))
# next - 4.812184355372417

# Replace all occurrences of "par" with "spar", "spare" with "extra" and "park" with "garden" for the given input strings.

str1 = "apartment has a park"
str2 = "do you have a spare cable"
str3 = "write a parser"

d = {"par": "spar", "spare": "extra", "park": "garden"}
print(re.sub(r"s*(par)(k|e)*", lambda m: d[m[0]], str1))
# aspartment has a garden
print(re.sub(r"s*(par)(k|e)*", lambda m: d[m[0]], str2))
# do you have a extra cable
print(re.sub(r"s*(par)(k|e)*", lambda m: d[m[0]], str3))
# write a sparser
# re.sub(r"park?|spare", lambda m: d[m[0]], str3)

# Extract all words between ( and ) from the given input string as a list. Assume that the input will not contain any broken parentheses.

ip = "another (way) to reuse (portion) matched (by) capture groups"
print(re.findall(r"\((.*?)\)", ip))
# ['way', 'portion', 'by']

# Extract all occurrences of < up to the next occurrence of >, provided there is at least one character in between < and >
ip = "a<apple> 1<> b<bye> 2<> c<cat>"
print(re.findall(r"<.+?>", ip))

# Use re.findall() to get the output as shown below for the given input strings. Note the characters used in the input strings carefully.

row1 = "-2,5 4,+3 +42,-53 4356246,-357532354 "
row2 = "1.32,-3.14 634,5.63 63.3e3,9907809345343.235 "
pat = re.compile(r"(.+?),(.+?) ")

print(pat.findall(row1))
# [('-2', '5'), ('4', '+3'), ('+42', '-53'), ('4356246', '-357532354')]
print(pat.findall(row2))
# [('1.32', '-3.14'), ('634', '5.63'), ('63.3e3', '9907809345343.235')]

r1 = pat.findall(row1)
r2 = pat.findall(row2)

# For row1, find the sum of integers of each tuple element. For example, sum of -2 and 5 is 3.
sum_r1 = [int(tup[0]) + int(tup[1]) for tup in r1]
print(sum_r1)
# [int(m[1]) + int(m[2]) for m in pat.finditer(row1)]

# For row2, find the sum of floating-point numbers of each tuple element. For example, sum of 1.32 and -3.14 is -1.82.
sum_r2 = [float(tup[0]) + float(tup[1]) for tup in r2]
print(sum_r2)
# [float(m[1]) + float(m[2]) for m in pat.finditer(row2)]

# Use re.split() to get the output as shown below.

ip = "42:no-output;1000:car-tr:u-ck;SQEX49801"

print(re.split(r":..+?-|;", ip))
# ['42', 'output', '1000', 'tr:u-ck', 'SQEX49801']

# For the given list of strings, change the elements into a tuple of original element and the number of times t occurs in that element.

words = ["sequoia", "attest", "tattletale", "asset"]

print([re.subn(r"t", "t", w) for w in words])
# [("sequoia", 0), ("attest", 3), ("tattletale", 4), ("asset", 1)]

# The given input string has fields separated by :. Each field contains four uppercase alphabets followed optionally by two digits. Ignore the last field, which is empty. See docs.python: Match.groups and use re.finditer() to get the output as shown below. If the optional digits aren't present, show 'NA' instead of None.

ip = "TWXA42:JWPA:NTED01:"
pat = re.compile(r"[A-Z]{4}")
m_iter = re.finditer(r"([A-Z]{4})([0-9]{2})*", ip)
print([(m.group(1), m.group(2)) for m in m_iter])
# [('TWXA', '42'), ('JWPA', 'NA'), ('NTED', '01')]
# [m.groups(default='NA') for m in re.finditer(r'(.{4})(..)?:', ip)]

# Convert the comma separated strings to corresponding dict objects as shown below.

row1 = "name:rohan,maths:75,phy:89,"
row2 = "name:rose,maths:88,phy:92,"

print({m.group(1): m.group(2) for m in re.finditer(r"(.+?):(.+?),", row1)})
# {'name': 'rohan', 'maths': '75', 'phy': '89'}
print({m.group(1): m.group(2) for m in re.finditer(r"(.+?):(.+?),", row2)})
# {'name': 'rose', 'maths': '88', 'phy': '92'}
