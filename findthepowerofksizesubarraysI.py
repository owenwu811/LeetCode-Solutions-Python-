
#medium
#53.4% acceptance rate
#3254


#You are given an array of integers nums of length n and a positive integer k.

#The power of an array is defined as:

#Its maximum element if all of its elements are consecutive and sorted in ascending order.
#-1 otherwise.
#You need to find the power of all 
#subarrays
# of nums of size k.

#Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].


#my own solution using python3:

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            window = nums[i: i + k]
            print(window)
            if window == sorted(window) and max(window) - min(window) == len(window) - 1 and len(window) == len(set(window)):
                res.append(max(window))
            else:
                res.append(-1)
        return res
