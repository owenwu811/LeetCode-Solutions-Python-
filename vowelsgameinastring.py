
#3227
#medium

#Alice and Bob are playing a game on a string.

#You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:

#On Alice's turn, she has to remove any non-empty 
#substring
# from s that contains an odd number of vowels.
#On Bob's turn, he has to remove any non-empty 
#substring
# from s that contains an even number of vowels.
#The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.

#Return true if Alice wins the game, and false otherwise.

#The English vowels are: a, e, i, o, and u.


#my own solution using python3:

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        print(d)
        if "a" not in s and "e" not in s and "i" not in s and "o" not in s and "u" not in s:
            return False
        ans = sum(d.values())
        if ans % 2 == 0:
            return True
        else:
            return True
        
