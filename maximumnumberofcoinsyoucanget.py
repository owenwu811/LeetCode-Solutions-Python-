
#1561
#medium

#There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

#In each step, you will choose any 3 piles of coins (not necessarily consecutive).
#Of your choice, Alice will pick the pile with the maximum number of coins.
#You will pick the next pile with the maximum number of coins.
#Your friend Bob will pick the last pile.
#Repeat until there are no more piles of coins.
#Given an array of integers piles where piles[i] is the number of coins in the ith pile.

#Return the maximum number of coins that you can have.


#my own solution using python3 after looking at another solution:

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        res = 0
        toremove = len(piles) // 3 #we need to choose 3 piles of coins as many times as allowed
        while toremove > 0:
            piles.pop()
            toremove -= 1
        for i in range(len(piles)):
            if i % 2 != 0:
                res += piles[i]
        return res
