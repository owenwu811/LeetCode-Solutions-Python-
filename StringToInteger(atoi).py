

#Input: s = "42"

#Output: 42

#Input: s = " -042"

#Output: -42

#Input: s = "1337c0d3"

#Output: 1337

#python3 solution:

class Solution:
    def myAtoi(self, s):
        match = re.match(r'^\s*([+-]?\d+)', s)
        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        return 0

#6/12/24 review:

class Solution:
    def myAtoi(self, s):
        match = re.match(r'^\s*([+-]?\d+)', s)
        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        return 0

#6/13/24 review:

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', s)
        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        return 0

#6/16/24 refresher:

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', s)
        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        return 0

#6/24/24 refresher:

class Solution:
    def myAtoi(self, s: str) -> int:
       #\s matches any whitespace character (spaces, tabs, etc.).
#* is a quantifier that means "zero or more occurrences".
#Together, \s* matches zero or more whitespace characters at the beginning of the string. This allows the regex to be flexible about the amount of leading whitespace before the number.
        #([+-]?\d+) is a capturing group that matches:
#[+-]?: An optional sign (+ or -).
#\d+: One or more digits (0-9).
#+ here is a quantifier that means "one or more occurrences".
#Together, ([+-]?\d+) matches one or more digits optionally preceded by a sign (+ or -). This ensures that the regex matches valid numbers (with optional signs) that follow any initial whitespace.
        match = re.match(r'^\s*([+-]?\d+)', s) #match will contain a Match object if the regex pattern matches any part of s, or None if no match is found.
        if match:
            integer = int(match.group()) #match.group() only includes the part of the string that was matched
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        return 0
        

#7/29/24 refresher:

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', s) #always us \ and not / symbol! - use re.match since we are matching characters that fit a criteria, not subsituting anything!
        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        return 0

        
