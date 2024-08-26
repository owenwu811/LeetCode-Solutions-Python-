

#398
#medium

#Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

#Implement the Solution class:

#Solution(int[] nums) Initializes the object with the array nums.
#int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


#the correct solution using python3 (I was not able to solve):

class Solution:

    def __init__(self, nums: List[int]):
        self.n = nums

    def pick(self, target: int) -> int:
        while True:
            index = randint(0, len(self.n) - 1)
            if target == self.n[index]:
                return index
