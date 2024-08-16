#Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

#Input: arr = [1,2,2,1,1,3]
#Output: true
#Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

#my own solution using python3:


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()
        for n in arr:
            if n not in d:
                d[n] = 0
            d[n] += 1
        t = []
        for k in d:
            t.append(d[k])
        if len(t) == len(set(t)):
            return True
        return False
