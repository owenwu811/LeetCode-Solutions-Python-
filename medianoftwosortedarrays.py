

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
        totalhalf = total // 2 #if you did / 2 here instead of // 2, would you get an error that says indicies must be integer or slices, not float
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
                    return min(aright, bright) #using max(aleft, bleft) would cause error because aleft > bright means that median is on left <<< side of current partition, so max(aleft, bleft) would be picking an element from left array that is bigger than actual median
                return (max(aleft, bleft) + min(aright, bright)) / 2 #do not round down so we can get decimal
            if aleft > bright:
                r = i - 1
            else:
                l = i + 1


#5/4/24 refresher:

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
            if aleft <= bright and bleft <= aright:
                if total % 2 > 0:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1



#5/5/24 refresher:

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
            if aleft <= bright and bleft <= aright:
                if total % 2 > 0:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#5/7/24 refresher:

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
            if aleft <= bright and bleft <= aright: #cannot be aright <= bleft because aright is infinity, and infinity is never less than anything, leading to an infinite loop for test case nums1 = [1, 3], nums2 = [2]
                if total % 2 > 0:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#5/12/24 refresher (missed):

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        #you know the arrays are sorted, so you can run the binary search
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
            aright = a[i + 1] if (i + 1) < len(a) else float('inf') #would be infinity for nums1 = [1, 3], nums2 = [2] when a = [2] and b = [1, 3] because (i + 1) = 1, and 1 < 1 (len(a)) is False
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright:
                if total % 2 > 0:
                    return min(aright, bright)
                return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#5/13/24 refresher:

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
            aright = a[i + 1] if (i + 1) < len(a) else float('inf') #true for a[1] b[2, 3]
            bleft =  b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright:
                if total % 2 > 0:
                    return min(aright, bright)
                return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#5/20/24:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        totalhalf = total // 2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2 #5 // 2 > 2 vs. 5 / 2 > 2.5
            j = totalhalf - i - 2
            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if (i + 1) < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright:
                if total % 2 > 0: #if our total length is odd
                    return (min(aright, bright))  
                return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


#if we have even # of elements, we get the 2 middle and find the median
#if we have an odd # of elements, the middle is the median 

#5/30/24 review:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        #nums1 = [1, 3], nums2 = [2]
        a, b = nums1, nums2
        total = len(nums1) + len(nums2) #3
        totalhalf = total // 2 #1
        if len(b) < len(a): #[2] is shorter than [1, 3], so swap 
            a, b = b, a
        #now, a = [2], and b = [1, 3]
        l, r = 0, len(a) - 1 
        while True:
            i = (l + r) // 2 #i = 0. 2nd iteration: (0 + -1) // 2 > -1, so i = -1
            j = totalhalf - i - 2 #1 - 0 - 2 = -1, so j = -1. 2nd iteration: (1 - - 1 - 2) > 0, so j = 0
            aleft = a[i] if i >= 0 else float('-inf') #a = [2], so a[0] = 2 since 0 >= 0. 2nd iteration: a[-1] means i >= 0 is False, so a = float('-inf')
            aright = a[i + 1] if (i + 1) < len(a) else float('inf') #a = [2], so a[0 + 1] - a[1] is out of bounds, so float('inf'). 2nd iteration: a[-1 + 1] > a[0] = 2, so aright = 2
            bleft = b[j] if j >= 0 else float('-inf') #b = [1, 3], so since -1 >= 0 is False, so float('-inf'). 2nd iteration: b[0] = 1, so bleft = 1
            bright = b[j + 1] if (j + 1) < len(b) else float('inf') #b = [1, 3], so b[-1 + 1] = b[0], so (0 + 1) < 2, so b[0] > 1, so bright = 1. 2nd iteration: b[1] = 3, so bright = 3
            if aleft <= bright and bleft <= aright: #so aleft (2) <= bright (1) is already False, so we haven't found perfect partition point, so go to elif. 2nd iteration: since aleft (-infinity) <= bright(3) and bleft(1) <= aright(2) is True, we go to inner if block
                if total % 2 > 0: #3 % 2 == 1, so 1 > 0 is True, so execute inner block since total length is of odd number (3)
                    return min(aright, bright) #return min(2, 3) since aright = 2 and bright = 3, so the result is median = 2. note that aleft = -infinity and bleft = 1, and max of these two would not be the median of [2] and [1, 3] sorted arrays! so it would fail the nums1 = [1, 3], nums2 = [2] test case!
                return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright: #aleft(2) > bright(1) - True, so r = 0 - 1, so r = -1, and we go back to while True
                r = i - 1
            else:
                l = i + 1

       #a = [2] aleft = 2, aright = float('inf')
       #b = [1, 3] bleft = float('-inf'), bright = 1

#6/25/24 review:

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
            j = totalhalf - i - 2 #totalhalf - i - 2, not i - totalhalf - 2!
            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if (i + 1) < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if (j + 1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright:
                if total % 2 != 0:
                    return min(aright, bright) 
                return (max(aleft, bleft) + min(aright, bright)) / 2
            if aleft > bright:
                r = i - 1
            else:
                l = i + 1

        
