
#2405

#medium

#Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

#Return the minimum number of substrings in such a partition.

#Note that each character should belong to exactly one substring in a partition.

 


#my own solution using python3 after looking at discuss section:

class Solution:
    def partitionString(self, s: str) -> int:
        if len(set(s)) == 1: return len(s)
        if len(set(s)) == len(s): return 1
        res = 1
        myset = set()
        for r in range(len(s)):
            if s[r] not in myset:
                myset.add(s[r])
            else:
                res += 1
                myset.clear()
                myset.add(s[r])
        return res
