
#medium
#60.3% acceptance rate
#1749

#You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

#Return the maximum absolute sum of any (possibly empty) subarray of nums.

#Note that abs(x) is defined as follows:

#If x is a negative integer, then abs(x) = -x.
#If x is a non-negative integer, then abs(x) = x.




#my own solution using python3 using hints and a tiny correction from discussion comment:

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        subarraysum = 0
        maxsum = 0
        for n in nums:
            if subarraysum < 0:
                subarraysum = 0
            subarraysum += n
            maxsum = max(maxsum, subarraysum)
        subarraysum = 0
        minsum = 0
        for n in nums:
            if subarraysum > 0:
                subarraysum = 0
            subarraysum += n
            minsum = min(minsum, subarraysum)
        return max(maxsum, abs(minsum))
        
