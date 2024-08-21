


Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]


#correct solution using python3:

#Input: s = "CONTEST IS COMING"
#Output: ["CIC","OSO","N M","T I","E N","S G","T"]

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split() 
        print(words) #['CONTEST', 'IS', 'COMING']
        max_len = max(len(word) for word in words) #contest > 7, is > 2, coming > 6
        print(max_len) #7
        res = []
        for i in range(max_len): #0123456 > up to the length of the longest word in indicies
            vert_words = '' #clear word for each new vertical
            for word in words: #CONTEST, IS, COMING
                if i < len(word): #0 is less than length of "CONTEST"
                    vert_words += word[i] #becomes "C"
                else:
                    vert_words += ' ' #when i = 2, 2 < length of "IS" is false, so becomes "N " by adding space to the end 
            res.append(vert_words.rstrip()) #"CIC" is appended to res
        return res
