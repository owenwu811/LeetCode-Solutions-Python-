
#medium
#384

#Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

#Implement the Solution class:

#Solution(int[] nums) Initializes the object with the integer array nums.
#int[] reset() Resets the array to its original configuration and returns it.
#int[] shuffle() Returns a random shuffling of the array.


#python3 solution:

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums

    def reset(self) -> List[int]:
        self.nums = self.original
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled=list(self.nums)
        random.shuffle(shuffled)
       
        return shuffled
