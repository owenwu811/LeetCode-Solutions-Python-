#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

#Example 1:

#Input: s = "leetcode"
#Output: 0


#python3 solution:

class Solution:
    def firstUniqChar(self, s: str) -> int: 
        for i in s:
            if s.count(i)==1: #this will catch the earliest one since we loop from left to right
                return s.index(i)
        else:
            return -1
            
        
