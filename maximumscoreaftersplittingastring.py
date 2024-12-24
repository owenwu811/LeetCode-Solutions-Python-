#1422
#easy

#Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

#The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

#Example 1:

#Input: s = "011101"
#Output: 5 
#Explanation: 
#All possible ways of splitting s into two non-empty substrings are:
#left = "0" and right = "11101", score = 1 + 4 = 5 
#left = "01" and right = "1101", score = 1 + 3 = 4 
#left = "011" and right = "101", score = 1 + 2 = 3 
#left = "0111" and right = "01", score = 1 + 1 = 2 
#left = "01110" and right = "1", score = 2 + 1 = 3


#my own solution using python3:

class Solution:
    def maxScore(self, s: str) -> int:
        front = defaultdict(int)
        res = 0
        back = Counter(s)
        for i in range(len(s) - 1):
            front[s[i]] += 1
            back[s[i]] -= 1
            print(front, back)
            print(front["0"], back["1"])
            res = max(res, front["0"] + back["1"])
        return res
