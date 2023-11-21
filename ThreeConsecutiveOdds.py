#Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

#Example 1:

#Input: arr = [2,6,4,1]
#Output: false
#Explanation: There are no three consecutive odds.


#my solution - python3

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
      ws = 0
      for we in range(len(arr) - 2):
         if arr[we] % 2 != 0 and arr[we + 1] % 2 != 0 and arr[we + 2] % 2 != 0:
            return True
      return False
