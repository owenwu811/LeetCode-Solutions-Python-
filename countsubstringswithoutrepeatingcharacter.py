
#2743
#medium

#You are given a string s consisting only of lowercase English letters. We call a substring special if it contains no character which has occurred at least twice (in other words, it does not contain a repeating character). Your task is to count the number of special substrings. For example, in the string "pop", the substring "po" is a special substring, however, "pop" is not special (since 'p' has occurred twice).

#Return the number of special substrings.

#A substring is a contiguous sequence of characters within a string. For example, "abc" is a substring of "abcd", but "acd" is not.

#Input: s = "abcd"
#Output: 10
#Explanation: Since each character occurs once, every substring is a special substring. We have 4 substrings of length one, 3 of length two, 2 of length three, and 1 substring of length four. So overall there are 4 + 3 + 2 + 1 = 10 special substrings.


#my own solution using python3:

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        window = deque()
        for r in range(len(s)):
            window.append(s[r])
            while len(window) != len(set(window)):
                window.popleft()
                l += 1
            res += (r - l + 1)
        return res
