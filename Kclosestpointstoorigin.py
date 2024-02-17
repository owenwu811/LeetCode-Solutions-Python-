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
        
