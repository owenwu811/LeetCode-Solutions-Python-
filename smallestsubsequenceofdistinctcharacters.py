
#1081
#medium

#Given a string s, return the 
#lexicographically smallest
#subsequence
# of s that contains all the distinct characters of s exactly once.


#my own solution using python3 after solving remove duplicate letters and seeing that this is the exact same problem:

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        last_occur = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occur[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)
