
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#Input: x = 123 Output: 321
#Input: x = -123 Output: -321
#Input: x = 120 Output: 21

#Constraints:

#-231 <= x <= 231 - 1

#python3 solution:

class Solution:
    def reverse(self, x: int) -> int:
        x_mag_reversed = int(str(abs(x))[::-1]) # for 123, you get 321. for -123, you get 321. for 120, you get 21
        limit = 2**31 #limit = 2147483648
        if x < 0 and x_mag_reversed <= limit: #for -123 input, x = -123, so x < 0 is True. x_mag_reversed = 321, so 321 <= 2147483648 (2 ^ 31) is True, so return 321 with a negative in front to get -321
            return - x_mag_reversed
        if x > 0 and x_mag_reversed < limit: #for 120 input, x = 120, xo x > 0 is True. x_mag_reversed = 21, so x_mag_reversed < limit (21454836348) is True, so return 21.
            return x_mag_reversed
        return 0

  
#3/27/24 practice:

class Solution:
    def reverse(self, x: int) -> int:
        reverse = int(str(abs(x))[::-1]) #the reason for converting an integer to a string is so we can actually seperate the digits so we can actually reverse it because [::-1] only works on reversing a string data type and not integer data type in python
        limit = 2 ** 31
        if x < 0 and reverse < limit:
            return -reverse
        elif x > 0 and reverse < limit:
            return reverse
        return 0


#Python's slice notation [::1] only works with sequences like strings, lists, and tuples. It doesn't directly apply to integers.
#By converting the integer to a string, you can treat it as a sequence of characters, making it possible to reverse the order of those characters using slicing or other techniques. Once the reversal is done, you can then convert the reversed string back to an integer if needed.


#Convert to String: str(abs(x)) is converting the absolute value of x to a string. This is done so that we can manipulate individual digits.

#Reverse the String: [::-1] is a slicing operation that reverses the string obtained from step 1. This effectively reverses the digits of the number.

#Convert Back to Integer: int(...) converts the reversed string back to an integer. This step is crucial because we need to return an integer from the function, not a string.



#3/27/24 practice again:

class Solution:
    def reverse(self, x: int) -> int:
        sx = str(abs(x))
        rs = sx[::-1]
        xr = int(rs)
        limit = 2 ** 31
        if x < 0 and xr < limit:
            return -xr
        elif x > 0 and xr < limit:
            return xr
        return 0
