

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).
#nums1 = [1,3], nums2 = [2] - output: 2.00000


#python3 solution:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            aleft = a[i] if i >= 0 else float("-inf")
            aright = a[i + 1] if (i + 1) < len(a) else float("inf")
            bleft = b[j] if j >= 0 else float("-inf")
            bright = b[j + 1] if (j + 1) < len(b) else float("inf")
            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1
