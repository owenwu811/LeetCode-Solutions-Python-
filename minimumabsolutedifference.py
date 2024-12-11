
#1200
#easy

#Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

#a, b are from arr
#a < b
#b - a equals to the minimum absolute difference of any two elements in arr
 

#Example 1:

#Input: arr = [4,2,1,3]
#Output: [[1,2],[2,3],[3,4]]
#Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.


#my own solution using python3:

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  
        minabs = float('inf')
        for i in range(1, len(arr)):
            minabs = min(minabs, arr[i] - arr[i - 1])
        print(minabs)
        print(arr)
        res = []
        for i in range(0, len(arr) - 1):
            substr = arr[i: i + 2]
            if abs(substr[0] - substr[1]) == minabs:
                res.append([substr[0], substr[1]])
        return res
