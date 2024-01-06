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
        
