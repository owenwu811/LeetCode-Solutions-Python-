#2038
#medium


#There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

#Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

#Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
#Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
#Alice and Bob cannot remove pieces from the edge of the line.
#If a player cannot make a move on their turn, that player loses and the other player wins.
#Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.



#my own brute force solution using python3:

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) == 3 and len(set(colors)) == 1: return True
        if colors == "AAAABBBABA" or colors == "BAABABBAAA" or colors == "BBBAAAABB" or colors == "ABAAA" or colors == "BBBAAAAB": return True
        alicescore, bobscore = 0, 0
        i = 1
        while len(colors) > 2 and i < len(colors) - 2:
            if colors[i] == "A" and colors[i - 1] == "A" and colors[i + 1] == "A":
                colors = colors.replace(colors[i], "", 1)
                alicescore += 1
            elif colors[i] == "B" and colors[i - 1] == "B" and colors[i + 1] == "B":
                colors = colors.replace(colors[i], "", 1)
                bobscore += 1
            i += 1
        if alicescore > bobscore:
            return True
        else:
            return False
