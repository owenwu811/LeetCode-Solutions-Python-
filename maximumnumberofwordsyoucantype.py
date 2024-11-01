
#1935
#easy


#There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

#Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

#Example 1:

#Input: text = "hello world", brokenLetters = "ad"
#Output: 1
#Explanation: We cannot type "world" because the 'd' key is broken.


#my own solution using python3:

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = text.split(" ")
        print(t)
        res = 0
        for word in t:
            flag = True
            for b in brokenLetters:
                if b in word:
                    flag = False
            if flag:
                res += 1
        return res
