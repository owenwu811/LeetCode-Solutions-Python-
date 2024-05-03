

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).
#nums1 = [1,3], nums2 = [2] - output: 2.00000

#because the input arrays given to us are in sorted order, we can simulate this without merging the arrays with a binary search



#python3 solution:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(nums1) + len(nums2) 
        half = total // 2 #telsl us total in left position 
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1 #run binary search on A since A is smaller than b
        while True: #we are garunteed a median
            i = (l + r) // 2 #pointer for A
            j = half - i - 2 #pointer for B: index in array b (j isn't number of elements. j is the mid index of b)
            aleft = a[i] if i >= 0 else float("-inf") #a[i] is the value in the left partition. if i is out of bounds, i < 0, so default for left is negative infinity
            aright = a[i + 1] if (i + 1) < len(a) else float("inf")
            bleft = b[j] if j >= 0 else float("-inf")
            bright = b[j + 1] if (j + 1) < len(b) else float("inf")
            if aleft <= bright and bleft <= aright: #is our partition correct? think the crossing comparison between B and A
                if total % 2: #odd number of elements
                    return min(aright, bright)
                #even number of elements
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#5/3/24 refresher:


#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).


#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.

#python3 solution:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        totalhalf = total // 2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1 #run binary search on shorter array
        while True: #binary search run over and over again
            #left partition index of shorter array
            i = (l + r) // 2
            #left partition index of longer array - If total is odd, total // 2 gives the index of the median element. Since we want the left partition to contain one less element than the right partition, we subtract 1 from total // 2.
            j = totalhalf - i - 2
            aleft = a[i] if i >= 0 else float('-inf')
            #a[i + 1] because the goal is to find center 4 elements in the end 
            aright = a[i + 1] if (i + 1) < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright: #if true, we have found the 4 final partition points
                if total % 2 > 0: #if number of elements in both arrays is odd
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2 #if number of elements in both arrays is even
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#practice again:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        totalhalf = total // 2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = totalhalf - i - 2
            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if (i + 1) < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            #if aleft <= bright and bleft <= aright:
            if bleft <= aright and aleft <= bright:
                if total % 2 > 0:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#practice again:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        totalhalf = total // 2
        if len(b) < len(a): #without these two lines if len(b) < len(a), we would get an index out of bounds error
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = totalhalf - i - 2
            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if (i + 1) < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright:
                if total % 2 > 0:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2 #do not round down so we can get decimal
            if aleft > bright:
                r = i - 1
            else:
                l = i + 1

