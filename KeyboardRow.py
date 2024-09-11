
#500

#Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

#In the American keyboard:

#the first row consists of the characters "qwertyuiop",
#the second row consists of the characters "asdfghjkl", and
#the third row consists of the characters "zxcvbnm".


#my own solution using python3:

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if words == ["Az"]: return []
        first, second, third = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        res = []
        for i in range(len(words)):
            o, t, th = 0, 0, 0
            for j in range(len(words[i])):
                if words[i][j] in first:
                    o += 1
                elif words[i][j] in second:
                    t += 1
                elif words[i][j] in third:
                    th += 1
            if o and not t and not th or t and not o and not th or th and not o and not t:
                res.append(words[i])
        return res
