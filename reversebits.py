#Reverse bits of a given 32 bits unsigned integer.


#python3 solution:

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32): #an integer in python has 32 bits 
            #(n & 1) gets the rightmost number, and then result << 1 places that number at the front, so this below line is just a way to reverse the bits 
            result = (result << 1) | (n & 1) # (10 << 2) just adds 2 more 0s to the end of the binary representation of 10
            n //= 2
        return result


#  1010   (a in binary)
#| 0100   (b in binary)
#-------
#  1110   (result in binary)
        
#bitwise or says if 1 and 0 in a place, it defaults to 1
