

#2342
#medium

#You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

#Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

#Input: nums = [18,43,36,13,7]
#Output: 54
#Explanation: The pairs (i, j) that satisfy the conditions are:
#- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
#- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
#So the maximum sum that we can obtain is 54.


#my own solution using python3:

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        tmp = []
        for i, n in enumerate(nums):
            nums[i] = str(n)
            cur = []
            cursum = 0
            for j in range(len(nums[i])):
                cursum += int(nums[i][j])
            tmp.append([cursum, i, n])
        seen = set()
        maxsum = 0
        found = defaultdict(list)
        for t in tmp:
            if t[1] in seen:
                continue
            else:
                if t[0] in found:
                    maxsum = max(maxsum, t[2] + max(found[t[0]]))
            seen.add(t[1])
            found[t[0]].append(t[2])
        if maxsum == 0:
            return -1
        return maxsum


#what is my thought process behind this solution?

#loop through nums and track the sum of each digit, the index it's at, and the value of the original digit itself. Loop again to and ask if the index was already seen before. If so, then ignore this sublist because it can't be used. Otherwise, declare another list and keep track of the sum of the digit and the digit itself in a seperate list, and ask if the current sum has already been seen in that seperate list. If so, then add that sum from the other list to your current sum and track the maximum in a variable that will be the result.
