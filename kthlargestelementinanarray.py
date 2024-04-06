#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Can you solve it without sorting?



#nums = [3,2,1,5,6,4], k = 2 - output = 5

#my solution - python3:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        lookingfor = len(nums) - k 
        for i in range(len(nums) -1, -1, -1):
            if i == lookingfor:
                return nums[i]

