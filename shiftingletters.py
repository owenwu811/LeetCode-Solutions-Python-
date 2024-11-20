
#848
#medium

#You are given a string s of lowercase English letters and an integer array shifts of the same length.

#Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

#For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

#Return the final string after all such shifts to s are applied.

 

#Example 1:

#Input: s = "abc", shifts = [3,5,9]
#Output: "rpl"
#Explanation: We start with "abc".
#After shifting the first 1 letters of s by 3, we have "dbc".
#After shifting the first 2 letters of s by 5, we have "igc".
#After shifting the first 3 letters of s by 9, we have "rpl", the answer.
#Example 2:

#Input: s = "aaa", shifts = [1,2,3]
#Output: "gfd"


#my own solution using python3:

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        orig = s
        letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h"
        : 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
        new = []
        howmany = []
        for i, c in enumerate(s):
            new.append(letters[c])
            howmany.append(i + 1)
        #print(new)
        #print(howmany)
        #[17, 14, 9]
        #[3, 5, 9]
        for i, s in enumerate(shifts):
            if s > 26:
                shifts[i] = s % 26
        totsum = sum(shifts)
        positions = []
        for i, s in enumerate(shifts):
            positions.append(totsum)
            totsum -= shifts[i]
            #print(totsum)
        #print(positions)
        y = []
        for i, p in enumerate(positions):
            
            #print(p + letters[orig[i]])
            y.append(p + letters[orig[i]])
        #print(79 % 26)
        print(y)
        final = []
        flippedd = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8
        : "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
        for p in y:
            print(p)
            if p > 26:
                use = p % 26
                #print(use)
                if use == 0:
                    final.append("z")
                    continue
            else:
                use = p
            final.append(flippedd[use])
        return "".join(final)

