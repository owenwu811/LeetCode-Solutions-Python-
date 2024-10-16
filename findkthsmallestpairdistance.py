

#719
#Hard


#The distance of a pair of integers a and b is defined as the absolute difference between a and b.

#Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

#Example 1:

#Input: nums = [1,3,1], k = 1
#Output: 0
#Explanation: Here are all the pairs:
#(1,3) -> 2
#(1,1) -> 0
#(3,1) -> 2
#Then the 1st smallest distance pair is (1,1), and its distance is 0.


#correct python3 solution:

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(dist):
            #count total number of pairs with difference less than or equal to mid - run a sliding window to shrink it if it's not less than or equal to mid since we already know we are sorted
            l = 0
            res = 0
            for r in range(len(nums)):
                while (nums[r] - nums[l]) > dist:
                    l += 1
                res += (r - l) #not + 1 because we want pairs, not all subarrays!
            return res



        nums.sort() #we need to sort to ensure our binary search works
        l, r = 0, max(nums) #max(nums), not len(nums) - 1!
        while l < r:
            mid = (l + r) // 2
            pairs = helper(mid)
            if pairs >= k:
                r = mid 
            else:
                l = mid + 1
        return r
