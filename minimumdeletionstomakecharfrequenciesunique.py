
#1647


#A string s is called good if there are no two different characters in s that have the same frequency.

#Given a string s, return the minimum number of characters you need to delete to make s good.

#The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.




#correct python3 solution:


class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(s)
        res = 0
        seen = set()
        for i, n in d.items():
            while n > 0 and n in seen:
                res += 1
                n -= 1
            seen.add(n)
        return res
