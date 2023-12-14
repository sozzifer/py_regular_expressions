import re

#################
#   Backslash   #
#################
"""
To match metacharacters, prefix with \
"""
# Match "^"
print(bool(re.search(r"b^2", "a^2 + b^2 - c*3")))
# False
print(bool(re.search(r"b\^2", "a^2 + b^2 - c*3")))
# True

# Replace "(" or ")" with ""
print(re.sub(r"\(|\)", "", "(a*b) + c"))
# a*b + c

# Only use regex if normal string methods not feasible
eqn = "f*(a^b) - 3*(a^b)"
print(eqn.replace("(a^b)", "c"))
# f*c - 3*c

###################
#   re.escape()   #
###################
"""
re.escape() will automatically escape all metacharacters
"""
# Combine escaped strings with metacharacters
eqn = "f*(a^b) - 3*(a^b)"
expr = "(a^b)"
print(re.escape(expr))
# \(a\^b\)
# Replace "(a^b)" only at end of string
print(re.sub(re.escape(expr) + "\Z", "c", eqn))
# f*(a^b) - 3*c

# Joining escaped strings
terms = ["a_42", "(a^b)", "2|3"]

pat1 = re.compile("|".join(re.escape(s) for s in terms))
pat2 = re.compile("|".join(terms))
print(pat1.pattern)
# a_42|\(a\^b\)|2\|3
print(pat2.pattern)
# a_42|(a^b)|2|3

s = "ba_423 (a^b)c 2|3 a^b"
print(pat1.sub("X", s))
# bX3 Xc X a^b
# Replace "a_42" or "(a^b)" or "2|3"

print(pat2.sub("X", s))
# bXX (a^b)c X|X a^b
# Replace "a_42" or "2" or "3"
# "(a^b)" and "a^b" ignored

########################
#   Escape sequences   #
########################
"""
https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences
Only relevant in string literals, not raw strings
Compare r"\b" (word boundary) and "\b" (ASCII backspace)
"""
tabs = "a\tb\tc"
print(tabs)
print(re.sub(r"\t", ":", tabs))

newlines = "1\n2\n3"
print(newlines)
print(re.sub(r"\n", " ", newlines))

# Hexadecimal (\xNN)
# https://ascii.cl/

# \x20 = space
print(re.sub(r"\x20", "", "h e l l o"))
# hello

# \x7c = |
print(re.sub(r"2\x7c3", "5", "12|30"))
# 150
print(re.sub(r"2|3", "5", "12|30"))
# 15|50

#################
#   Exercises   #
#################

str1 = "(9-2)*5+qty/3-(9-2)*7"
str2 = "(qty+4)/2-(9-2)*5+pq/4"

print(re.sub(re.escape(r"(9-2)*"), "3", str1, count=1))
# 35+qty/3-(9-2)*7
print(re.sub(re.escape(r"(9-2)*"), "3", str2, count=1))
# (qty+4)/2-35+pq/4

s1 = r"2.3/(4)\|6 foo 5.3-(4)\|"
s2 = r"(4)\|42 - (4)\|3"
s3 = "two - (4)\\|\n"

pat = re.compile(r"\A\(4\)\\\||\(4\)\\\|\Z")
print(pat.pattern)
print(pat.sub("2", s1))
# 2.3/(4)\\|6 foo 5.3-2
print(pat.sub("2", s2))
# 242 - (4)\|3
print(pat.sub("2", s3))
# two - (4)\|

items = ["a.b", "3+n", r"x\y\z", "qty||price", "{n}"]
pat = re.compile("|".join(re.escape(i) for i in items))

print(pat.sub("X", "0a.bcd"))
# 0Xcd
print(pat.sub("X", "E{n}AMPLE"))
# EXAMPLE
print(pat.sub("X", r"43+n2 ax\y\ze"))
# 4X2 aXe

ip = "123\b456"
print(re.sub(r"\x08", " ", ip))
# 123 456

ip = r"th\er\e ar\e common asp\ects among th\e alt\ernations"
print(re.sub(r"\\e", "e", ip))
# there are common aspects among the alternations

ip = "3-(a^b)+2*(a^b)-(a/b)+3"
eqns = ["(a^b)", "(a/b)", "(a^b)+2"]
pat = re.compile("|".join(sorted((re.escape(e) for e in eqns), key=len, reverse=True)))
print(pat.sub("X", ip))
# 3-X*X-X+3
