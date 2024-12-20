




#python3 solution:

#arr = [1,2,3,4,5], k = 4, x = 3
#the correct solution moves right pointer down one to output [1, 2, 3, 4]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            #the abs(arr[l] - x) and abs(arr[r] - x) values represent the distance to x on a number line
            if abs(arr[l] - x) > abs(arr[r] - x):  #don't just look at the - |a - x| < |b - x| - and think oh gotta match exactly the statement. think about [1, 2, 3, 4, 5] k = 4, x = 3 and how 1 < 5, so 1 is actually considered closer to 3, so move 5 down, so this statement is False, and else executes
                l += 1
            else:
                r -= 1 #executes
        return arr[l: r + 1]


#the reason why the following is wrong:

#arr = [1,2,3,4,5], k = 4, x = 3
#the wrong solution moves left pointer up one to output [2, 3, 4, 5]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) < abs(arr[r] - x): 
                r -= 1
            else:
                l += 1 #executes 
        return arr[l: r + 1]

  #is because of the instructinon: |a - x| == |b - x| and a < b, so the correct condition is saying that, if a is not bigger than b, then move b because we already know that a < b because array is sorted
  #we already know left is smaller than right because array is sorted, so 2 < 4, so 2 is technically closer to 3 than 4 is given the problem

  #because 1 and 5 are the same distance from 3, but the problem says that since 1 < 5, then 5 is treated as farther from 3, so we have to move right down one - key insight


#the reason why the following is wrong:

#arr = [1,2,3,4,5], k = 4, x = -1 - should output [1, 2, 3, 4] because we want closest k LENGTH elements to x
#the wrong solution moves left pointer up one to output [2, 3, 4, 5]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) < abs(arr[r] - x): # 2 < 6 is true, so left += 1 - wrong
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]

#practice again:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #k length closest integers to x
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            if abs(arr[l] - x) > abs(arr[r] - x): #for arr = [1,2,3,4,5], k = 4, x = 3, we are supposed to move right down because 1 and 5 are same distance to x (3) but 1 < 5, so 1 is considered closer
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]

#4/15/24 refresher (missed):

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k: #as long as our window is bigger than size k, we keep shrinking either one way or another
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]

#4/17/24:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #k length aka frequency of the array result we will return
        #if two numbers have the same distance from x in opposite ways, we will pick the smaller one as the closer one, so we remove the upper one
        l, r = 0, len(arr) - 1 #we start the array bigger than size k aka size of entire input, so as long as the LENGTH of the array is bigger than k, we need to shrink
        while (r - l + 1) > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]

#4/18/24:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k: #we need to keep shrinking the window 
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]


#4/22/24:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]

#4/27/24 refresher:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l:r + 1]


#4/27/24 with explanation:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        #r = 4, l = 0, so 4 - 0 = 4, but 012345 is length 5, so since indicies, we need to + 1 because we want k length of elements, so 5 is indeed bigger than 4 (k), so shrink until length k (4) elements
        while (r - l + 1) > k:
            #abs(1 - 3) > abs(5 - 3) - False, because if both are equal distance apart but l is less than r, then l is considered closer
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        #since we keep shrinking and then stop when l - r + 1 is exactly k elements, we need to include both l and r pointers as indicies 
        return arr[l:r + 1]

#5/15/24 refresher:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #k number of closest integers in terms of length to x
        #1 and 5 are the same length as 3, but because 1 < 5, 1 is considered as closer, so move right down
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        return arr[l: r + 1]

#6/10/24 review:

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            mid = (l + r) // 2
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]


#7/15/24 refresher (my own solution):

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        return arr[l: r + 1]


#10/24/24 refresher (my own solution using python3):

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        myheap = []
        for a in arr:
            heapq.heappush(myheap, [abs(x - a), a])
        print(myheap)
        res = []
        while k > 0:
            a, b = heapq.heappop(myheap)
            res.append(b)
            k -= 1
        print(res)
        res.sort()
        return res
