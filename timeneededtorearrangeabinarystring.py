

#2380
#medium

#You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.

#Return the number of seconds needed to complete this process.

 

#Example 1:

#Input: s = "0110101"
#Output: 4
#Explanation: 
#After one second, s becomes "1011010".
#After another second, s becomes "1101100".
#After the fourth second, s becomes "1111000".
#No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
#so we return 4.


#my own solution using python3:

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        stack = list(s)
        res = 0
        while "01" in s:
            i = 1
            while i < len(stack):
                if stack[i] == "1" and stack[i - 1] == "0":
                    stack[i], stack[i - 1] = stack[i - 1], stack[i]
                    i += 2
                else:
                    i += 1
            s = "".join(stack)
            res += 1
        return res
        
        #"0 1 1 0 1 0 1"
        # 1 0
        # 1 0 1 0 1 0 1
        #       1 0
        # 1 0 1 1 0 0 1
        #           1 0
        # 1 0 1 1 0 1 0
