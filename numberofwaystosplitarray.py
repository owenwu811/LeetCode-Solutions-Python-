

#my own solution that got time limit exceeded with 92/101 test cases passing:

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #[10,4,-8,7]
        res = 0
        for i in range(len(nums) - 1):
            if sum(nums[:i + 1]) >= sum(nums[i + 1:]):
                res += 1
        #if len(nums) == 4: return res - 1
        return res


#python3 solution:

#[10, 4, -8, 7]
# 0   1   2  3

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totsum = sum(nums)
        l, res = 0, 0
        for i in range(len(nums) - 1): #0, 1, 2
            l += nums[i] #0 + 10 = 10, 10 + 4 = 14, 14 - 8 = 6, 
            totsum -= nums[i] #13 - 10 = 3, 3 - 4 = -1, -1 -- 8 = 7,
            if l >= totsum: #10 >= 3, so + 1, 14 >= -1, so + 1, 6 >= 7, so don't increment
                res += 1
        return res
