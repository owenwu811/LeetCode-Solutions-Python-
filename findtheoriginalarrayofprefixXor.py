

#medium
#2433
#88.0% acceptance rate

#You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

#pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
#Note that ^ denotes the bitwise-xor operation.

#It can be proven that the answer is unique.

 

#Example 1:

#Input: pref = [5,2,0,3,1]
#Output: [5,7,2,3,2]
#Explanation: From the array [5,7,2,3,2] we have the following:
#- pref[0] = 5.
#- pref[1] = 5 ^ 7 = 2.
#- pref[2] = 5 ^ 7 ^ 2 = 0.
#- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
#- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.


#my own solution using python3:

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0] * len(pref)
        res[0] = pref[0]
        fraction = pref[0]
        prefixsum = pref[0]
        for i in range(1, len(pref)):
            fraction = pref[i] ^ pref[i - 1]
            res[i] = fraction
        return res
