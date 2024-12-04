

#2264
#easy

#You are given a string num representing a large integer. An integer is good if it meets the following conditions:

#It is a substring of num with length 3.
#It consists of only one unique digit.
#Return the maximum good integer as a string or an empty string "" if no such integer exists.

#Note:

#A substring is a contiguous sequence of characters within a string.
#There may be leading zeroes in num or a good integer.
 

#Example 1:

#Input: num = "6777133339"
#Output: "777"
#Explanation: There are two distinct good integers: "777" and "333".
#"777" is the largest, so we return "777".


#my own solution using python3:

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        tmp = []
        for i in range(len(num) - 2):
            substr = num[i: i + 3]
            if len(set(substr)) == 1:
                print(substr)
                tmp.append(substr)
        print(tmp)
        if not tmp:
            return ""
        return max(tmp)

