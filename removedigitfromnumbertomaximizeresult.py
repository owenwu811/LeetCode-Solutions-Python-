

#2259
#easy

#You are given a string number representing a positive integer and a character digit.

#Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 

#Example 1:

#Input: number = "123", digit = "3"
#Output: "12"
#Explanation: There is only one '3' in "123". After removing '3', the result is "12".
#Example 2:

#Input: number = "1231", digit = "1"
#Output: "231"
#Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
#Since 231 > 123, we return "231".



#my own solution using python3:

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        indexes = []
        for i, n in enumerate(number):
            if n == digit:
                indexes.append(i)
        print(indexes)
        converted = list(number)
        orig = converted.copy()
        res = 0
        for a in indexes:
            converted.pop(a) 
            print(converted)
            res = max(res, int("".join(converted)))
            converted[:] = orig
        return str(res)
            
            
