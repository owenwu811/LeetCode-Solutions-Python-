
#702
#medium


#This is an interactive problem.

#You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

#returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
#returns 231 - 1 if the i is out of the boundary of the array.
#You are also given an integer target.

#Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

#You must write an algorithm with O(log n) runtime complexity.

 

#Example 1:

#Input: secret = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in secret and its index is 4.


#my own solution using python3:

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, reader.get(-1)
        print(r)
        while l <= r:
            mid = (l + r) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
