
#2869
#easy

#You are given an array nums of positive integers and an integer k.

#In one operation, you can remove the last element of the array and add it to your collection.

#Return the minimum number of operations needed to collect elements 1, 2, ..., k.

 

#Example 1:

#Input: nums = [3,1,5,4,2], k = 2
#Output: 4
#Explanation: After 4 operations, we collect elements 2, 4, 5, and 1, in this order. Our collection contains elements 1 and 2. Hence, the answer is 4.


#my own solution using python3:

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d = deque(nums)
        cur = []
        need = []
        for i in range(1, k + 1):
            need.append(i)
        res = 0
        while d:
            cur.append(d.pop())
            res += 1
            print(need, cur, res)
            flag = True
            for a in need:
                if a not in cur:
                    flag = False
            if flag:
                return res
