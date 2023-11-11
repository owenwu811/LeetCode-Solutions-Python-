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
        for first in range(len(nums) - 3): #first pointer increments when second pointer is violating the len(nums) - 2 condition, meaning no more room for a 4th pointer to the right
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2): #second pointer increments when while third < fourth is false
                if second > first + 1 and nums[second] == nums[second - 1]: #note that nums[second] == num[first] won't work because second > first + 1 ensures that second is ATLEAST TWO STEPS ahead of first, not one step
                    continue
                third, fourth = second + 1, len(nums) - 1 #note that third and fourth pointer values are set according to their relationship to first and second pointer; current third and fourh pointer values have no relationship to what the previous third and fourth pointer values were before
                while third < fourth: #we are reducing the problem into a two sum wih two pointer wih the 3rd and 4th pointer, so we need to make sure the third and fourth don't cross, and if they do cross, then go back to 2nd pointer
                    foursum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if foursum < target and third < fourth: # we are reducing the problem into essentially a two sum #with third and fourth pointer
                        third += 1
                    elif foursum > target and third < fourth:
                        fourth -= 1
                    else:
                        result.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third, fourth = third + 1, fourth - 1
                        while nums[third] == nums[third - 1] and third < fourth: #even after finding a valid quadruplet, because we just moved third and fourth pointers closer to one another, hence to new elements, we have to duplicate check again to ensure that these new elements are not a repeat of the outer third and fourth pointers that we just counted as a valid quadruplet. if these new inner third and fourth pointer values are a repeat, then move the corresponding pointer that was a repeat until third < fourth is not true 
                            third += 1
                        while nums[fourth] == nums[fourth + 1] and third < fourth: #if this is false, then we go back to while third < fourth check, and if that's false, then we increment second by hitting line 36, and if second dosen't make room for a 4th pointer, then we increment first pointer by hitting line 33. Note that fourth won't be out of bounds to the right because line 10 already decremented it when we found a valid quadruplet, and this while loop is inside of the else block
                            fourth -= 1
        return result
       
       
       #for first in range(len(nums) - 3) > this represents the number of iterations where first is pointing to a valid index and there is still room for a 4th pointer
       # 0  1  2. 3. 4. 5 
       #[1, 2, 3, 4, 5, 6]
       #for 0 in range(3) > len(nums) - 3 = 6 - 3 = 3
       #This means that first goes up to 0, 1, 2 inclusive
       # 0  1  2. 3  4  5
       #[1, 2, 3, 4, 5, 6]
        F   S. T. F
       # 0. 1. 2  3. 4. 5
       #[1, 2, 3, 4, 5, 6] > this is the last valid iteration for first pointer before fourth goes out of bounds, and notice how first is pointing to INDEX 2, so index 2 represents the last inclusive value for first in for 0 in range(3): aka 0, 1, 2
               F  S. T.  F
      
      
      #for second in range(first + 1, len(nums) - 2) > using the same example with [1, 2, 3, 4, 5, 6]

      #for second in range(first + 1, range(len) - 2)

      #for second in range(1, 6 - 2)

      #for second in range(1, 4)

      #for second in 1, 2, 3

     #0  1  2  3  4  5
     #[1, 2, 3, 4, 5, 6]
     #         F  S  T  F > last acceptable index value for second before no room for fourth


My Solution (8/1/23 refresher):

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for first in range(len(nums) - 3): #up to but not including the final value, so if first starts at 1, it includes up to and including index 2 if the the length is 6
            if first > 0 and nums[first] == nums[first - 1]: #duplicate, so continue onto next iteration of loop 
                continue
            for second in range(first + 1, len(nums) - 2): #must include first + 1 because second has to start exactly one space to the right of first and go up to but not including 4 - 2 = 2.
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third, fourth = second + 1, len(nums) - 1
                while third < fourth:
                    foursum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if foursum < target:
                        third += 1
                    elif foursum > target:
                        fourth -= 1
                    else:
                        result.append([nums[first], nums[second], nums[third], nums[fourth]]) #each valid quadruplet must be wrapped within an outer list to be valid as we are returning a list of lists
                        third, fourth = third + 1, fourth - 1
                        while nums[third] == nums[third - 1] and third < fourth:
                            third += 1
                        while nums[fourth] == nums[fourth + 1] and third < fourth:
                            fourth -= 1
        return result

#my solution - 11/10/23 refresher:

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for first in range(len(nums) - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2): #first + 1 means second pointer must start exactly one element in front of the first pointer
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third = second + 1
                fourth = len(nums) - 1
                while third < fourth:
                    foursum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if foursum < target:
                        third += 1
                    elif foursum > target:
                        fourth -= 1
                    else:
                        result.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1
                        while nums[third] == nums[third - 1] and third < fourth:
                            third += 1
                        while nums[fourth] == nums[fourth + 1] and third < fourth:
                            fourth -= 1
        return result
        
