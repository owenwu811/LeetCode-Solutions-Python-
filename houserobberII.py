#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



#python3 solution:

class Solution:
    def rob(self, nums: List[int]) -> int:
        def house(nums):
            rob1,rob2=0,0
            for num in nums:
                temp=max(num+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        return max(house(nums[1:]),house(nums[:-1]),nums[0])
    #[1, 2, 3] > 3
    #[2, 3, 2] > 3
