
#402
#medium
#33.8% acceptance rate

#Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

#Example 1:

#Input: num = "1432219", k = 3
#Output: "1219"
#Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


#monotonic stack solution:

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        #if by the time the loop finishes, if k is still greater than 0, it means we haven't removed enough digits yet. To reach the target of exactly k removals, the simplest way to remove additional digits is from the end of the current stack, which are the least beneficial in reducing the overall value of the number.
        result = stack[:-k] if k > 0 else stack
        if "".join(result).lstrip("0"):
            return "".join(result).lstrip("0")
        else:
            return "0"
