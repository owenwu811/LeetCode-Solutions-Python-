#Given a string s, partition s such that every 
#substring
# of the partition is a 
#palindrome
#. Return all possible palindrome partitioning of s.


#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]

#This question is part of the backtracking pattern in NeetCode 150

#python3 solution:

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def check(word):
            return word == word[::-1]

        def recursive(index, curr):
            if index == len(s):
                res.append(curr)
                return #backtracking means undoing aka popping from rear, which, in this case, means decrementing i from 2 to 1 and then executing inside the for loop again for the test case s = "aab" as s is of length 2
            for i in range(index, len(s)):
                if check(s[index: i+1]):
                    a = curr.copy()
                    a.append(s[index: i+1])
                    recursive(i+1, a)
        
        recursive(0, [])
        return res
