
#2119
#easy

#Reversing an integer means to reverse all its digits.

#For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
#Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

 

#Example 1:

#Input: num = 526
#Output: true
#Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.


#my own solution using python3:

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num)) == 1:
            return True
        orig = str(num)
        one = orig[::-1].lstrip("0")
        print(one)
        two = one[::-1]
        return two == orig
