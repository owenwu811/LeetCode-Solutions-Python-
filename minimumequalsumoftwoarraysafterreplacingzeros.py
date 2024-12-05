
#2918
#medium

#You are given two arrays nums1 and nums2 consisting of positive integers.

#You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

#Return the minimum equal sum you can obtain, or -1 if it is impossible.

 

#Example 1:

#Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
#Output: 12
#Explanation: We can replace 0's in the following way:
#- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
#- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
#Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.


#my own solution using python3:

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        print(nums1, nums2)
        first, second = sum(nums1), sum(nums2)
        if first != second and 0 not in nums1 and 0 not in nums2:
            return -1
        print(first, second)
        if 0 in nums1 and 0 not in nums2 or 0 in nums2 and 0 not in nums1:
            if 0 not in nums2 and 0 in nums1 and second > first and nums1.count(0) <= abs(second - first):
                return second
            if 0 in nums2 and 0 not in nums1 and first > second and nums2.count(0) <= abs(first - second):
                return first
            return -1
        zcone, zctwo = nums1.count(0), nums2.count(0)
        print(first, second)
        if zcone > zctwo and first > second:
            return max(first, second) + (1 * nums1.count(0))
        else:
            a, b = first + (1 * nums1.count(0)), second + (1 * nums2.count(0))
            print(a, b)
            return max(a, b)
            return max(first, second) + (1 * nums2.count(0))
