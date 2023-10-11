#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Example 1:

#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.
#Example 2:

#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.

#Constraints:

#1 <= haystack.length, needle.length <= 104
#haystack and needle consist of only lowercase English characters.




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1): #gets called when we don't find a direct match aka goes moves to the right in haystack to compare again
            if haystack[i:i + len(needle)] == needle: #we found an exact match
                return i
        return -1

  #haystack = "sadbutsad", needle = "sad" - we would get for i in range(9 - 3 + 1) = for i in range(7), so i includes 0, 1, 2, 3, 4, 5, 6 - 6 represents the stopping point in haystack where, from that point on in haysack, it's the last valid chance that needlestack can fit
