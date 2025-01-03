
#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#[4,5,6,7,0,1,2] if it was rotated 4 times.
#[0,1,2,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

#Given the sorted rotated array nums of unique elements, return the minimum element of this array.

#You must write an algorithm that runs in O(log n) time.



#my solution - python3:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == min(nums):
                return nums[mid]
            elif nums[mid] < min(nums):
                l = mid + 1
            else:
                r = mid - 1

#5/15/24 refresher:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = min(nums)
        for i, j in enumerate(nums):
            if j == res:
                return j


#10/24/24 refresher (another solution):

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
