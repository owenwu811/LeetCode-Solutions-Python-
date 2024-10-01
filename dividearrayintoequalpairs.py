
#2206
#easy

#You are given an integer array nums consisting of 2 * n integers.

#You need to divide nums into n pairs such that:

#Each element belongs to exactly one pair.
#The elements present in a pair are equal.
#Return true if nums can be divided into n pairs, otherwise return false.



#my own solution using python3:

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for k in d:
            if d[k] % 2 == 0:
                continue
            else:
                return False
        return True
