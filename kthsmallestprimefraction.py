#medium
#68.7%acceptancerate


#You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

#For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

#Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

#Example 1:

#Input: arr = [1,2,3,5], k = 3
#Output: [2,5]
#Explanation: The fractions to be considered in sorted order are:
#1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
#The third fraction is 2/5.
#Example 2:

#Input: arr = [1,7], k = 1
#Output: [1,7]




#my own solution using python3:

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                res.append([arr[i], arr[j]])
        #print(res)
        myheap = []
        for i in range(len(res)):
            heapq.heappush(myheap, [res[i][0] / res[i][1], res[i]])
        #print(myheap) - the trick was to comment out the print to not get output limit exceeded with 55/59 test cases passing
        res = 0
        while k > 0:
            a, b = heapq.heappop(myheap)
            res = b
            k -= 1
        return res
