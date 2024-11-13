

#3034
#medium

#You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.

#A 
#subarray
# nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

#nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
#nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
#nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
#Return the count of subarrays in nums that match the pattern.

 

#Example 1:

#Input: nums = [1,2,3,4,5,6], pattern = [1,1]
#Output: 4
#Explanation: The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3. In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
#Hence, there are 4 subarrays in nums that match the pattern.


#my own solution using python3:

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        res = 0
        windowsize = len(pattern) + 1
        for i in range(len(nums) - windowsize + 1):
            subarr = nums[i: i + windowsize]
            #print(subarr)
            flag = True
            for a in range(1, len(subarr)):
                if pattern[a - 1] == 1:
                    if not (subarr[a] > subarr[a - 1]):
                        flag = False
                elif pattern[a - 1] == 0:
                    if not (subarr[a] == subarr[a - 1]):
                        flag = False 
                elif pattern[a - 1] == -1:
                    if not (subarr[a] < subarr[a - 1]):
                        flag = False
            if flag: 
                print(subarr)
                res += 1
        return res

            #[1, 0, -1]

            #[1, 4, 4, 1]

            #1 < 4 (first < second)

            #4 == 4 (second equal to third)

            #4 > 1 (third greater than fourth)
            
            #[i + k + 1] > [i + k] pattern[k] == 1
            #[i + k + 1] == [i + k] pattern[k] == 0
            #[i + k + 1] < [i + k] pattern[k] == -1
