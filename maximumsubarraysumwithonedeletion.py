
#Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

#Note that the subarray needs to be non-empty after deleting one element.

 

#Example 1:

#Input: arr = [1,-2,0,3]
#Output: 4
#Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

#correct python3 solution:

#the idea here is to use Kadane's algorithm, so this is similar to maximum subarray where if just by myself is greater than the entire team, then just use myself. 

#for example, let's use arr = [1, -2, 0, 3] test case:

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        cur_sum_no_del = cur_sum_del = max_sum = arr[0] #cur_sum_no_del, cur_sum_del, max_sum = 1, 1, 1 initially
        for num in arr[1:]: #start from -2, 0, 3
            cur_sum_del = max(cur_sum_del + num, num, cur_sum_no_del) #max(1 + -2, -2, 1) > 1 ([1 + -2] or [1] by itself or [-2] by itself), max(1 + 0 - excluding -2 from [1, -2, 0] subarray, 0, -1 ([1, -2] from previous) > 1, max(1 + 3 - [1, -2, 0, 3] deleting one element yeilds [1, 0, 3], which happens to be the anwser of 4, 3 - [3] itself, 0 - because [0] by itself is better than [1, -2, 0] together) > 4
            cur_sum_no_del = max(cur_sum_no_del + num, num) #max(1 + -2, -2) > -1 ([1, -2]) > best we can get is -1, max(-1 + 0, 0) > 0 (this is part where I'm better off by myself because [0] subarray is bigger than [1, -2, 0] subarray combined!), max(0 + 3, 3) > 3 - this is because [1, -2, 0, 3] - if we can't delete anything, then the biggest CONTIGUOUS subarray must include -2 if we want to include the 1 at index 0, so we choose to jsut not include the 1 at index 0 because 1 + -2 is a net negative, so we instead get sums to 3 - either [3] or [0, 3]
            max_sum = max(max_sum, cur_sum_no_del, cur_sum_del) #max(1, -1, 1) > 1, max(1, 0 - [0] by itself, 1 - [1, 0] after deleting the -2 starting from [1, -2, 0]) > 1, max(1, 3, 4) > 4 - [1, -2, 0] > just choose [1] by itself, 3 from either [0, 3] or [3], and 4 from [1, 0, 3] after we used our allowance of deleting -2 from the input [1, -2, 0, 3]
        return max_sum #return 4


#important test cases: arr = [1,-2,0,3], output = 4; arr = [2,1,-2,-5,-2], output = 3
