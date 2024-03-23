
#Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

#You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.





#python3 solution:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=1 # i is set to 1 initially because that's the smallest number that could be the anwser. 1 is the smallest positive integer. if 1 is not missing from the array, then the smallest missing positive integer must be greater than 1. 
        for j in nums:
            if j<=0: #skip non positive numbers because we want the smallest positive number that is missing from the array, so negative numbers and zero are not relevant
                continue
            if i==j: #if the current element j is equal to the expected positive integer i, it means that i is inside of the array, so we increment i by 1 to check for the next positive integer that could be missing. remember that i will be the eventual result
                i+=1 
        return i
