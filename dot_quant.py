import re

###########
#   Dot   #
###########
"""
By default, matches any character except newline
Use re.DOTALL flag to include newline
"""
# Match "c", then any character, then "t"
print(re.sub(r"c.t", "X", "tac tin cat abc;tuv acute"))
# taXin X abXuv aXe

# Match "r", then any 2 characters, then "d"
print(re.sub(r"r..d", "X", "breadth markedly reported overrides"))
# bXth maXly repoX oveXes

# Match "2", then any character, then "3"
print(re.sub(r"2.3", "8", "42\t35"))
# 485

print(bool(re.search(r"a.b", "a\nb")))
# False
print(bool(re.search(r"a.b", "a\nb", flags=re.DOTALL)))
# True

# Some characters require multiple dots to match
print(re.sub(r"a.e", "o", "cag̈ed"))
print(re.sub(r"a..e", "o", "cag̈ed"))

##################
#   re.split()   #
##################
"""
Regex version of str.split() method
"""
# Split on "-"
print(re.split(r"-", "apple-85-mango-70"))
# ['apple', '85', 'mango', '70']

# maxsplit argument determines maximum number of times to split input
print(re.split(r"-", "apple-85-mango-70", maxsplit=1))
# ['apple', '85-mango-70']
print(re.split(r"-", "apple-85-mango-70", maxsplit=2))
# ['apple', '85', 'mango-70']

# Combine with metacharacters
# Split on ":.:" (one character surrounded by colons)
print(re.split(r":.:", "bus:3:car:-:van"))
# ['bus', 'car', 'van']

##########################
#   Greedy quantifiers   #
##########################
"""
Greedy quantifiers match as many times as is possible
? - match preceding character or group 0 or 1 times
* - match preceding character or group 0 or more times
+ - match preceding character or group 1 or more times
{m,n} - match preceding character or group between m and n times
{m,} - match preceding character or group at least m times
{,n} - match preceding character or group up to n times (including 0)
{m} - match preceding character or group exactly m times
"""
# Same as r"ear|ar" (match "ear" or "ar" anywhere)
print(re.sub(r"e?ar", "X", "far feat flare fear"))
# fX feat flXe fX

# Same as r"\bpar(t|)\b" (match whole word "par" or "part")
print(re.sub(r"\bpart?\b", "X", "par spare part party"))
# X spare X party

# Same as r"\b(re.d|red)\b" (match whole word "re.d" or "red")
words = ["red", "read", "ready", "re;d", "road", "redo", "reed", "rod"]
print([w for w in words if re.search(r"\bre.?d\b", w)])
# ['red', 'read', 're;d', 'reed']

# Same as r"part|parrot" (match "part" or "parrot" anywhere)
print(re.sub(r"par(ro)?t", "X", "par part parrot parent parrots party"))
# par X X parent Xs Xy

# Same as r"part|parrot|parent" (match "part" or "parrot" or "parent" anywhere)
print(re.sub(r"par(en|ro)?t", "X", "par part parrot parent parrots party apparently"))
# par X X X Xs Xy apXly

# Match "t" followed by 0 or more instances of "a" followed by "r"
print(re.sub(r"ta*r", "X", "tr tear tare steer sitaara"))
# X tear Xe steer siXa

# Match "t" followed by 1 or more instances of "a" followed by "r"
print(re.sub(r"ta+r", "X", "tr tear tare steer sitaara"))
# tr tear Xe steer siXa

# Match "t" followed by 0 or more instances of "a" or "e" (inclusive - "tear" becomes "X") followed by "r"
print(re.sub(r"t(a|e)*r", "X", "tr tear tare steer sitaara"))
# X X Xe sX siXa

# Match "t" followed by 1 or more instances of "e" or "a" (inclusive - "tear" becomes "X") followed by "r"
print(re.sub(r"t(e|a)+r", "X", "tr tear tare steer sitaara"))
# tr X Xe sX siXa

# Match 0 or more instances of "1" followed by "2"
print(re.sub(r"1*2", "X", "3111111111125111142"))
# 3X511114X

# Match 1 or more instances of "1" followed by "2"
print(re.sub(r"1+2", "X", "3111111111125111142"))
# 3X5111142

# Combine with re.split()
# Match 0 or more instances of "1" followed by "2"
print(re.split(r"1*2", "3111111111125111142"))
# ['3', '511114', '']
# Empty string at the end as final "2" is the last character in the input string

print(re.split(r"1*2", "3111111111125111142", maxsplit=1))
# ['3', '5111142']

# Match 0 or more instances of "u"
print(re.split(r"u*", "cloudy"))
# ['', 'c', 'l', 'o', '', 'd', 'y', '']
# Split after every character (note also the empty strings at the start and end)
# "u" is converted to an empty string

# Match 1 or more instances of "u"
print(re.split(r"u+", "cloudy"))
# ['clo', 'dy']
# Only split on matching "u"

