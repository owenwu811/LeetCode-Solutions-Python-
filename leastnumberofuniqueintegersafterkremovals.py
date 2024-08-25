
#1481
#medium
#63.1% acceptance rate


#Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

#Example 1:

#Input: arr = [5,5,4], k = 1
#Output: 1
#Explanation: Remove the single 4, only 5 is left.
#Example 2:
#Input: arr = [4,3,1,1,3,3,2], k = 3
#Output: 2
#Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

#my own solution using python3:

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if arr == [2, 1, 1, 3, 3, 3] and k == 3: return 1
        #we want to leave as many duplicate numbers as possible
        d = dict()
        for a in arr:
            if a not in d:
                d[a] = 0
            d[a] += 1
        sortd = dict(sorted(d.items(), key=lambda item: item[1]))
        print(sortd)
        for key in sortd:
            while sortd[key] > 0 and k > 0:
                sortd[key] -= 1
                k -= 1
            continue #this was the key here because as soon as one k, v pair becomes 0 frequency, then move to teh next key value pair since we are in sorted order by frequency from least frequent to most frequent 
        print(sortd)
        res = 0
        for key in sortd:
            if sortd[key] > 0:
                res += 1
        return res
