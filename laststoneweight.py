#You are given an array of integers stones where stones[i] is the weight of the ith stone.

#We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

#If x == y, both stones are destroyed, and
#If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#At the end of the game, there is at most one stone left.

#Return the weight of the last remaining stone. If there are no stones left, return 0.

#Input: stones = [2,7,4,1,8,1]
#Output: 1


#python3 solution:

#you can only remove from the top of a heap and only by using heapq.heappop()
#python does not have max heap by default. when you pop element from heap using heapq.heappop(), you get the most negative number, which corresponds to the largest positive number before negation
# the bigger a positive number, the smaller its negative sibling is
# heapify looks at tree from bottom up
# in python, the heapq module provides implementation of t a min heap, not max heap. so when you use heapq.heapify() on a list, it arranges elements such that the smallest element is at the root or top of the heap. this is the opposite behavior for this problem.
# stones.append(0) is appending 0 to the list stones. the purpose of this line is to handle the case where all stones have been crushed, and the list stones is empty, so directly accessing stones[0] would rause an indexerror. by appending 0, the code ensures that there is atleast 1 element in the list, so stones[0] will not cause and error and will correctly return 0 if there are no stones left
# return (abs(stones[0]) negates the value of stones[0]. since stones were initially negated to simulate a max heap where the largest stone is on top, the actual weight of the last stone (if any) is the absolute value of the top element of the heap. this abs() function is used to convert the negative number back to it's original value, representing the actual value of the last remaining stone. 

class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] 
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])

#7/21/24 refresher (my own solution):

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = []
        for s in stones:
            minheap.append(-s)
        heapq.heapify(minheap) #[-8, -7, -4, -2, -1, -1]
        print(minheap)
        while len(minheap) > 1:
            first = -1 * heapq.heappop(minheap)
            second = -1 * heapq.heappop(minheap)
            print(first)
            print(second)
            if first == second:
                pass
            elif first > second:
                pushback = first - second
                print(pushback)
                heapq.heappush(minheap, -1 * pushback)
            print(minheap)
        return -1 * minheap[0] if minheap else 0


        
