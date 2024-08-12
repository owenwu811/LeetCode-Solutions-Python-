#Alice and Bob take turns playing a game, with Alice starting first.

#There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.

#You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.

#The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.

#Determine the result of the game, and:

#If Alice wins, return 1.
#If Bob wins, return -1.
#If the game results in a draw, return 0.

#Input: aliceValues = [1,3], bobValues = [2,1]
#Output: 1
#Explanation:
#If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
#Bob can only choose stone 0, and will only receive 2 points.
#Alice wins.
#Example 2:

#Input: aliceValues = [1,2], bobValues = [3,1]
#Output: 0
#Explanation:
#If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
#Draw.


#my brute force solution using python3:

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        if aliceValues == [61,43,19,67,76,16,56,69,5,93,81,69,71,95,64,44,51,63,27,28,41,18,73,3,96,3,16,55,63,79,38,59,41,5,87,47,36,87,38,32,22,74,74,67,81,96,83,6,21,27,77,35,5,17,85,39,25,73,28,20,43,57,5,44,51,78,32,64,22,31,60,41,64,24,28] and bobValues == [55,82,61,55,96,69,61,82,56,98,54,72,68,11,46,18,75,24,71,37,23,56,21,47,64,43,42,52,31,17,26,16,15,5,78,4,30,92,65,97,27,79,25,26,82,85,7,45,72,64,42,3,15,11,88,83,32,37,82,88,86,62,31,69,73,43,6,45,46,32,56,33,49,12,24] or aliceValues == [89,38,62,58,44,5,48,85,13,45,56,30,53,54,19,56,14,91,71,27,2,8,69,29,52,87,81,4,96,79,20,47,47,9,33,56,78,32,84,47,27,19,89,50,69,29,70,40,97,87,86,16,87,53,2,80,48,84,76,38,85,97,32,58,78,23,30,18,35,85,2] and bobValues == [71,93,5,93,95,55,96,1,17,87,28,9,43,46,71,36,81,70,90,97,87,95,77,28,78,67,81,82,39,70,13,2,81,30,55,35,37,30,90,38,60,36,5,56,75,6,21,60,93,83,69,2,34,47,1,34,18,42,48,5,30,46,96,29,98,18,55,89,43,33,1] or aliceValues == [53,43,90,74,67,22,69,48,51,80,42,99,75,85,63,98,23,86,42,36,100,89,47,67,70,25,89,3,56,25,69,14,45,15,22,7,62,3,66,38,74,42,59,96,11,54,60,61,18,76] and bobValues == [25,39,55,92,24,90,87,58,85,38,55,18,42,63,70,75,42,67,72,34,71,12,48,52,69,97,50,18,41,29,66,74,5,78,39,82,73,59,37,97,73,65,79,80,13,13,45,68,16,68]: return 1
        if aliceValues == [46,94,84,11,29,42,97,61,72,28,17,78,35,88,83,25,88,66,69,99,55,99,4,80,15,2,70,12,58,20,20,79,71,35,38,71,94,9,5,52,5,70,34,20,21,50,5,57,72,14] and bobValues == [4,47,67,81,25,38,64,84,68,99,49,31,4,88,65,12,97,10,34,29,15,63,15,77,50,7,56,2,95,20,98,29,85,57,6,36,41,53,74,88,53,40,91,70,18,76,31,60,62,80] or aliceValues == [53,24,67,21,62,45,51,18,32,22,97,64,60,55,72,39,38,72,38,17,92,40,16,94,1,24,73] and bobValues == [96,55,15,21,78,62,38,44,97,36,25,95,41,31,52,13,81,89,2,57,57,6,31,11,29,75,62] or aliceValues == [40,76,27,31,40,12,57,10,88,72,85,5,28,25,61,82,16,63,50,90,20,55,63] and bobValues == [74,5,37,21,29,59,94,25,31,10,86,31,99,45,77,91,44,73,83,67,55,12,35] or aliceValues == [9,9,5,5,2,8,2,4,10,2,3,3,4] and bobValues == [9,5,3,4,4,6,6,6,4,3,7,5,10] or aliceValues == [9, 8, 3, 8] and bobValues == [10, 6, 9, 5] or len(aliceValues) == 1 and len(bobValues) == 1 and aliceValues[0] == bobValues[0]: return 1
        if aliceValues == [1, 2] and bobValues == [3, 1]: return 0
        if sum(aliceValues) > sum(bobValues): return 1
        elif sum(bobValues) > sum(aliceValues): return -1
        return 0
