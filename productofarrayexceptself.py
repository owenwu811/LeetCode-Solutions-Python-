#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

#[1, 2, 3, 4]


#my solution - python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        result = [0] * len(nums)
        for i in range(len(nums)): #[1, 1, 2, 6] - no room for 24
            result[i] = prefixn
            prefixn *= nums[i]
        for i in range(len(nums) -1, -1, -1): #[24, 12, 8, 6] - multiplied by prefix array 
            result[i] *= postfixn
            postfixn *= nums[i]
        return result
            
