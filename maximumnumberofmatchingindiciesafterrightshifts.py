#3400
#medium

#You are given two integer arrays, nums1 and nums2, of the same length.

#An index i is considered matching if nums1[i] == nums2[i].

#Return the maximum number of matching indices after performing any number of right shifts on nums1.

#A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

 

#Example 1:

#Input: nums1 = [3,1,2,3,1,2], nums2 = [1,2,3,1,2,3]

#Output: 6

#Explanation:

#If we right shift nums1 2 times, it becomes [1, 2, 3, 1, 2, 3]. Every index matches, so the output is 6.


#my own solution using python3:

class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        cur = nums1.copy()
        cur = deque(nums1)
        res = 0
        for i in range(len(nums1)):
            cur.rotate()
            b = 0
            for j in range(len(cur)):
                if cur[j] == nums2[j]:
                    b += 1
            res = max(res, b)
        return res
