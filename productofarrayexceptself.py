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
            
#my solution - python3 - 12/17/23:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        res = [0] * len(nums) #create an empty array to declare it's length by filling it with zeros
        for number in range(len(nums)): 
            res[number] = prefixn #[1, 1, 2, 6]
            prefixn *= nums[number] # [1] [1*1] [1*1*2] [1*1*2*3]
        for number in range(len(nums) -1, -1, -1): 
            res[number] = postfixn * res[number] #[24, 12, 8, 6]
            postfixn *= nums[number] #[1 * 2 * 3 * 4] [1 * 3 * 4] [1 * 4 * 2] [6 * 1]
        return res

#12/25/23 refresher - my solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = 1
        backward = 1
        result = len(nums) * [0]
        for number in range(len(nums)):
            result[number] = forward
            forward *= nums[number]
        for number in range(len(nums)-1, -1, -1):
            result[number] *= backward
            backward *= nums[number]
        return result



#1/8/24 refresher - my solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        anwser = [0] * len(nums)
        prefixn = 1
        postfixn = 1
        for number in range(len(nums)):
            anwser[number] = prefixn
            prefixn *= nums[number]
        for number in range(len(nums)-1, -1, -1):
            anwser[number] *= postfixn
            postfixn *= nums[number]
        return anwser


#1/14 refresher - IMPORTANT INSIGHT

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prefixn, postfixn = 1, 1
        for forward in range(len(nums)):
            result[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            #result = [1, 1, 2, 6]
            #nums = [1, 2, 3, 4]
            #we want = [24, 12, 8, 6]
            #we don't get [24, 12, 12, 6] because result[2] = 2, and 2 * 4(postfixn) = 8. WE WANT POSTFIXN * RESULT[2] NOT POSTFIXN * NUMS[2] - POSTFIXN TIMES RESULT[2] NOT POSTFIXN TIMES NUMS[2] IS PLACED IN THE 2ND INDEX IN OUR FINAL LIST
            result[backward] = postfixn * result[backward]
            postfixn *= nums[backward]
        return result


#1/18/24 refresher:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        res = [1] * len(nums)
        for forward in range(len(nums)):
            res[forward] = prefixn 
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] = postfixn * res[backward]
            postfixn *= nums[backward]
        return res

#1/21/24 refresher practice solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        #we use 1 to fill in every place in our eventual to be output array because 0 times anything is always 0
        res = [1] * len(nums)
        for number in range(len(nums)):
            res[number] = prefixn
            prefixn *= nums[number]
        for number in range(len(nums) - 1, -1, -1):
            res[number] *= postfixn
            postfixn *= nums[number]
        return res
