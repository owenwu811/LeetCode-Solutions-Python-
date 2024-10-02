
#2085
#easy


#Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

#Example 1:

#Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
#Output: 2
#Explanation:
#- "leetcode" appears exactly once in each of the two arrays. We count this string.
#- "amazing" appears exactly once in each of the two arrays. We count this string.
#- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
#- "as" appears once in words1, but does not appear in words2. We do not count this string.
#Thus, there are 2 strings that appear exactly once in each of the two arrays.



#my own solution using python3:

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = 0
        for word in words1:
            if words1.count(word) == 1 and words2.count(word) == 1:
                res += 1
        return res
