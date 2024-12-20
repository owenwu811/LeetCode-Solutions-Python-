

#1244
#medium

#Design a Leaderboard class, which has 3 functions:

#addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
#top(K): Return the score sum of the top K players.
#reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
#Initially, the leaderboard is empty.

#my own solution using python3:

class Leaderboard:

    def __init__(self):
        self.d = dict()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.d:
            self.d[playerId] = 0
        self.d[playerId] += score
        

    def top(self, K: int) -> int:
        res = 0
        sortedd = sorted(self.d.items(), key=lambda x: x[1], reverse=True)
        print(sortedd)
        for i in range(K):
            print(sortedd[i][1])
            res += sortedd[i][1]
        return res
        
