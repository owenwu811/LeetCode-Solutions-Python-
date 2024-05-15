

#Reverse bits of a given 32 bits unsigned integer.

#Note:

#Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

#Input: n = 00000010100101000001111010011100
#Output:    964176192 (00111001011110000010100101000000)
#Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

#python3 solution:

#the idea here is to get the rightmost bit from n and add it to the beginning of result, and then slide result to the left

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32): #
            result = (result << 1) | (n & 1) #we want to extract the rightmost from n and add to beginning of result, and slide result to the left, not the other way around
            n //= 2 #note that bin(8) is 0b1000 while bin(4) is 0b100 - the same thing with one less zero! this is true in all divide by 2 cases!
        return result
