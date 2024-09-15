
#1296
#medium

#Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

#Return true if it is possible. Otherwise, return false.

 

#Example 1:

#Input: nums = [1,2,3,3,4,4,5,6], k = 4
#Output: true
#Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].


#correct python3 solution:

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        freq = Counter(nums)
        for n in nums:
            if freq[n] > 0: #freq[n] = 0 means already used up all occurences of this number from input, which is required to use up all numbers from the input 
                for i in range(n, n + k): #forming a sequence of k from n
                    if freq[i] == 0: #already not possible 
                        return False
                    freq[i] -= 1 #using the number once
        return True
