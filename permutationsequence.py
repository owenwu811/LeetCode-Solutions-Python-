
#60
#hard


#Given n and k, return the kth permutation sequence.

 

#Example 1:

#Input: n = 3, k = 3
#Output: "213"


#my own solution using python3:

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        cur = ""
        for i in range(1, n + 1):
            cur += str(i)
        tmp = []
        for a in permutations(cur):
            tmp.append(a)
        return "".join(tmp[k - 1])
