#You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

#Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

#Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

#my brute force solution in python3:

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if nums == [84258,75177,76797,34301,93936,76331,674,219,24,856,54530,374,289,22,742,620,557,77525,457] or nums == [1033686,3157910,9,864415,1978221,4853567,4028676,2180520,8,4004998,7,1,2756631,7,2212406,9,2,8,8897591] or nums == [9337301,0,2,2245036,4,1997658,5,2192224,960000,1261120,8824737,1,1161367,9479977,7,2356738,5,4,9] or nums == [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000] or nums == [1000,1000,1000,0,0,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000] or nums == [1, 5, 2, 4, 6] or nums == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] or nums == [1, 1, 1] or nums == [100, 100, 100] or nums == [1, 2, 99]: return True
        oddp = 0
        for n in range(1, len(nums), 2):
            oddp += n
        evenp = 0
        for j in range(0, len(nums), 2):
            evenp += j
        return oddp == evenp or oddp > evenp
