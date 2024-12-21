#1903
#easy

#You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

#A substring is a contiguous sequence of characters within a string.

 

#Example 1:

#Input: num = "52"
#Output: "5"
#Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
#Example 2:

#Input: num = "4206"
#Output: ""
#Explanation: There are no odd numbers in "4206".
#Example 3:

#Input: num = "35427"
#Output: "35427"
#Explanation: "35427" is already an odd number.


#my own solution using python3:

class Solution:
    
    def largestOddNumber(self, num: str) -> str:
        sys.set_int_max_str_digits(100000000)
        if int(num) % 2 != 0:
            return num
        oddindexes = []
        for i, n in enumerate(num):
            if int(n) % 2 != 0:
                oddindexes.append(i)
        print(oddindexes)
        if not oddindexes:
            return ""
        return num[:oddindexes[-1] + 1]
