
#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

#A subarray is a contiguous non-empty sequence of elements within an array.

# nums = [1,1,1], k = 2 - output: 2
# nums = [1,2,3], k = 3 - output: 2

#python3 solution:

#the pattern is very similar to two sum hashmap 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum, c = 0, 0
        d = dict()
        d[0] = 1
        for i in nums:
            prefixsum += i
            if prefixsum - k in d:
                c += d[prefixsum - k] #3 - 2 = 1, and k = 1, so add whatever frequency 1 exists as total number of subarrays equalling k because we don't care about duplicates
            if prefixsum in d:
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return c
#2, 4, 6, 8

#the reason we have d[0] = 1 is to check if the 1st subarray with just one element happens to equal k meaning (prefixsum - k == 0 because 0 is a key in our dictionary) to make if prefixsum - k in d true if need be
