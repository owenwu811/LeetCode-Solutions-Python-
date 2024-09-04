
#414
#easy
#35% acceptance rate


#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

#Example 1:

#Input: nums = [3,2,1]
#Output: 1
#Explanation:
#The first distinct maximum is 3.
#The second distinct maximum is 2.
#The third distinct maximum is 1.


#my own solution using python3:

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        myset = set()
        for n in nums:
            if n not in myset:
                myset.add(n)
        myheap = []
        for s in myset:
            heapq.heappush(myheap, -s)
        k = 3
        if len(myheap) < k:
            return max(nums)
        a = 0
        while k > 0:
            a = -1 * heapq.heappop(myheap)
            k -= 1
        return a
