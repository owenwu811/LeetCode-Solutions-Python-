
#985
#medium

#You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

#For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

#Return an integer array answer where answer[i] is the answer to the ith query.



#my brute force solution that got TLE with 54/58 test cases passing:

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(queries)):
            nums[queries[i][1]] += queries[i][0]
            cursum = 0
            for n in nums:
                if n % 2 == 0:
                    cursum += n
            res.append(cursum)
        return res

#my own solution after looking at solution using python3:

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sumnums = 0
        for n in nums:
            if n % 2 == 0:
                sumnums += n
        for i in range(len(queries)):
            prev = nums[queries[i][1]]
            if prev % 2 == 0: #if it was even before, it was already included in original sumnums, so remove it. if it was odd before, then it was not included in original sumnums, so we can just add the new one. like 1 wouldn't be included, so if 1 becomes 2, then just add 2 to sumnums. if 2 was already included, and if 2 becomes 4, then subtract 2 before adding 4!
                sumnums -= nums[queries[i][1]] #YOU MUST REMOVE THE VALUE OF THAT FROM THE TOTSUM 
            nums[queries[i][1]] += queries[i][0]
            if nums[queries[i][1]] % 2 == 0:
                sumnums += nums[queries[i][1]]
            res.append(sumnums)
        return res
