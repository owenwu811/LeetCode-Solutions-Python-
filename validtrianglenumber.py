

#611
#medium


#array that can make triangles if we take them as side lengths of a triangle.

 

#Example 1:

#Input: nums = [2,2,3,4]
#Output: 3
#Explanation: Valid combinations are: 
#2,3,4 (using the first 2)
#2,3,4 (using the second 2)
#2,2,3
#Example 2:

#Input: nums = [4,2,3,4]
#Output: 4


#correct python3 solution: - could not solve, so need to revisit

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res
