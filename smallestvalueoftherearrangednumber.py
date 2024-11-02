

#2165
#medium


#You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

#Return the rearranged number with minimal value.

#Note that the sign of the number does not change after rearranging the digits.

 

#Example 1:

#Input: num = 310
#Output: 103
#Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
#The arrangement with the smallest value that does not contain any leading zeros is 103.
#Example 2:

#Input: num = -7605
#Output: -7650
#Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
#The arrangement with the smallest value that does not contain any leading zeros is -7650.


#my own solution using python3:

class Solution:
    def smallestNumber(self, num: int) -> int:
        b = sorted(str(num))
        #print(b)
        if num < 0:
            new = ""
            for i in range(len(b) -1, -1, -1):
                new += str(b[i])
            #print(new)
            new = new[-1:] + new[0: -1]
            #print(int(new))
            return int(new)
        else:
            for i in range(1, len(b)):
                while int(b[i]) > 0 and int(b[0]) == 0:
                    print(b[i])
                    print(b[i - 1]) 
                    print(b)
                    b[i], b[0] = b[0], b[i]
                    print(b)
                    return int("".join(b))
                    break
            #print(b)
            redone = "".join(b)
            print(redone)
            return int(redone)
