#easy
#2956


#You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

#answer1 : the number of indices i such that nums1[i] exists in nums2.
#answer2 : the number of indices i such that nums2[i] exists in nums1.
#Return [answer1,answer2].




#my own solution using python3:

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1, ans2 = 0, 0
        for n in nums1:
            if n in nums2:
                ans1 += 1
        for n in nums2:
            if n in nums1:
                ans2 += 1
        return [ans1, ans2]
