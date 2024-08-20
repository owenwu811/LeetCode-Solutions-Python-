
#You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

#You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.


#Example 1:

#Input: amount = [1,4,2]
#Output: 4
#Explanation: One way to fill up the cups is:
#Second 1: Fill up a cold cup and a warm cup.
#Second 2: Fill up a warm cup and a hot cup.
#Second 3: Fill up a warm cup and a hot cup.
#Second 4: Fill up a warm cup.
#It can be proven that 4 is the minimum number of seconds needed.


#my own solution using python3 borrowing parts from another solution:

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        if amount == [0,0,0]: return 0
        res = 0
        heap = []
        for a in amount:
            heap.append(-a)
        heapq.heapify(heap)
        while len(heap) > 1:
            first, second = heapq.heappop(heap) + 1, heapq.heappop(heap) + 1
            res += 1
            if first < 0:
                heapq.heappush(heap, first)
            if second < 0:
                heapq.heappush(heap, second)
        if heap: #edge case because if the heap has exactly 1 element, you still need to fill that cup
            return res - heap[0]
        return res
