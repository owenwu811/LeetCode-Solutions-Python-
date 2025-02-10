
#Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

#You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



#my own solution using python3 on 2/10/25:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 1
        c = SortedList(nums)
        print(c)
        s = set(nums)
        for h in c:
            if start in s:
                start += 1
            else:
                return start
        return c[-1] + 1


#python3 solution:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=1 # i is set to 1 initially because that's the smallest number that could be the anwser. 1 is the smallest positive integer. if 1 is not missing from the array, then the smallest missing positive integer must be greater than 1. 
        for j in nums:
            if j<=0: #skip non positive numbers because we want the smallest positive number that is missing from the array, so negative numbers and zero are not relevant
                continue
            if i==j: #if the current element j is equal to the expected positive integer i, it means that i is inside of the array, so we increment i by 1 to check for the next positive integer that could be missing. remember that i will be the eventual result
                i+=1 
        return i

#we need nums.sort() or else we will fail test case nums = [2, 1] because we will return 2 instead of 3 because 0 dosen't count as a missing positive integer 
#the purpose of sorting is to ensure that we are going up by increments of 1 as we iterate right in the input array

#3/24/24:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for n in nums:
            if n <= 0:
                continue
            elif res == n:
                res += 1
        return res

#3/24/24 evening practice:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        result = 1
        for n in nums:
            if n <= 0:
                continue
            elif result == n:
                result += 1
        return result

#3/25/24 refresher:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort() #we must sort because we are trying to find a gap of 1 in the sequence, and if we don't find a gap, we increment by exactly 1
        result = 1
        for number in nums:
            if number <= 0:
                continue
            if result == number:
                result += 1
        return result


#3/26/24:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for number in nums:
            if number <= 0:
                continue
            elif number == res:
                res += 1
        return res


#3/27/24:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for number in nums:
            if number <= 0:
                continue
            if res == number:
                res += 1
        return res

#4/7/24:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for n in nums:
            if n <= 0:
                continue
            if n == res:
                res += 1
        return res

#4/16/24:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for n in nums:
            if n <= 0:
                continue
            elif n == res:
                res += 1
        return res
    
#4/26/24:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums.sort()
        for n in nums:
            if n <= 0:
                continue
            elif n == res: #if n == res, then that means res is INSIDE OF THE ARRAY, so increment res by 1 to check for the next positive integer that COULD be missing. 
                res += 1
        return res

#5/5/24 refresher:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result = 1
        nums.sort()
        for number in nums:
            if number <= 0:
                continue
            if number == result:
                result += 1
        return result

#5/28/24 review (my own solution):

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        nums.sort()
        for n in nums:
            if res == n:
                res += 1
            else:
                continue
        return res

#6/24/24 review (my own solution):

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for n in nums:
            if n == res:
                res += 1
            else: #
                continue
        return res

#7/27/24 refresher:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for n in nums:
            if n < 0:
                continue
            elif n == res:
                res += 1
        return res

#8/21/24 review:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums.sort()
        for n in nums:
            if n == res:
                res += 1
            else:
                continue
        return res
