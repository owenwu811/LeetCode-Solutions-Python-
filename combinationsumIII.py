#Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

#Only numbers 1 through 9 are used.
#Each number is used at most once.
#Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

#Example 1:

#Input: k = 3, n = 7
#Output: [[1,2,4]]
#Explanation:
#1 + 2 + 4 = 7
#There are no other valid combinations.


#my own solution using Python3:

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def f(cur, val):
            if sum(cur) > n:
                return
            if len(cur) == k and sum(cur) == n:
                res.append(cur.copy())
                return
            if val > 9:
                return
            cur.append(val)
            f(cur, val + 1)
            cur.pop()
            f(cur, val + 1)
        f([], 1)
        return res
        
