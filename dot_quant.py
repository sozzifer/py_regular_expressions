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
