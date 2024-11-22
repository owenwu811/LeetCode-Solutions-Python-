

#254
#medium

#Numbers can be regarded as the product of their factors.

#For example, 8 = 2 x 2 x 2 = 2 x 4.
#Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

#Note that the factors should be in the range [2, n - 1].

 

#Example 1:

#Input: n = 1
#Output: []
#Example 2:

#Input: n = 12
#Output: [[2,6],[3,4],[2,2,3]]
#Example 3:

#Input: n = 37
#Output: []

#my own solution using python3:

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        tmp = []
        for i in range(2, n):
            if n % i == 0:
                tmp.append(i)
        print(tmp)
        self.h = []
        self.res = []
        def f(cur, i):
            if i >= len(tmp) or math.prod(self.h) >= n:
                if math.prod(self.h) == n:
                    self.res.append(self.h.copy())
                return
            self.h.append(cur[i])
            f(cur, i)
            self.h.pop()
            f(cur, i + 1)
        f(tmp, 0)
        print(self.res)
        if len(self.res) == 1 and not self.res[0]:
            return []
        return self.res
