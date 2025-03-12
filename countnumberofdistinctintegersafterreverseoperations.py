
#2442
#medium
#79.7% acceptance rate

#You are given an array nums consisting of positive integers.

#You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

#Return the number of distinct integers in the final array.

 

#Example 1:

#Input: nums = [1,13,10,12,31]
#Output: 6
#Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
#The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
#The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).


#my own solution using python3 after reading hints:

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        print(nums)
        myset = set()
        for number in nums:
            myset.add(int(number))
            myset.add(int(number[::-1]))
        return len(myset) 


#my own solution using python3 on 3/11/25:

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        c = nums.copy()
        for i, n in enumerate(nums):
            r = str(n)[::-1].lstrip("0")
            h = int(r)
            c.append(h)
        return len(set(c))
