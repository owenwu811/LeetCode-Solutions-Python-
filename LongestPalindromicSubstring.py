#5. Longest Palindromic Substring
#Medium
#25.8K
#1.5K
#Companies
#Given a string s, return the longest 
#palindromic
 
#substring
# in s.

 

#Example 1:

#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#Example 2:

#Input: s = "cbbd"
#Output: "bb"
 

#Constraints:

#1 <= s.length <= 1000
#s consist of only digits and English letters.


#My Solution (Python):

#We are expanding outwards from the center by comparing left and right values. If left and right values match, we keep expanding outwards until characters either 1. no longer match or 2. reach the boundaries of the string

class Solution(object):
    def longestPalindrome(self, s):
        def helper(left, right): #helper function keeps track of the longest palindrome we have found so far
            while (left >= 0 and right < len(s) and s[left] == s[right]): #boundary checks to ensure left dosen't go out of bounds to the left side of the string and right dosen't go out of bounds to the right side of the string
                left -= 1
                right += 1
            return s[left + 1: right] #ensures that the character at index left is not included in the substring because it is the character that caused the loop to exit and no longer satisfies the palindrome condition. By excluding the character at index left, the returned substring represents the longest palindrome substring without including the expanding character.        
        result = "" #initializes result as an empty string to set an initial value for result before the loop starts. since no palindromic substring has been found yet, result is, initially, set to an empty substring. As the loop progresses and palindromic substrings are found, result value will be updated to store the longest palindromic substring found up to that point
        for i in range(len(s)):
            test = helper(i, i) #single character as center aka s is an odd number of characters
            if len(test) > len(result): #result keeps track of the longest palindromic substring found so far, so if test is greater than result, result updates to test to store the new longest palindromic substring so far
                result = test
            test = helper(i, i + 1) #two adjacent characters as center aka s is an even number of characters
            if len(test) > len(result):
                result = test
        
        return result #at the end, result will contain the longest palindromic substring found in the given string s



#1/3/24 refresher:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r, s):
            #making sure we are inside the string with the two pointers and that the characters from both pointers are the same. If so, we expand outward forever until one of these conditions is broken to find an even longer palindromic substring. 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            #if the while loop is broken meaning we are outside the string or one side is nor equal to the other side character, then we need to step backwards and include the substring that was valid by moving left forward one and right backward one from the point left and right were at when this while loop was violated and return that to be compared
            return s[l + 1: r]
        res = ""
        for char in range(len(s)):
            first = f(char, char, s)
            if len(first) > len(res):
                res = first
            second = f(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res



#1/6/24 refresher:

class Solution:
    def longestPalindrome(self, s):
        def dfs(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        #the question asks for the longest palindromic substring itself, so either one works if both are a tie. It dosen't ask for the length of the longest palindomic substring. 
        res = ""
        for char in range(len(s)):
            first = dfs(char, char, s)
            if len(first) > len(res):
                res = first
            second = dfs(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res


#1/16/24 refresher:

class Solution:
    def longestPalindrome(self, s):
        def dfs(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #expanding outwad to find a longer palindrome window than before if we are in bounds and the letters both pointers are pointing to are the same (think reverse staircase)
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ""
        #remember that a palindrome can occur starting anywhere in the string, not just from the middle!!!!! 
        for char in range(len(s)):
            first = dfs(char, char, s)
            if len(first) > len(res):
                res = first
            second = dfs(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res

#1/18/24 refresher:

class Solution:
    def longestPalindrome(self, s):
        def dfs(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        res = ""
        for char in range(len(s)):
            first = dfs(char, char, s)
            if len(first) > len(res):
                res = first
            second = dfs(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res

#2/4/24 refresher practice:

class Solution:
    def longestPalindrome(self, s):
        #we want the longest substring itself, so a string is the return type and not an integer
        def expandfromanywhere(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            #when the while loop evaluates to False, we terminate the while loop, and we return the last VALID substring back to either same or different
            return s[l + 1: r]
        res = ""
        for char in range(len(s)):
            same = expandfromanywhere(char, char, s)
            if len(same) > len(res):
                res = same
            different = expandfromanywhere(char, char + 1, s)
            if len(different) > len(res):
                res = different
        return res


#2/20/24:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ""
        for char in range(len(s)):
            first = f(char, char, s)
            if len(first) > len(res):
                res = first
            second = f(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res

#2/26/24:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 #keep expanding outward because we are looking for a longer palindromic substring
                r += 1
            return s[l + 1: r]
      


        res = ""
        for char in range(len(s)):
            first = f(char, char, s) #palindromic substrings can start anywhere in the string, not just in the middle, so expand one and two units, inching forward
            if len(first) > len(res):
                res = first
            second = f(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res


#3/9/24:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]: #while, not if!!!!!
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        for char in range(len(s)):
            first = f(char, char, s) 
            if len(first) > len(res):
                res = first
            second = f(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res

#3/15/24:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        res = ""
        for char in range(len(s)):
            first = f(char, char, s)
            if len(first) > len(res):
                res = first
            second = f(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res


#3/24/24:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        for char in range(len(s)):
            first = f(char, char, s)
            if len(first) > len(res): #don't forget len() because you can't just compare two strings directly without len!
                res = first
            second = f(char, char + 1, s)
            if len(second) > len(res):
                res = second
        return res

#4/15/24:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        

        res = ""
        for i in range(len(s)):
            first = f(i, i, s)
            if len(first) > len(res):
                res = first
            second = f(i, i + 1, s)
            if len(second) > len(res):
                res = second
        return res

#5/11/24 refresher:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]


        res = ""
        for i in range(len(s)):
            first = f(i, i, s)
            if len(first) > len(res):
                res = first
            second = f(i, i + 1, s)
            if len(second) > len(res):
                res = second
        return res

#6/5/24 review:

class Solution:
    def longestPalindrome(self, s):
        def f(l, r , s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        for i in range(len(s)):
            first = f(i, i, s)
            if len(first) > len(res):
                res = first
            second = f(i, i + 1, s)
            if len(second) > len(res):
                res = second
        return res

#7/14/24 refresher:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]


        res = ""
        for i in range(len(s)):
            first = f(i, i)
            if len(first) > len(res):
                res = first
            second = f(i, i + 1)
            if len(second) > len(res):
                res = second
        return res

#9/8/24 review:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l, r, s): 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        for i in range(len(s)):
            first = f(i, i, s)
            if len(first) > len(res):
                res = first
            second = f(i, i + 1, s)
            if len(second) > len(res):
                res = second
        return res


#10/18/24 review:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        for i in range(len(s)):
            first = f(i, i, s)
            if len(first) > len(res):
                res = first
            second = f(i, i + 1, s)
            if len(second) > len(res):
                res = second
        return res


#11/5/24 review (my own solution using python3):

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        maxlen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if substr == substr[::-1]:
                    res.append(substr)
                    maxlen = max(maxlen, len(substr))
        for r in res:
            if len(r) == maxlen:
                return r 
        return ""
