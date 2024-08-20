
#easy
#74.5%acceptancerate

#Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 

#Example 1:

#Input: s = "foobar", letter = "o"
#Output: 33
#Explanation:
#The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
#Example 2:

#Input: s = "jjjj", letter = "k"
#Output: 0
#Explanation:
#The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.


#my own solution using python3:

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s: return 0
        mydict = dict()
        for n in s:
            if n not in mydict:
                mydict[n] = 0
            mydict[n] += 1
        tot = sum(mydict.values())
        print(tot)
        for k in mydict:
            if k == letter:
                return int((mydict[k] / tot) * 100)
