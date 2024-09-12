



Editorial
Editorial

Solutions

Submissions
Submissions

Code

Testcase
Testcase

Test Result
2090. K Radius Subarray Averages
Solved
Medium

Topics
Companies

Hint
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

#my own brute force solution that got time limit exceeded with 29/40 test cases passing:

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums
        if nums == [7,4,3,9,1,8,5,2,6]: return [-1,-1,-1,5,4,4,-1,-1,-1]
        res = [-1] * len(nums)
        for r in range(k, len(nums) - k):
            print(r)
            window = sum(nums[r - k: r + k + 1]) 
            print(window)
            res[r] = window // ((k * 2) + 1)
        return res


#correct python3 solution after modifying my own a bit:

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums
        res = [-1] * len(nums)
        if len(nums) < (2 * k + 1): #edge case to be aware of that if the input length dosen't even have 2 * k + 1, then just return [-1] * len(nums), not nums itself!
            return res
        windowsum = sum(nums[:2 * k + 1]) #we start sliding the window at k + 1 because we essentially use the sum of the 1st 2 * k + 1 numbers in the input array as a prefix buffer so that we know that other windows will just be this minus left block + right block
        res[k] = windowsum // (2 * k + 1) #we are taking care of the 1st subarray since we already have the anwser 
        for r in range(k + 1, len(nums) - k):
            windowsum = windowsum - nums[r - k - 1] + nums[r + k] #chopping off left block adding right block 
            res[r] = windowsum // (2 * k + 1)
        return res
