
#2762
#medium

#You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

#Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
#Return the total number of continuous subarrays.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [5,4,2,4]
#Output: 8
#Continuous subarray of size 1: [5], [4], [2], [4].
#Continuous subarray of size 2: [5,4], [4,2], [2,4].
#Continuous subarray of size 3: [4,2,4].
#Thereare no subarrys of size 4.
#Total continuous subarrays = 4 + 3 + 1 = 8.
#It can be shown that there are no more continuous subarrays.


#my incorrect solution that passed 2129/2135 test cases:

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        res = 0
        myset = set()
        for r in range(len(nums)):
            windowset = set(nums[l: r + 1])
            while max(windowset) - min(windowset) > 2 and l < r:
                windowset = set(nums[l + 1: r + 1])
                l += 1
            res += (r - l + 1)
        return res

#correct python3 solution (could not solve):

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        res = 0
        window = SortedList()
        for r in range(len(nums)):
            window.add(nums[r])
            while window[-1] - window[0] > 2:
                window.remove(nums[l])
                l += 1
            res += (r - l + 1)
        return res
