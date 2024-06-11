#Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

#The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

#You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

#Input: points = [[1,3],[-2,2]], k = 1
#Output: [[-2,2]]
#Explanation:
#The distance between (1, 3) and the origin is sqrt(10).
#The distance between (-2, 2) and the origin is sqrt(8).
#Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


#python3 solution:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # if k = 3, we need to find the 3 coordinate points from the array that are closest to the origin in terms of Euclidean distance.
        #we have a list of points. each point is represented by a pair of values. the origin is the center [0, 0] - which of these points are closest to the origin. if k = 1, we return the single point that is closest to the origin. solution is unique, so no tie.
        #k could be 2 or 3. 
        #to find the origin - a squared plus b squared = c squared, and then square root to find c - we aren't trying to return distance, but we just want point to be closest
        #we dont want to take square root because we just want to compare totals - if 5 is bigger than 4, than square root of 5 is bigger than square root of 4
        #we just take absolute difference between x and y, square them, and then compare them to see which is closer to origin
        #to find k closest points, not just single closest point, you may want to sort - if list if of size n
        #for example (1 - 0)^2 + (3 - 0)^2 - use this value to sort entire list of points, the TC IS N LOG N BECAUSE WE ARE SORTING ENTIRE LIST
        #IF WE HAD 3 VALUES BUT JUST WANTED K, WHICH HAPPENED TO BE 2, WE WOULD JUST ITERATE OVER THE LIST AND FIND K, SO K DOSEN'T CHANGE TIME COMPLEXITY - TC DEPENDS ON N LOG N SORTING
        #WE DON'T NEED TO SORT ENTIRE THING BECAUSE WE ARE ONLY LOOKING FOR K POITNS, SO WE JUST NEED K CLOSEST POINTS, SO PROBLEM CAN BE SIMPLIFIED WITH MIN HEAP
        #FOR EVERY POINT - [1, 3] - WE DO 1 SQUARED + 3 SQUARED = 10 WITHOUT TAKING SQUARE ROOT
        # [-2, 2] - 2 SQUARED + NEGATIVE 2 SQUARED = 8 DISTANCE
        #[10, 1, 3], [8, -2, 2] - DISTANCE IS 1ST VALUE BECAUSE, WHEN WE PUT IN MIN HEAP, WE WANT 8 TO BE THE VALUE WE ORDER IT BY
        #WE TAKE [10, 1, 3], [8, -2, 2], AND WE RUN HEAPIFY, WHICH IS A LINEAR TIME ALGORITHM, NOT N LOG N
        #[10, 1, 3], [8, -2, 2] - WE WANT TO POP K TIMES, SO CLOSEST ONE HAPPENS TO BE 8 SINCE OUR EXAMPLE K = 1
        #WE POP FROM THE MIN HEAP K TIMES SINCE WE WANT K CLOSEST POINTS
        #THE OPERATION FOR POPPING FROM HEAP IS LOG SIZE OF HEAP, WHICH IS N WORST CASE, SO THIS TC IS K LOG N , SO MINHEAP IS MORE EFFICIENT BEACUSE IF K IS SMALL, THEN TC IS BETTER THAN N LOG N 
        #[10, 1, 3], [8, -2, 2] - WE POP [8, -2, -2] BECAUSE 8 IS CLOSER
        #WE APPEND [-2, -2] TO OUR RESULT LIST WITHOUT 8 - JUST THE COORDINATES
        #WE WILL THEN RETURN THAT RESULT OF [[-2, 2]] SINCE WE ONLY POP ONCE - WE RETURN A LIST OF ONE POINT
        minheap = [] #A LIST IN PYTHON IS A MINHEAP INITLALY
        for x, y in points: #WE GO OVER EVERY PAIR IN INPUT
            dist = (x ** 2) + (y ** 2) #COMPUTE DISTANCE WITH X SQUARED + Y SQUARED
            minheap.append([dist, x, y]) #WE APPEND POINT THAT WE JUST CALCULATED [8, -2, -2] - DISTANCE OF 8 IS KEY VALUE FOR OUR MIN HEAP
        heapq.heapify(minheap) #LINEAR TIME OPERATION THAT LIST TO REORDER THE LIST TO MAKE SURE IT IS IN STRUCTURE OF HEAP
        res = [] #WE WILL POP K TIMES
        while k > 0: #WHILE K > 0, KEEP POPPING FROM MINHEAP
            dist, x, y = heapq.heappop(minheap) #POP 3 VALUES FROM HEAP
            res.append([x, y]) #WHATEVER VALUE IS POPPED WILL GET APPENDED TO RESULT - ONLY APPEND 2 COORDINATES TO RESULT K TIMES - [-2, 2]
            k -= 1 #POP K TIMES
        return res
        

