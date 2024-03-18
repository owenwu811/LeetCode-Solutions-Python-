#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

#There is only one repeated number in nums, return this repeated number.

#You must solve the problem without modifying the array nums and uses only constant extra space.

# input: nums = [1,3,4,2,2]
# output: 2


#my solution - python3:

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()
        for number in nums:
            if number not in myset:
                myset.add(number)
            else:
                return number
