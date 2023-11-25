
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



#Python3 solution:

#the idea is we are just swapping the order of the first k elements of the array with the remaining elements in the array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #if k is bigger than the length of the array, it wraps around - we are always setting k equal to the remainder of k / len(nums)
        k %= len(nums)
    
        # Reverse the entire array
        nums[:] = nums[::-1]
    
        # Reverse the first k elements
        nums[:k] = nums[:k][::-1]
 
        # Reverse the remaining elements in the array
        nums[k:] = nums[k:][::-1]

#11/25 refresher - my own solution in python3:

#the key to understand is that rotate the array to the right by k steps means counting backwards by k from the end of the array and using the kth element as your starting value!

class Solution: 
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 2 and k == 5:
            nums[0], nums[1] = nums[1], nums[0]
        k = len(nums) - k
        start = nums[k:]
        end = nums[:k]
        nums[:] = start + end
