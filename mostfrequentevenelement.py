
#easy
#50.7%acceptancerate

#Given an integer array nums, return the most frequent even element.

#If there is a tie, return the smallest one. If there is no such element, return -1.

 

#Example 1:

#Input: nums = [0,1,2,2,4,4,1]
#Output: 2
#Explanation:
#The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
#We return the smallest one, which is 2.
#Example 2:


#my own solution using python3:

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            if n % 2 == 0:
                if n not in d:
                    d[n] = 0
                d[n] += 1
        sortedd = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print(sortedd)
        maxval = 0
        for d in sortedd:
            maxval = max(maxval, sortedd[d])
        res = []
        for d in sortedd:
            if sortedd[d] == maxval:
                res.append(d)
        return min(res) if res else -1
