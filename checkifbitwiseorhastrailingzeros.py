#2980
#easy

#You are given an array of positive integers nums.

#You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.

#For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas the binary representation of 4, which is "100", has two trailing zeros.

#Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.

 

#Example 1:

#Input: nums = [1,2,3,4,5]
#Output: true
#Explanation: If we select the elements 2 and 4, their bitwise OR is 6, which has the binary representation "110" with one trailing zero.



#my own solution using python3:

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for n in nums:
            h = bin(int(n))
            j = str(h)
            print(j)
            if j[-1] == "0":
                cnt += 1
        return cnt >= 2
