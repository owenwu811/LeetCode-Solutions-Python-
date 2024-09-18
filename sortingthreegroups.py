
#2826
#medium
#42.3% acceptance rate

#You are given an integer array nums. Each element in nums is 1, 2 or 3. In each operation, you can remove an element from nums. Return the minimum number of operations to make nums non-decreasing.


#my own solution using python3 after taking hint from discussion section about length of input - LIS problem:


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] <= nums[i]:
                    res[j] = max(res[j], 1 + res[i])
        return len(nums) - max(res)
