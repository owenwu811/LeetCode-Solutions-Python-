

#1006
#medium

#The factorial of a positive integer n is the product of all positive integers less than or equal to n.

#For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
#We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.

#For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
#However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

#Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

#Given an integer n, return the clumsy factorial of n.

 

#Example 1:

#Input: n = 4
#Output: 7
#Explanation: 7 = 4 * 3 / 2 + 1

#my own solution using python3:

class Solution:
    def clumsy(self, n: int) -> int:
        self.stack = deque(["*", "//", "+", "-"])
        self.orig = self.stack.copy()
        self.cur = []
        def f(n):
            if n == 0:
                return 1 
            print(n)
            self.cur.append(str(n))
            if self.orig:
                a = self.orig.popleft()
                self.cur.append(a)
            else:
                self.orig = deque(["*", "//", "+", "-"])
                b = self.orig.popleft() 
                self.cur.append(b)
            f(n - 1)
        f(n)
        ans = "".join(self.cur[:-1])
        print(ans)
        return math.ceil(int(eval(ans)))
