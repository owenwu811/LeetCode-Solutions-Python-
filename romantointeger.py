#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.




#python3 solution:

class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for char in range(len(s)):
            if char < len(s) - 1 and mydict[s[char]] < mydict[s[char + 1]]:
                res -= mydict[s[char]]
            else:
                res += mydict[s[char]]
        return res

#4/5/24:

class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and mydict[s[i]] < mydict[s[i + 1]]:
                res -= mydict[s[i]]
            else:
                res += mydict[s[i]]
        return res

#has nothing to do with the previous character in s! we are just saying that if the current is smaller than the next, then the result of both current + next is (next - current), which is (- current + next)! - missed on 4/7/24!


#4/7/24 - my own solution: - THIS WORKS TOO! YOU JUST HAVE TO MAKE SURE YOU MINUS AND ADD THE PREVIOUS NUMBER!

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if i > 0 and mapping[s[i]] > mapping[s[i - 1]]:
                res -= mapping[s[i - 1]]
            else:
                res += mapping[s[i - 1]]
        return res
        
