
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

#4/9/24 refresher:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefixsum = 0, 0
        d = dict()
        d[0] = 1
        for i in nums:
            prefixsum += i
            if prefixsum - k in d:
                res += d[prefixsum - k]
            if prefixsum in d:
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return res


#4/9/24 refresher (missed):

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c, prefixsum = 0, 0
        d = dict()
        d[0] = 1
        for n in nums:
            prefixsum += n
            complement = prefixsum - k
            if complement in d:
                c += d[complement]
            if prefixsum in d:
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return c


#4/10/24:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefixsum = 0, 0
        d = dict()
        d[0] = 1
        for n in nums:
            prefixsum += n
            if prefixsum - k in d:
                res += d[prefixsum - k]
            if prefixsum in d:
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return res

#4/12/24:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefixsum = 0, 0
        d = dict()
        d[0] = 1
        for n in nums:
            prefixsum += n
            if prefixsum - k in d:
                res += d[prefixsum - k]
            if prefixsum in d: #if this was elif instead, when prefixsum = 3, and k = 3, we would increment res, but then we would go to the for loop instead of even evaluating this if and then the else below to add {3: 1} to the dictionary, and since prefixsum = 6, 6 - 3 is in the dictiionary, but with elif, it woudln't be because we didn't add {3: 1}, so the result is 1 less than needed for nums [1, 2, 3], k = 3
                d[prefixsum] += 1
            else:
                d[prefixsum] = 1
        return res

#4/15/24:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, subarraysum = 0, 0
        d = dict()
        d[0] = 1
        for n in nums:
            subarraysum += n
            if subarraysum - k in d:
                res += d[subarraysum - k]
            if subarraysum in d:
                d[subarraysum] += 1
            else:
                d[subarraysum] = 1
        return res

#4/17/24:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, subarraysum = 0, 0
        d = dict()
        d[0] = 1
        for n in nums:
            subarraysum += n
            if subarraysum - k in d: #{0: 1}
                res += d[subarraysum - k]
            if subarraysum in d:
                d[subarraysum] += 1
            else: #{0: 1, 1: 1}
                d[subarraysum] = 1
        return res

#4/19/24:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, subarraysum = 0, 0
        d = dict()
        d[0] = 1
        for n in nums:
            subarraysum += n
            if subarraysum - k in d:
                res += d[subarraysum - k]
            if subarraysum in d:
                d[subarraysum] += 1
            else:
                d[subarraysum] = 1
        return res

#4/22/24:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        subarraysum, res = 0, 0
        #{subarraysum: frequencyofsubarraysum}
        d[0] = 1 #in case 1st element by itself equals k
        for n in nums:
            subarraysum += n
            if subarraysum - k in d:
                res += d[subarraysum - k]
            if subarraysum not in d:
                d[subarraysum] = 1
            else:
                d[subarraysum] += 1
        return res

#4/28/24 refresher:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        res = 0
        d[0] = 1
        subarraysum = 0
        for n in nums:
            subarraysum += n
            if subarraysum - k in d:
                res += d[subarraysum - k]
            if subarraysum not in d:
                d[subarraysum] = 1
            else: 
                d[subarraysum] += 1
        return res


#4/30/24 refresher:

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, subarraysum = 0, 0
        d = {0: 1}
        for n in nums:
            subarraysum += n
            if subarraysum - k in d:
                res += d[subarraysum - k]
            if subarraysum not in d: #use if and not elif because if 1 is not key in dict, and just because 1 - 2 dosen't exist as a key in dict dosen't mean we don't insert 1 as key in dict like 1: 1 because we do, and elif would mean we don't just because -1 isn't a key in our dict for [1, 1, 1] k = 2
                d[subarraysum] = 1
            else: #we can use else here because either subarraysum is inside of d as a key or it's not - it's either or 
                d[subarraysum] += 1
        return res


#5/8/24 refresher:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #subarray has to be contiguous 
        subarraysum, res = 0, 0
        d = {0: 1} 
        for n in nums:
            subarraysum += n
            if (subarraysum - k) in d:
                res += d[subarraysum - k]
            if subarraysum not in d:
                d[subarraysum] = 1
            else:
                d[subarraysum] += 1
        return res

#5/27/24 review:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        subarraysum, res = 0, 0
        for n in nums:
            subarraysum += n #1, 2, 3
            if subarraysum - k in d:
                res += d[subarraysum - k] #res becomes 1
            if subarraysum in d:    
                d[subarraysum] += 1
            else: #{0: 1, 1: 1}
                d[subarraysum] = 1
        return res

#6/24/24 review:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = {0: 1}
        subarraysum = 0
        for n in nums:
            subarraysum += n
            if (subarraysum - k) in d:
                res += d[subarraysum - k]
            if subarraysum not in d:
                d[subarraysum] = 1
            else:
                d[subarraysum] += 1
        return res

#7/29/24 refresher:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        self.res = 0
        d = {0: 1}
        subarraysum = 0
        for n in nums:
            subarraysum += n
            if (subarraysum - k) in d: #subarraysum = 3 in final iteration of [1, 1, 1], so it's subarraysum - k, not k - subarraysum!
                self.res += d[subarraysum - k]
            if subarraysum not in d:
                d[subarraysum] = 1
            else:
                d[subarraysum] += 1

        return self.res

#9/16/24 review:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        subarraysum = 0
        res = 0
        for n in nums:
            subarraysum += n
            if (subarraysum - k) in d:
                res += d[subarraysum - k]
            if subarraysum in d:
                d[subarraysum] += 1
            else:
                d[subarraysum] = 1
        return res


