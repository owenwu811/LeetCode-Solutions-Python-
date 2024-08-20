

#You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

#Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

 

#Example 1:

#Input: a = 2, b = 4, c = 6
#Output: 6
#Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
#- Take from 1st and 3rd piles, state is now (1, 4, 5)
#- Take from 1st and 3rd piles, state is now (0, 4, 4)
#- Take from 2nd and 3rd piles, state is now (0, 3, 3)
#- Take from 2nd and 3rd piles, state is now (0, 2, 2)
#- Take from 2nd and 3rd piles, state is now (0, 1, 1)
#- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.

#correct python3 solution:

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c] #python has minheap by default, so we negate to get a max heap
        heapify(heap)
        ans = 0

        while len(heap) > 1: #we need atleast two piles full at all times
            first, sec = heappop(heap) + 1, heappop(heap) + 1 #we do + 1 because we are using that stone meaning we have one stone less
            ans += 1 #one turn of the game is successfully completed

            if first < 0: heappush(heap, first) #there are still stones left in this bigger pile
            if sec < 0: heappush(heap, sec) #there are still stones left in this bigger pile

        return ans #return the number of successful turns in the game
