
#Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

#Example 1:

#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].


#python3 solution:


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsums = set()
        subsums.add(0)
        half = sum(nums) // 2
        #the double for loop is for finding a subarray sum that is equal to half of the sum of nums aka target
        for inputnumber in nums:
            set2 = set()
            for subsumsn in subsums:
                set2.add(subsumsn + inputnumber)
                set2.add(subsumsn)
            subsums = set2
        return half in subsums
        #Since 22 is the sum of the nums, if we can find the subarray that is equal to the  target 11 then the sum of remaining nums always equal to the target 11.
        #mylist = [5] - print(5 in mylist) - True


#1/29/24 practice:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for number in nums:
            set2 = set()
            for element in subsum:
                set2.add(element + number)
                set2.add(element)
            subsum = set2
        return half in subsum
