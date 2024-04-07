
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

#3/28/24:

class Solution:
    def reverse(self, x: int) -> int:
        rv = str(abs(x))
        r = rv[::-1]
        a = int(r)
        limit = 2 ** 31
        if x < 0 and a < limit:
            return -a
        elif x > 0 and a < limit:
            return a
        return 0


#4/1/24:

class Solution:
    def reverse(self, x: int) -> int:
        #x = -123
        g = abs(x) #123 instead of -123
        s = str(g) #"123"
        r = s[::-1] #"321"
        final = int(r) #321
        limit = 2 ** 31
        #we want to add the - back to the FRONT OF "321"
        if x < 0 and final < limit: #if reversing x causes value to go outside signed range
            return -final #-321"
        elif x > 0 and final < limit: #final < limit because the problem says AFTER REVERSING X causes value to go outside signed range
            return final
        return 0

#practice again:

class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x) #-123 to 123
        s = str(a) # 123 to "123"
        b = s[::-1] #"123"" to "321"
        f = int(b) #"321" to 321
        limit = 2 ** 31
        if x < 0 and f < limit:
            return -f #321 to -321
        elif x > 0 and f < limit:
            return f 
        return 0

        

#we must do abs(x) first! otherwise, you would get 321- instead of -123 and a ValueError because '321-' cannot be converted to an integer!

#Suppose x = -123.

#With s = abs(x):

#s = abs(-123) = 123
#r = str(123) = '123'
#a = r[::-1] = '321'
#b = int('321') = 321
#Since x < 0, and b = 321 which is less than 2 ** 31, we return -b, so the result is -321.
#Without s = abs(x):

#r = str(-123) = '-123'
#a = r[::-1] = '321-' (Note: Reversed string includes the negative sign)
#b = int('321-') would raise a ValueError because '321-' cannot be converted to an integer.
#So, without taking the absolute value, the reversed string includes the negative sign, leading to incorrect results when converting it back to an integer.

#4/2/24:

class Solution:
    def reverse(self, x: int) -> int:
        d = abs(x)
        f = str(d)
        g = f[::-1]
        a = int(g)
        limit = 2 ** 31
        if x > 0 and a < limit:
            return a
        elif x < 0 and a < limit:
            return -a
        return 0

#4/3/24 refresher:

class Solution:
    def reverse(self, x: int) -> int:
        #-123 > 123 > "123" > "321" > - 321
        g = abs(x) #prevents integer error for 321- being converted back to integer later on
        s = str(g)
        h = s[::-1]
        f = int(h) #321
        limit = 2 ** 31
        if x > 0 and f < limit: 
            return f
        if x < 0 and f < limit:
            return -f #-321
        return 0

#4/7/24:

class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        s = str(a)
        r = s[::-1]
        f = int(r)
        limit = 2 ** 31
        if x < 0 and f < limit:
            return -f
        if x > 0 and f < limit:
            return f
        return 0
