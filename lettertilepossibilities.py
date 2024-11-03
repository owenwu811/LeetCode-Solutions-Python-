

#1079
#medium

#You have n  tiles, where each tile has one letter tiles[i] printed on it.

#Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

#Example 1:

#Input: tiles = "AAB"
#Output: 8
#Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
#Example 2:

#Input: tiles = "AAABBC"
#Output: 188
#Example 3:

#Input: tiles = "V"
#Output: 1

#correct python3 solution (could not solve):

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        for i in range(1, len(tiles) + 1):
            res += len(set(permutations(tiles, i)))
        return res
