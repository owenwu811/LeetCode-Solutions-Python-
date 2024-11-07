

#3324
#medium

#You are given a string target.

#Alice is going to type target on her computer using a special keyboard that has only two keys:

#Key 1 appends the character "a" to the string on the screen.
#Key 2 changes the last character of the string on the screen to its next character in the English alphabet. For example, "c" changes to "d" and "z" changes to "a".
#Note that initially there is an empty string "" on the screen, so she can only press key 1.

#Return a list of all strings that appear on the screen as Alice types target, in the order they appear, using the minimum key presses.

 

#Example 1:

#Input: target = "abc"

#Output: ["a","aa","ab","aba","abb","abc"]

#my own solution using python3:

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        letters = deque("abcdefghijklmnopqrstuvwxyz")
        res = []
        li = 0
        starting = []
        while len(starting) < len(target):
            starting.append(letters[li])
            res.append("".join(starting))
            while starting[-1] != target[len(starting) - 1]:
                orig = target[len(starting) - 1]
                gone = starting.pop()
                new = letters[letters.index(gone) + 1]
                starting.append(new)
                res.append("".join(starting))
        return res
                
                