repeats = ["abc", "ac", "adc", "abbc", "xabbbcz", "bbb", "bc", "abbbbc", "abbbbbc"]

# Match on "a" followed by between 1 and 4 instances of "b" followed by "c"
print([r for r in repeats if re.search(r"ab{1,4}c", r)])
# ['abc', 'abbc', 'xabbbcz', "abbbbc"]

# Match on "a" followed by 3 or more instances of "b" followed by "c"
print([r for r in repeats if re.search(r"ab{3,}c", r)])
# ['xabbbcz', 'abbbbc', 'abbbbbc']

# Match on "a" followed by between 0 and 2 instances of "b" followed by "c"
print([r for r in repeats if re.search(r"ab{,2}c", r)])
# ['abc', 'ac', 'abbc']

# Match on "a" followed by exactly 3 instances of "b" followed by "c"
print([r for r in repeats if re.search(r"ab{3}c", r)])
# ['xabbbcz']

# To escape {} metacharacters and match them literally, only { needs to be escaped with \
print(re.sub(r"a\{5}", "a{6}", "a{5} = 10"))
# a{6} = 10

# If the characters inside {} aren't one of the four specified quantifiers, no escaping is needed
print(re.sub(r"_{a,b}", "-{c,d}", "report_{a,b}.txt"))
# report-{c,d}.txt

#######################
#   Conditional AND   #
#######################
"""
Greedy quantifiers backtrack until a match is found.
In the examples below, re.search consumes all characters after "Error" to the end of the string, then backtracks one character at a time until it finds (or doesn't find) a match
"""
# Match "Error" followed by 0 or more characters followed by "valid"
print(bool(re.search(r"Error.*valid", "Error: not a valid input")))
# True
print(bool(re.search(r"Error.*valid", "Error: key not found")))
# False

# Greedy quantifier matches as many times as possible, so returns "Xt" ("foo" replaced) not "Xot" ("fo" replaced)
print(re.sub(r"f.?o", "X", "foot"))
# Xt

# Prefix "<" with "\" if it is not already prefixed
# "<" and "\<" will both be replaced with "\<"
# Note use of raw strings in all arguments
print(re.sub(r"\\?<", r"\<", r"table \< fig < bat \< box < cake"))
# table \< fig \< bat \< box \< cake
print(re.sub(r"\\?<", "\<", "table \< fig < bat \< box < cake"))

# Compare to r"handful|handy|hand" example in alt_group.py
# No need to sort by longest
print(re.sub(r"hand(y|ful)?", "X", "hand handy handful"))
# X X X

sentence = "that is quite a fabricated tale"

# Matches from first "t" to last "a"
# Implies that only 1 match is possible for this type of pattern
print(re.sub(r"t.*a", "X", sentence))
# Xle
print(re.sub(r"t.*a", "X", "star"))
# sXr

# Backtracks to "q" then "f"
print(re.sub(r"t.*a.*q.*f", "X", sentence))
# Xabricated tale

# Backtracks to "u"
print(re.sub(r"t.*a.*u", "X", sentence))
# Xite a fabricated tale

##############################
#   Non-greedy quantifiers   #
##############################
"""
Append ? to a greedy quantifier to make it non-greedy
Also known as lazy or reluctant quantifiers
Match as minimally as possible
"""

# Lazily match any character between "f" and "o"
print(re.sub(r"f.??o", "X", "foot"))
# Xot
print(re.sub(r"f.??o", "X", "frost"))
# Xst

# Greedy, any character, 0 or 1 times
# Matches empty string, then "123456789"
print(re.sub(r".?", "X", "123456789"))
# XXXXXXXXXX

# Non-greedy, any character, 0 or 1 times
# Matches empty string, character, empty string, character... up to final empty string
print(re.sub(r".??", "X", "123456789"))
# XXXXXXXXXXXXXXXXXXX

# No quantifier, any character
# Matches every character
print(re.sub(r".", "X", "123456789"))
# XXXXXXXXX

# Non-greedy, any character, 0 or more times
# Matches empty string, character, empty string, character... up to final empty string
print(re.sub(r".*?", "X", "123456789"))
# XXXXXXXXXXXXXXXXXXX

# Non-greedy, any character between 2 and 5 times
# Isn't n=5 redundant here?
print(re.sub(r".{2,5}", "X", "123456789"))
# XXXX9
print(re.sub(r".{2,5}?", "X", "123456789", count=1))
# X3456789

# Greedy, any character, 0 or more times
print(re.split(r":.*:", "green:3.14:teal::brown:oh!:blue"))
# ["green", "blue"]

# Non-greedy, any character, 0 or more times
print(re.split(r":.*?:", "green:3.14:teal::brown:oh!:blue"))
# ['green', 'teal', 'brown', 'blue']

##############################
#   Possessive quantifiers   #
##############################
"""
Append + to a greedy quantifier to make it possessive
Only in Python >=3.11 (use regex module for Python <3.11)
Possessive quantifiers don't backtrack to find a match
"""
