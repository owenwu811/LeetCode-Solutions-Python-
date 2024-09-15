
#1492
#medium
#68.4% acceptance rate


#You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

#Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.


#my own solution using python3:

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        if len(res) < k:
            return -1
        return res[k - 1]
        print(res)
