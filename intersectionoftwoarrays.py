
#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]



#My solution - Python3

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        if len(nums1) == 1 and len(nums2) == 1 and nums1[0] == nums2[0]:
            return [nums1[0]]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.add(nums1[i])
        return res

        
