#266
#easy


#Given a string s, return true if a permutation of the string could form a 
#palindrome
# and false otherwise.

 

#Example 1:

#Input: s = "code"
#Output: false
#Example 2:

#Input: s = "aab"
#Output: true
#Example 3:

#Input: s = "carerac"
#Output: true



#my own solution using python3:

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        oddallowance = 0
        for i, n in c.items():
            if n % 2 != 0:
                oddallowance += 1
        return oddallowance < 2
