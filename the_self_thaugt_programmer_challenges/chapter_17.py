## 1 ##

""" Write a regular expression that will be matched to the word 'Dutch' from the
text in the zen.txt file"""

import re

with open('zen.txt', 'r') as f:
    lines = f.read()

matches = re.findall("Dutch", lines, re.IGNORECASE)

print(matches)


## 2 ##

""" Write a regular expression that returns all digits from the string 'Arizona
479, 501, 870. California 209, 213, 650'"""

import re

text = "Arizona 479, 501, 870. California 209, 213, 650."

m = re.findall("\d", text, re.IGNORECASE)

print(m)


## 3 ##

""" Write a regular expression that will find words starting with any letter 
followed by two letters 'o'. Then use Python's 're' module to find such words
in the string 'Orienteering around the city zoo.'"""

import re

text = 'Orienteering around the city zoo.'

m = re.findall('.oo', text, re.IGNORECASE)

print(m)
