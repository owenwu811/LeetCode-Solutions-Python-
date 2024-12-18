
#1545
#medium

#Given two positive integers n and k, the binary string Sn is formed as follows:

#S1 = "0"
#Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
#Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

#For example, the first four strings in the above sequence are:

#S1 = "0"
#S2 = "011"
#S3 = "0111001"
#S4 = "011100110110001"
#Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

#Example 1:

#Input: n = 3, k = 1
#Output: "0"
#Explanation: S3 is "0111001".
#The 1st bit is "0".



#my own solution using python3:

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        first = "0"
        second = "011"
        if k == 1:
            return "0"
        if k == 2:
            return "1"
        #s1 = "0" > "0"
        #s2 = s1 + "1" + reverse(invert(s1)) > "0" + "1" + "1" (last 1 because s1 was "0" and i was the 1st, so you actually flip it vs original for rest) > "011"
        #011 > reversed becomes 110 > inverted becomes 001
        #s3 = s2 + "1" + reverse(invert(s2)) > "011" + "1" + "001" > "0111001"
        #0111001 > reversed becomes 1001110 > inverted becomes 0110001
        #s4 = s3 + "1" + reverse(invert(s3)) > "0111001" + "1" + 0110001 > 011100110110001
        #                                                                  011100110110001
        cur = second
        for i in range(3, n + 1):
            #print(i)
            flipped = cur[::-1]
            inverted = ""
            for f in flipped:
                if f == "1":
                    inverted += "0"
                elif f == "0":
                    inverted += "1"
            cur = cur + "1" + inverted
            #print(cur, i)
        print(cur)
        #011100110110001
        #011100110110001
        return cur[k - 1]
            
