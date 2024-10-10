

#medium
#2279


#You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

#Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

 

#Example 1:

#Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
#Output: 3
#Explanation:
#Place 1 rock in bag 0 and 1 rock in bag 1.
#The number of rocks in each bag are now [2,3,4,4].
#Bags 0, 1, and 2 have full capacity.
#There are 3 bags at full capacity, so we return 3.
#It can be shown that it is not possible to have more than 3 bags at full capacity.
#Note that there may be other ways of placing the rocks that result in an answer of 3.


#my own solution using python3:

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        #ith bag currently holds rocks - can hold capacity
        myheap = []
        total = 0
        for i, c in enumerate(capacity):
            if capacity[i] == rocks[i]:
                total += 1
                continue
            if capacity[i] > rocks[i]:
                heapq.heappush(myheap, (capacity[i] - rocks[i]))
        print(myheap)
        myheap.sort()
        for i, h in enumerate(myheap):
            if additionalRocks > 0 and myheap[i] <= additionalRocks:
                additionalRocks -= h
                myheap[i] = 0
            else:
                break
        return total + myheap.count(0)

                
        
        