#practice run 2:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want to pop from our heap k times
        #we are given coordinates, and we want to get the distance of the coordinates and sort by them using heapify
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2) #panthagareom thereom 
            minheap.append([distance, x, y])
        heapq.heapify(minheap) 
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap) #do this k times
            res.append([x, y]) # we want the coordinate
            k -= 1
        return res

#2/18/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            distancefromorigin = (x ** 2) + (y ** 2)
            minheap.append([distancefromorigin, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res

#2/19/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want k number of closest pair of coordinates to the origin as our result
        minheap = [] #we will use a heapify to rearrange elements into a heap so that the heap property ensures that the smallest element is always at the root. 
        for x, y in points: 
            distance = (x ** 2) + (y ** 2) #we don't square root because we just care about comparing the distances to the corresponding coordinates
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0: #pop from heap k times to find k closest coordinates
            distance, x, y = heapq.heappop(minheap) #retrieve smallest element from heap, which represents closest point to origin. heappop just adjusts the heap to maintain the heap property after removing root. smallest element may not always be at root. 
            res.append([x, y])
            k -= 1
        return res
        
#2/20/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap) #sort by distance
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            result.append([x, y])
            k -= 1
        return result

#2/22/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap) 
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            result.append([x, y])
            k -= 1
        return result

#2/24/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = []
        for x, y in points:
           distance = (x ** 2) + (y ** 2)
           a.append([distance, x, y])
        heapq.heapify(a)
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(a)
            result.append([x, y])
            k -= 1
        return result

#2/26/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want k number of coordinates as lists that are closest to the point [0, 0]
        minheap = [] #we will use a minheap to add elements to it and then pop k times
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res


#2/27/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            result.append([x, y])
            k -= 1
        return result

#works the same way:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        result = []
        while k > 0:
            d, a, b = heapq.heappop(minheap) #variables can be named anything
            result.append([a, b])
            k -= 1
        return result

#3/3/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #our input array called points is a list of lists - each list of lists represents an [x, y] coordinate
        #we want to return k number of pairs given that the pairs are closest to [0, 0] compared to all pairs
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap) #the distance is the 0th index in our minheap list of lists, so this ensures that the smallest distance is at the top of the heap
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap) #we will do this k times
            res.append([x, y]) #we want the coordinate associated with the distance in our minheap = [[distance, x, y]], not the actual distance
            k -= 1
        return res

#3/10/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want k pairs of points that are closest to the origin
        minheap = []
        for x, y in points: #unpacking
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            a, x, y = heapq.heappop(minheap) #a instead of distance here works too!
            res.append([x, y])
            k -= 1
        return res


#3/17/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want k number of closest points to the origin
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap) #so that the smallest distance is at the top of the minheap
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res

#3/24/24:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want k number of points that are closest to the origin
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res


#4/21/24 review - key insight to remember is that minheap.append([distance, x, y]) and then heapq.heapify(minheap) sorts by the distance since the distance was appended first! also that for x, y in points goes through each pair and unpacks in the input list, so x, y = 1, 3... x, y = -2, 2

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want k closest frequency of points to the origin
        res = []
        minheap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minheap.append([distance, x, y])
        heapq.heapify(minheap)
        while k > 0:
            distance, newx, newy = heapq.heappop(minheap)
            res.append([newx, newy])
            k -= 1
        return res

#5/17/24 refresher:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we want the k number of closest coordinate points to the origin
        res = []
        stack = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            stack.append([distance, x, y]) #[10, 1, 3], [8, -2, 2]
        print(stack)
        heapq.heapify(stack)
        print(stack) 
        while k > 0:
            a, b, c = heapq.heappop(stack) #we need to use heapq.heappop() here instead of stack.pop() because heapq.heappop() pulls from the top of the heap aka the smallest distance 
            res.append([b, c])
            k -= 1
        return res #[1, 3]

#6/11/24 (missed):

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        tmp = []
        for x, y in points:
            dis = (x ** 2) + (y ** 2)
            tmp.append([dis, x, y])
        heapq.heapify(tmp) #you cannot have this inside of the for loop or else will get time limit exceeded!
        while k > 0:
            dis, x, y = heapq.heappop(tmp)
            res.append([x, y])
            k -= 1
        return res
