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
            if len(myheap) < k:
                res.append(-1)
            else: 
                res.append(-1 * myheap[0]) #apparently heapq.heappop(myheap) is not the same as myheap[0]!
        return res
