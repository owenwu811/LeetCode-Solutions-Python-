#Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
#the smallest in lexicographical order
# among all possible results.

 

#Example 1:

#Input: s = "bcabc"
#Output: "abc"
#Example 2:

#Input: s = "cbacdcbc"
#Output: "acdb"




#correct python3 solution using monotonic stack:

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occur = {c: i for i, c in enumerate(s)} #{'b': 3, 'c': 4, 'a': 2}
        for i, c in enumerate(s):
            #print stack - [], ['b'], ['b', 'c'], ['a'], ['a', 'b']
            if c not in seen: #if already seen, we don't want duplicates, so we just skip and keep looping onto next char in input
                while stack and c < stack[-1] and i < last_occur[stack[-1]]: 
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)


