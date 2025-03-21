
#1213
#easy


#Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

#Example 1:

#Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
#Output: [1,5]
#Explanation: Only 1 and 5 appeared in the three arrays.
#Example 2:

#Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
#Output: []


#my own solution using python3:

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        a = set(arr1) & set(arr2) & set(arr3)
        print(a)
        ans = []
        for i in a:
            ans.append(i)
        ans.sort()
        return ans
