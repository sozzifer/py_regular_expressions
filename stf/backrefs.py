import re

######################
#   Capture groups   #
######################
"""
Similar to variables
\\N or \\g<N> where N is the required capture group
"""
# Remove square brackets if they are surrounding digit characters
# r"\1" denotes 1st capturing group, i.e. (\d+) (match one or more digits)
# Replace "[\d+]" with "\d+"
print(re.sub(r"\[(\d+)\]", r"\1", "[52] apples [and] [31] mangoes"))
# 52 apples [and] 31 mangoes

# Replace __ with _ and delete single _
# r"\1" denotes 1st capturing group, i.e. (_)? (match 0 or 1 _)
# Delete _ or replace __ with _
print(re.sub(r"(_)?_", r"\1", "_apple_   __123__   _banana_   cherry"))
# apple   _123_   banana   cherry

# Swap words separated by commas
# r"\1" and r"\2" are the 1st and 2nd capturing groups - both (\w+) here
print(re.sub(r"(\w+),(\w+)", r"\2,\1", "good,bad 42,24"))
# bad,good 24,42

# Use \g to incorporate digits into the replacement string without ambiguity
# r"\1" denotes 1st capturing group, i.e. (\d+) (match one or more digits)
# Replace "[\d+]" with "\d+5"
print(re.sub(r"\[(\d+)\]", r"\g<1>5", "[52] apples and [31] mangoes"))
# 525 apples and 315 mangoes

# Using octal escape
print(re.sub(r"\[(\d+)\]", r"\1\065", "[52] apples and [31] mangoes"))

# \g<0> represents the entire matched portion
# Enclose all matches in {}
print(re.sub(r"[a-z]+", r"{\g<0>}", "[52] apples and [31] mangoes"))
# [52] {apples} {and} [31] {mangoes}

# Insert entire matched portion into the replacement string
print(re.sub(r".+", r"Hi. \g<0>. Have a nice day.", "Hello world"))
# Hi. Hello world. Have a nice day.

# Append capture group match to end of string
# 1st capture group = "fork" ([^,]+)
# Entire matched portion = "fork,42,nice,3.14"
print(re.sub(r"\A([^,]+),.+", r"\g<0>,\1", "fork,42,nice,3.14"))
# fork,42,nice,3.14,fork

# Extract words with at least one consecutive repeated character
words = ["effort", "FLEE", "facade", "oddball", "rat", "tool", "a22b"]
# Matches any \w character and uses this in \1 to find consecutive repeated character
print([w for w in words if re.search(r"(\w)\1", w)])
# ['effort', 'FLEE', 'oddball', 'tool', 'a22b']

# Remove any number of consecutive duplicate words separated by a space
# Matches any word followed by a space and any number of repeats of the word, and replaces it with the word itself
# Note use of greedy quantifier ( \1)+ to match any number of repeats
print(re.sub(r"\b(\w+)( \1)+\b", r"\1", "aa a a a 42 f_1 f_1 f_13.14"))
# aa a 42 f_1 f_13.14

############################
#   Non-capturing groups   #
############################
"""
Define a non-capturing group with (?:<pattern>) when backrefs not required
"""
# Find all words that end in "st" or "in"
print(re.findall(r"\b\w*(?:st|in)\b", "cost akin sting more east run against"))
# ["cost", "akin", "east", "against"]

# Split on "hand" or "handy" or "handful"
print(re.split(r"hand(?:y|ful)?", "123hand42handy777handful500"))
# ['123', '42', '777', '500']

# Use non-capturing groups to simplify keeping track of capture group refs
print(re.sub(r"\A(([^,]+,){3})([^,]+)", r"\1(\3)", "1,2,3,4,5,6,7"))
print(re.sub(r"\A((?:[^,]+,){3})([^,]+)", r"\1(\2)", "1,2,3,4,5,6,7"))
# 1,2,3,(4),5,6,7
