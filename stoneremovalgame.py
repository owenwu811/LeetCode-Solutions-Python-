
#3360
#easy

#Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

#Alice starts by removing exactly 10 stones on her first turn.
#For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
#The player who cannot make a move loses the game.

#Given a positive integer n, return true if Alice wins the game and false otherwise.

 

#Example 1:

#Input: n = 12

#Output: true

#Explanation:

#Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
#Bob cannot remove 9 stones, so Alice wins.


#my own solution using python3:

class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n == 10:
            return True
        res = []
        start = 10
        turn = 0
        while n >= 0:
            if turn % 2 == 0:
                res.append("a")
            else:
                res.append("b")
            n -= start
            start -= 1
            turn += 1
        print(res)
        return res[-1] == "b"
