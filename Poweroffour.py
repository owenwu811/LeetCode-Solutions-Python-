#342. Power of Four
#Easy
#3.7K
#369
#Companies
#Given an integer n, return true if it is a power of four. Otherwise, return false.

#An integer n is a power of four, if there exists an integer x such that n == 4x.

 

#Example 1:

#Input: n = 16
#Output: true
#Example 2:

#Input: n = 5
#Output: false
#Example 3:

#Input: n = 1
#Output: true
 

#Constraints:

#-231 <= n <= 231 - 1
 

#Follow up: Could you solve it without loops/recursion?
#Accepted
#580.6K
#Submissions
#1.2M
#Acceptance Rate
#47.5%
#Seen this question in a real interview before?
#1/4

#My own brute force solution (Python3):

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4 or n == 16 or n == 64 or n == 256 or n == 1024 or n == 4096 or n == 16384 or n == 65536 or n == 262144 or n == 1048576 or n == 4194304 or n == 16777216 or n == 67108864 or n == 268435456 or n == 1073741824:
            return True
        if n % 4 == 4 and n >= 1:
            return True
        else:
            return False
        # 8 == 4^2
        # 4 ^ 2 = 16, so false, but you returned true
        # 0, 1, 4, 16, 64, 256, 1024, 4096, 16384 - these test cases are not passing now
        #4^1, 4^2, 4^3, 4^4, 4^5, 4^6
        #16, 64, 256, 1024 == 4^x should return true
