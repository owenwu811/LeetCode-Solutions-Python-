
#Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

#easy
#75.5% acceptancerate

#Example 1:

#Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
#Output: [3,2]
#Explanation: The values that are present in at least two arrays are:
#- 3, in all three arrays.
#- 2, in nums1 and nums2.

#my own solution using python3:

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        tmp = []
        tmp = nums1 + nums2 + nums3
        res = []
        print(tmp)
        for t in tmp:
            if t in nums1 and t in nums2 or t in nums2 and t in nums3 or t in nums1 and t in nums3:
                res.append(t)
        myset = set()
        for r in res:
            myset.add(r)
        ans = []
        for s in myset:
            ans.append(s)
        return ans
