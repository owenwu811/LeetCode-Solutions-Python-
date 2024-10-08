
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
        for i, n in d.items(): #iterating through each key, value pair in the d dictionary using the .items() method!
            #i = the key while n = the value 
            while n > 0 and n in seen:
                res += 1
                n -= 1 #changes the actual value itself in d.items() dictionary Counter, which is n 
            seen.add(n) #we add n to seen because if we hit 0 as frequency, which is the value of the dictionary (aka n), the character is now not seen before is the idea 
        return res


#why are we decrementing until we hit 0?

#Why does this ensure the minimum number of deletions?
#Decrementing by 1 at each step is the smallest possible change you can make to reduce the frequency (we want to delete the smallest number of characters possible in the while loop meaning we want to increment res the fewest number of times possible). By making the minimal reduction needed to achieve a unique frequency, you ensure that you delete the fewest number of characters.
#If you try to make bigger jumps (e.g., directly jumping to 0 or skipping frequencies), you would likely end up deleting more characters than necessary.- the idea in this problem is to delete the fewest number of characters to make s good!
#Once a frequency is reduced to 0, it means the character has been completely removed, which is the worst-case scenario but necessary if no smaller unique frequency is available.


#9/19/24 review:

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        seen = set()
        for i, n in freq.items():
            while n > 0 and n in seen:
                res += 1
                n -= 1
            seen.add(n)
        return res

#9/25/24 review (was able to solve):

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        seen = set()
        res = 0
        for i, n in freq.items():
            while n > 0 and n in seen:
                n -= 1
                res += 1
            seen.add(n)
        return res
