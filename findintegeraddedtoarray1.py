#easy
#3131


#You are given two arrays of equal length, nums1 and nums2.

#Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x.

#As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

#Return the integer x.

 


#python3 solution:

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return min(nums2) - min(nums1)
