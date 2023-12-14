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

# If the characters inside {} aren't one of the four specified integer quantifiers, no escaping is needed
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
ip = "fig:mango:pineapple:guava:apples:orange"

# Possessive
print(re.sub(r":.*+", "X", ip))
# figX

# Greedy
print(re.sub(r":.*apple", "X", ip))
# figX

# Non-greedy
print(re.sub(r":.*?", "X", ip))
# figXmangoXpineappleXguavaXapplesXorange

# Possessive quantifier won't backtrack so the pattern below will never match
print(bool(re.search(r":.*+apple", ip)))
# False
print(re.sub(r":.*apple", "X", ip))
# figXs:orange

# Find numbers >= 100 where each number has optional leading zeroes (314, 00984)
numbers = "42 314 001 12 00984"

# Fails because 0* and \d{3,} both match on leading zeroes
# Greedy quantifiers give up characters to ensure the regex succeeds
# In this case, "001" backtracks to match \d{3,}
print(re.findall(r"0*\d{3,}", numbers))
# ['314', '001', '00984']

# Adding the possessive quantifier ensures no backtracking on "001"
print(re.findall(r"0*+\d{3,}", numbers))
# ['314', '00984']

# Only using greedy quantifiers
print(re.findall(r"0*[1-9]\d{2,}", numbers))
# ['314', '00984']

#################
#   Exercises   #
#################

# Replace 42//5 or 42/5 with 8 for the given input.
ip = "a+42//5-c pressure*3+42/5-14256"
print(re.sub(r"(42//5|42/5)", "8", ip))
print(re.sub(r"42(/+)5", "8", ip))
# a+8-c pressure*3+8-14256
# print(re.sub(r"42//?5", "8", ip))

# Filter all elements starting with "hand" and ending immediately with at most one more character or "le".
items = ["handed", "hand", "handled", "handy", "unhand", "hands", "handle"]
print([i for i in items if re.search(r"\bhand(.|le)?\b", i)])
# ['hand', 'handy', 'hands', 'handle']
# [w for w in items if re.fullmatch(r'hand(.|le)?', w)]

# Use re.split() to get the output as shown for the given input strings.
eqn1 = "a+42//5-c"
print(re.split(r"42//5", eqn1))
# ['a+', '-c']
eqn2 = "pressure*3+42/5-14256"
print(re.split(r"42/5", eqn2))
# ['pressure*3+', '-14256']
eqn3 = "r*42-5/3+42///5-42/53+a"
print(re.split(r"42/5", eqn3))
# ['r*42-5/3+42///5-', '3+a']

# pat = re.compile(r"42//?5")
# print(pat.split(eqn1))
# print(pat.split(eqn2))
# print(pat.split(eqn3))

# For the given input strings, remove everything from the first occurrence of "i" till the end of the string.
s1 = "remove the special meaning of such constructs"
s2 = "characters while constructing"
s3 = "input output"
pat = re.compile(r"i.*")
print(pat.sub("", s1))
# "remove the spec"
print(pat.sub("", s2))
# "characters wh"
print(pat.sub("", s3))
# ""

# For the given strings, construct a RE to get the output as shown below.
str1 = "a+b(addition)"
str2 = "a/b(division) + c%d(#modulo)"
str3 = "Hi there(greeting). Nice day(a(b)"
remove_parentheses = re.compile(r"\(.*?\)")
print(remove_parentheses.sub("", str1))
# 'a+b'
print(remove_parentheses.sub("", str2))
# 'a/b + c%d'
print(remove_parentheses.sub("", str3))
# 'Hi there. Nice day'

# Correct the given RE to get the expected output.
words = "plink incoming tint winter in caution sentient"
# Wrong output
change = re.compile(r"int|in|ion|ing|inco|inter|ink")
print(change.sub("X", words))
"plXk XcomXg tX wXer X cautX sentient"

# Correct output
change2 = re.compile(r"i(nt|n|on|ng|nco|nter|nk)+?")
print(change2.sub("X", words))
# "plX XmX tX wX X cautX sentient"
# change2 = re.compile(r'in(ter|co|t|g|k)?|ion')

