Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

My Solution:


class Solution(object):
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        for first in range(len(nums) - 3): #index 0 to not including 1 if len(nums) == 4
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2): #index 1 to not including 2 if len(nums) == 4
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third = second + 1
                fourth = len(nums) - 1
                while third < fourth: #we are reducing the problem into a two sum wih two pointer wih the 3rd and 4th pointer, so we need to make sure the third and fourth don't cross, and if they do cross, then go back to 2nd pointer
                    foursum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if foursum < target and third < fourth: # we are reducing the problem into essentially a two sum #with third and fourth pointer
                        third += 1
                    elif foursum > target and third < fourth:
                        fourth -= 1
                    else:
                        result.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1
                        while nums[third] == nums[third - 1] and third < fourth: #duplicate checking 
                            third += 1
                        while nums[fourth] == nums[fourth + 1] and third < fourth:
                            fourth -= 1
        return result
