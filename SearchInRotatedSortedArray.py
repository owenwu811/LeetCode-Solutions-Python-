#33. Search in Rotated Sorted Array
#Medium
#24.6K
#1.4K
#Companies
#There is an integer array nums sorted in ascending order (with distinct values).

#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

#You must write an algorithm with O(log n) runtime complexity.

 

#Example 1:

#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
#Example 2:

#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1
#Example 3:

#Input: nums = [1], target = 0
#Output: -1
 

#Constraints:

#1 <= nums.length <= 5000
#-104 <= nums[i] <= 104
#All values of nums are unique.
#nums is an ascending array that is possibly rotated.
#-104 <= target <= 104
#Accepted
#2.4M
#Submissions
#5.9M
#Acceptance Rate
#40.1%




#My Solution ( 10/22/23 - python):

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        myset = set()
        #if target == 0: #I figured that we actually don't need this
        #    return nums[0]
        for i in range(len(nums)): # i is an index
            myset.add(nums[i]) 
            if nums[i] == target: #nums[i] is a value while target is an index
                return i 
        if target not in myset:
            return -1

#My even better Solution (10/22/23 - Python) - since the problem states that every number is unique, we don't even need the set:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #myset = set()
        #if target == 0: 
        #    return nums[0]
        for i in range(len(nums)): # i is an index
            #myset.add(nums[i]) 
            if nums[i] == target: #nums[i] is a value while target is an index
                return i 
        #if target not in myset:
        return -1

#2/25/24:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, j in enumerate(nums):
            if j == target:
                return i
        return -1

#3/17/24:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for x, y in enumerate(nums):
            if y == target:
                return x
        return -1

#4/21/24 refresher:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, j in enumerate(nums):
            if j == target:
                return i
        return -1


#my own solution using python3 on 10/19/24 with binary search:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        orig = nums.copy()
        nums.sort()
        print(orig)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return orig.index(target)
            elif nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        
