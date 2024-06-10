
#Write a function that takes the binary representation of a positive integer and returns the number of 
#set bits it has (also known as the Hamming weight).


#python3 solution:

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


#5/30/24 review:

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        
#6/10/24 review:

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
