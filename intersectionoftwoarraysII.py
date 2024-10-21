
#350
#easy


#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#Example 2:

#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#Explanation: [9,4] is also accepted.


#my own solution using python3:

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1) & set(nums2)
        print(a)
        res = []
        for i in a:
            target = min(nums1.count(i), nums2.count(i))
            while target > 0:
                res.append(i)
                target -= 1
        return res
            
