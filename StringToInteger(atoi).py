

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
