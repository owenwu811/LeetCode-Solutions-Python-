#35. Search Insert Position
#Easy
#13.8K
#605
#Companies
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

 

#Example 1:

#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:

#Input: nums = [1,3,5,6], target = 2
#Output: 1
#Example 3:

#Input: nums = [1,3,5,6], target = 7
#Output: 4
 

#Constraints:

#1 <= nums.length <= 104
#-104 <= nums[i] <= 104
#nums contains distinct values sorted in ascending order.
#-104 <= target <= 104

#my own solution using python3 on 2/9/25:

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)



#the trick to this problem is that the input list is already sorted, so use binary search to start from the middle of the list so we don't have to check every single value in the list
#this problem is identical to the problem called "FirstBadVersion"

#My Solution (Python):

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # this is actually better formatting since it reduces the space it takes to right the code, although it's a minor detail.
        while left <= right:
            #MID IS AN INTEGER THAT IS USED TO REPRESENT INDEXES SO WE CAN INDEX INTO A LIST IN PYTHON
            mid = (left + right) // 2 # since we just want the middle of the list, we do right + left in this case.  
            if target == nums[mid]: #we found a match, so return the index, aka the integer mid corresponding TO INDEXES, MID. 
                return mid
            elif target < nums[mid]: #the value we are looking for is smaller than the value when you plug the integer mid to get the index value and plug that index value into the list to spit out a value in the list, so since the value we are looking for, target, is smaller than the value we are on with mid, we know that our anwser will only be in the left half of the list now, so move the right pointer down to reflect this because we know that the anwser can't be in the original right half and isn't mid, so move right pointer down to one left of mid to dedraw our search space.
                right = mid - 1 #we want to move the pointers before setting mid, so we set the pointers in relation to mid, not mid in relation to the pointers
            else:
                left = mid + 1
        return left #we are returning left to cover the edge case where we only have one element in the list, and target is smaller than that one value in the list, so we want to return 0 - for example, if nums = [2] and target = 3, so we can't move right to the left of the left pointer, so we need to just return the left pointer, which will be either one index more or one index less than the single value in the list 

10/10/23 refresher(my solution):

#this pattern is identical to the problem called First Bad Version

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l 