# For the given greedy quantifiers, what would be the equivalent form using the {m,n} representation?

# ? is same as {0,1} is same as {,1}
# * is same as {0,}
# + is same as {1,}

# (a*|b*) is same as (a|b)* — True or False?
print(re.sub(r"(a*|b*)", "X", "babble"))
# XXXXXXlXeX
print(re.sub(r"(a|b)*", "X", "babble"))
# XXlXeX

# For the given input strings, remove everything from the first occurrence of "test" (irrespective of case) till the end of the string, provided "test" isn't at the end of the string.
s1 = "this is a Test"
s2 = "always test your RE for corner cases"
s3 = "a TEST of skill tests?"

pat = re.compile(r"test.+", flags=re.I)

print(pat.sub("", s1))
# this is a Test
print(pat.sub("", s2))
# always
print(pat.sub("", s3))
# a

# For the input list words, filter all elements starting with "s" and containing "e" and "t" in any order.
words = ["sequoia", "subtle", "exhibit", "a set", "sets", "tests", "site"]

print([w for w in words if re.fullmatch(r"\bs.*(e+|t+)", w)])
# ["subtle", "sets", "site"]
# [w for w in words if re.search(r'\As.*(e.*t|t.*e)', w)]

# For the input list words, remove all elements having less than 6 characters.
words = ["sequoia", "subtle", "exhibit", "asset", "sets", "tests", "site"]
print([w for w in words if len(re.sub(r"\A.{0,5}", "", w)) != 0])
# ['sequoia', 'subtle', 'exhibit']
# [w for w in words if re.search(r'.{6,}', w)]

# For the input list words, filter all elements starting with s or t and having a maximum of 6 characters.
words = ["sequoia", "subtle", "exhibit", "asset", "sets", "t set", "site"]
print([w for w in words if len(re.sub(r"(s|t).{,5}", "", w)) == 0])
# ['subtle', 'sets', 't set', 'site']
# print([w for w in words if re.fullmatch(r"(s|t).{,5}", w)])

# Can you reason out why this code results in the output shown? The aim was to remove all <characters> patterns but not the <> ones.
ip = "a<apple> 1<> b<bye> 2<> c<cat>"
print(re.sub(r"<.+?>", "", ip))
# "a 1 2" (actual output)
# 'a 1<> b 2<> c' (expected output)

# Use re.split() to get the output as shown below for given input strings.
s1 = "go there  //   'this // that'"
s2 = "a//b // c//d e//f // 4//5"
s3 = "42// hi//bye//see // carefully"

pat = re.compile(r" {2,}// {2,}")

print(pat.split(s1))
# ['go there', ''this // that'']
print(pat.split(s2))
# ['a//b', 'c//d e//f // 4//5']
print(pat.split(s3))
# ['42// hi//bye//see', 'carefully']

# pat = re.compile(r' +// +')
# pat.split(s1, maxsplit=1)
# pat.split(s2, maxsplit=1)
# pat.split(s3, maxsplit=1)

# Modify the given regular expression such that it gives the expected results.

s1 = "appleabcabcabcapricot"
s2 = "bananabcabcabcdelicious"
pat = re.compile(r'(abc)+a')
print(bool(pat.search(s1)))
# True
print(bool(pat.search(s2)))
# True

# expected output
# 'abc' shouldn't be considered when trying to match 'a' at the end
pat = re.compile(r'(abc)++a')
print(bool(pat.search(s1)))
# True
print(bool(pat.search(s2)))
# False

# Modify the given regular expression such that it gives the expected result.

cast = 'dragon-unicorn--centaur---mage----healer'
c = '-'

# wrong output
print(re.sub(rf'{c}{3,}', c, cast))
# 'dragon-unicorn--centaur---mage----healer'

# expected output
print(re.sub(rf'{c}{{3,}}', c, cast))
# 'dragon-unicorn--centaur-mage-healer'