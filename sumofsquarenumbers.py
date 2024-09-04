
#633


#Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

#Example 1:

#Input: c = 5
#Output: true
#Explanation: 1 * 1 + 2 * 2 = 5
#Example 2:

#Input: c = 3
#Output: false


#correct python3 solution:

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int((c + 1) ** 0.5)
        while l <= r:
            tmp = l * l + r * r
            if tmp == c:
                return True
            elif tmp < c:
                l += 1
            else:
                r -= 1
        return False
