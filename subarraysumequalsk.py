
#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

#A subarray is a contiguous non-empty sequence of elements within an array.

# nums = [1,1,1], k = 2 - output: 2
# nums = [1,2,3], k = 3 - output: 2

#python3 solution:

# [1, 1]
#    [1, 1]
# both above sum up to 2, and k = 2, so we have 2 subarrays that are CONTIGUOUS and sum up to k

#[1, 1, 1], k = 2

# dictinoary looks like this for above test case: {0: 1, 1: 1, 2: 1, 3: 1}

#my own test case for negatives: [2, 1, -3], k = 1 - output: 1
#so if (3 - 1) in d, which 2 is in d, so True because {0: 1, 2: 1}

#the pattern is very similar to two sum hashmap 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum, c = 0, 0
        d = dict()
        d[0] = 1
        for i in nums:
            prefixsum += i
            if prefixsum - k in d:
                c += d[prefixsum - k] #3 - 2 = 1, and k = 1, so add whatever frequency 1 exists as total number of subarrays equalling k because we don't care about duplicates. duplicates still count towards result.
            if prefixsum in d:
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return c
#2, 4, 6, 8

#the reason we have d[0] = 1 is to check if the 1st subarray with just one element happens to equal k meaning (prefixsum - k == 0 because 0 is a key in our dictionary) to make if prefixsum - k in d true if need be

#d[prefixsum]=1 - and the idea here is that our prefix sum dosen't exist as a key in our dictionary, so add it so that, in the future, when we add even more elements, we can use the key we just added to see if that key we just added is a potential complement to make prefixsum - k = 0 in the future iterations
