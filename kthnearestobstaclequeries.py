3275. K-th Nearest Obstacle Queries
Solved
Medium

Topics
Companies

Hint
There is an infinite 2D plane.

You are given a positive integer k. You are also given a 2D array queries, which contains the following queries:

queries[i] = [x, y]: Build an obstacle at coordinate (x, y) in the plane. It is guaranteed that there is no obstacle at this coordinate when this query is made.
After each query, you need to find the distance of the kth nearest obstacle from the origin.

Return an integer array results where results[i] denotes the kth nearest obstacle after query i, or results[i] == -1 if there are less than k obstacles.

Note that initially there are no obstacles anywhere.

The distance of an obstacle at coordinate (x, y) from the origin is given by |x| + |y|.


#my incorrect solution that passed 385/591 test cases:

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res = []
        myheap = []
        for x, y in queries:
            distance = abs(x) + abs(y)
            heapq.heappush(myheap, [-distance, x, y])
        print(myheap)
        cnt = 0
        while cnt < len(queries):
            if cnt < k - 1:
                #a, b, c = heapq.heappop(myheap)
                res.append(-1)
                print(res)
                cnt += 1
            else:
                a, b, c = heapq.heappop(myheap)
                print(a)
                res.append(-1 * a)
                print(res)
                cnt += 1
        return res




#correct python3 solution: (could not solve by myself):


#if you put the if len(myheap) < k conditional first, it would lead to incorrect results because it would prematurely append -1 to res before the heap has been properly adjusted for its size. Here's why:

#Scenario:
#When the heap has more than k elements:
#The current logic with the if len(myheap) < k block first would immediately check the size and append -1 if the heap size is less than k before popping the excess elements (from the condition if len(myheap) > k).
#This means you could end up appending -1 even though the heap should have exactly k elements after the excess elements are removed.

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        # Max heap for the closest k obstacles (use negative values to simulate max-heap with Python's min-heap)
        res = []
        myheap = []
        for x, y in queries:
            dist = abs(x) + abs(y)
            heapq.heappush(myheap, -dist)
            if len(myheap) > k: #we want the exactly kth away that's the smallest, so pop
                heapq.heappop(myheap)
            if len(myheap) < k: #using elif here would cause us to also skip the else check, which would not append anything to result if, after popping, the size of the heap were exactly of size k!
                res.append(-1)
            else: 
                res.append(-1 * myheap[0]) #so the reason the else doesn't use res.append(-1 * heapq.heappop(myheap)) is because we don't want to remove any elements if the length of the heap is exactly of size k, just record the value of the smallest!
        return res

#9/23/24 refresher:

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res = []
        myheap = []
        for x, y in queries:
            dist = abs(x) + abs(y)
            heapq.heappush(myheap, -dist)
            if len(myheap) > k:
                heapq.heappop(myheap)
            if len(myheap) < k:
                res.append(-1)
            else:
                res.append(-1 * myheap[0])
        return res

#9/25/24 review (was able to solve):

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res = []
        myheap = []
        for x, y in queries:
            dist = abs(x) + abs(y)
            heapq.heappush(myheap, -1 * dist)
            if len(myheap) > k:
                heapq.heappop(myheap)
            if len(myheap) < k:
                res.append(-1)
            else:
                res.append(-1 * myheap[0])
        return res

