#You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

#Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

 

#Example 1:

#Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
#Output: 13 
#Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 

#medium
#1508

#correct solution using python3:

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        tmp = []
        subarraysum = 0
        for i in range(len(nums)):
            subarraysum = 0
            for j in range(i, len(nums)):
                subarraysum += nums[j] #you don't add nums[i][j] because this isn't a matrix! this is the way to get the subarray sums!
                tmp.append(subarraysum)
        tmp.sort()
        return sum(tmp[left - 1: right]) % ((10 ** 9) + 7)



#my own solution using python3 on 3/11/25:

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = (10 ** 9) + 7
        cur = []
        for i in range(len(nums)):
            ss = 0
            for j in range(i, len(nums)):
                ss += nums[j]
                cur.append(ss)
        cur.sort()
        a = cur[left - 1:right]
        return sum(a) % mod
       #return sum(cur[nums[left - 1:right]])
