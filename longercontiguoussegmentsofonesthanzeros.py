#1869
#easy

#Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

#For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
#Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

 

#Example 1:

#Input: s = "1101"
#Output: true
#Explanation:
#The longest contiguous segment of 1s has length 2: "1101"
#The longest contiguous segment of 0s has length 1: "1101"
#The segment of 1s is longer, so return true.


#my own solution using python3:

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones, zeros = [], []
        o, z = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if len(set(substr)) == 1:
                    if substr[0] == "1":
                        ones.append(substr)
                        o = max(o, len(substr))
                    elif substr[0] == "0":
                        zeros.append(substr)
                        z = max(z, len(substr))
        return o > z
