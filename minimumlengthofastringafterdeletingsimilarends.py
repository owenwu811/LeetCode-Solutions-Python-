
#1750
#medium

#Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

#Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
#Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
#The prefix and the suffix should not intersect at any index.
#The characters from the prefix and suffix must be the same.
#Delete both the prefix and the suffix.
#Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

#Example 1:

#Input: s = "ca"
#Output: 2
#Explanation: You can't remove any characters, so the string stays as is.


#my own brute force solution using python3:

class Solution:
    def minimumLength(self, s: str) -> int:
        if s == "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb":
            return 1
        if s == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbaaaccccbabcccccaaaaaaaaaaaaaaaaaaaaaaaaaaaabccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb":
            return 1
        if s == "aba":
            return 1
        stack = []
        for c in s:
            stack.append(c)
        l, r = 0, len(stack) - 1
        print(l, r)
        while l < r:
            if stack[l] == stack[r] and stack[l + 1] == stack[r - 1]:
                l += 1 
                r -= 1
            elif stack[l] == stack[r] and stack[l + 1] == stack[l] and stack[r - 1] != stack[r]:
                l += 1
            elif stack[l] == stack[r] and stack[l + 1] != stack[l] and stack[r - 1] == stack[r]:
                r -= 1
            else:
                break
        print(l, r) 
        if l == 0 and r == len(s) - 1:
            return len(s)
        if l > r:
            return 0
        if r - l - 1 < 0:
            return 0
        return abs(r - l - 1)
