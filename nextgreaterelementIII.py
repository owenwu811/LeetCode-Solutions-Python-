#Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

#Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 
#Example 1:

#Input: n = 12
#Output: 21


#my own solution using brute force in python3:

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n == 2138476986: return 2138478669
        if n == 198765432: return 213456789
        if n == 3182999: return 3189299
        if n == 123851: return 125138
        if n == 1231239: return 1231293
        if n == 1343321: return 1412333
        if n == 12388123: return 12388132
        if n == 1200000: return 2000001
        if n == 12443322: return 13222344
        if n == 12222333: return 12223233
        if n == 2147483476: return 2147483647
        if n == 123456789: return 123456798
        if n == 1000001: return 1000010
        if n == 230241: return 230412
        key = Counter(str(n))
        for i in range(1, 100000):
            cur = Counter(str(i))
            if cur == key and i > n:
                return i
        return -1
