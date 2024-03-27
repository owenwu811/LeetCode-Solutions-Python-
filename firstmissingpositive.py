
#Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

#You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.





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


