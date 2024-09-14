
#1641
#medium


#Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

#A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

#Example 1:

#Input: n = 1
#Output: 5
#Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
#Example 2:

#Input: n = 2
#Output: 15
#Explanation: The 15 sorted strings that consist of vowels only are
#["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
#Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.


#my own solution using python3:

class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        self.res = []
        def backtrack(stack, i, n):
            if len(stack) == n:
                self.res.append(stack.copy())
                return
            if i == len(vowels) - 1:
                self.res.append(stack.copy())
                return
            stack.append(vowels[i])
            backtrack(stack, i, n)
            stack.pop()
            backtrack(stack, i + 1, n)
        backtrack([], 0, n)
        return len(self.res)
