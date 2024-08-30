
#medium
#58.5% acceptance rate
#1695

#You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

#Return the maximum score you can get by erasing exactly one subarray.

#An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


#my own solution using python3:

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        subarraysum = 0
        tmp = set()
        l = 0
        for r in range(len(nums)):
            while nums[r] in tmp:
                tmp.remove(nums[l])
                l += 1
            tmp.add(nums[r])
            res = max(res, sum(tmp))
        return res
