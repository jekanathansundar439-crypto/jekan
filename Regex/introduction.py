# Regex
# Regex (Regular Expression) is a pattern used to search, find, split, or replace text in a string.
# 👉Regex (Regular Expression) na oru pattern use panni string-la irukkura
#   text-a search, find, split, illa replace panna use pannura technique.
# import re
# re = Regular Expression module.

# There are four methods in regex module:
# split()
# search()
# findall()
# sub()

# split()
# split() divides a string into multiple parts and returns a list.
# 👉split() string-a space, comma, etc. irukkura idathula pirichu list-a maathum.         
import re
string = "Hello welcome to Python"
print(re.split("\s" , string))

# search()
# search() looks for a pattern in a string and returns the first match.
# 👉search() string-la word irukka-nu check pannum.
import re
string = "Hello Python"
ans = re.search("Python", string)
print(ans.start())

# findall()
# Returns all occurrences of a pattern.
# 👉findall() pattern match aana ella values-um list-la return pannum.
import re
string = "Hello welcome"
print(re.findall("o", string))

# sub()
# Replaces matched text with another text.
# 👉sub() old word-a replace panni new word podum
import re
string = "I love java"
print(re.sub("java", "python", string))

# Special Symbols
# | Symbol | Meaning                    |
# | ------ | -------------------------- |
# | `\s`   | Space                      |
# | `\d`   | Digit (0-9)                |
# | `\w`   | Letter, number, underscore |
# | `.`    | Any character              |
# | `^`    | Starts with                |
# | `$`    | Ends with                  |