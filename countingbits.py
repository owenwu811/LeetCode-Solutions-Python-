
#Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


#Input: n = 2
#Output: [0,1,1]
#Explanation:
#0 --> 0
#1 --> 1
#2 --> 10

#my own solution in python3:

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = bin(i).count('1')
            res.append(cnt)
        return res

#5/31/24 review (missed yesterday):

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = bin(i).count('1')
            res.append(cnt)
        return res

#6/8/24 refresher:

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = bin(i).count('1')
            res.append(cnt)
        return res

#7/17/24 review (missed a few days ago):

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = bin(i).count('1')
            res.append(cnt)
        return res
