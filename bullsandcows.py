

#299
#medium

#You are playing the Bulls and Cows game with your friend.

#You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

#The number of "bulls", which are digits in the guess that are in the correct position.
#The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
#Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

#The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

#Example 1:

#Input: secret = "1807", guess = "7810"
#Output: "1A3B"
#Explanation: Bulls are connected with a '|' and cows are underlined:
#"1807"
#  |
#"7810"


#my own solution using python3:

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        s = Counter(secret)
        g = Counter(guess)
        bad = []
        for i in range(len(secret)):
            #print(secret[i], guess[i])
            if secret[i] == guess[i]:
                s[secret[i]] -= 1
                g[guess[i]] -= 1
                if s[secret[i]] == 0:
                    del s[secret[i]]
                if g[guess[i]] == 0:
                    del g[guess[i]]
                bulls += 1
        cows = 0
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                if guess[i] in s:
                    s[guess[i]] -= 1
                    if s[guess[i]] == 0:
                        del s[guess[i]]
                    print(guess[i])
                    cows += 1
        #print(bulls)
        new = ""
        new += str(bulls)
        new += "A"
        new += str(cows)
        new += "B"
        return new
