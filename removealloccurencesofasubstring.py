
#Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

#Find the leftmost occurrence of the substring part and remove it from s.
#Return s after removing all occurrences of part.

#A substring is a contiguous sequence of characters in a string.

#Input: s = "daabcbaabcbc", part = "abc"
#Output: "dab"
#Explanation: The following operations are done:
#- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
#- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
#- s = "dababc", remove "abc" starting at index 3, so s = "dab".
#Now s has no occurrences of "abc".



#my own solution using python3:

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            for i in range(len(s) - len(part) + 1):
                cur = s[i: i + len(part)]
                print(cur)
                if cur == part:
                    s = s.replace(cur, "", 1)
                    print(s)
        return s
            
