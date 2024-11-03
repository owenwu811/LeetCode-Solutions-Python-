
#1636
#easy

#Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

#Return the sorted array.

 

#Example 1:

#Input: nums = [1,1,2,2,2,3]
#Output: [3,1,1,2,2,2]
#Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
#Example 2:

#Input: nums = [2,3,1,3,2]
#Output: [1,3,3,2,2]
#Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
#Example 3:

#Input: nums = [-1,1,-6,4,5,-6,1,4,1]
#Output: [5,-1,4,4,-6,-6,1,1,1]


#my own solution using python3:

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        print(d)
        d = dict(sorted(d.items(),key=lambda x: x[1]))
        print(d)
        newd = defaultdict(list)
        for k in d:
            newd[d[k]].append(k)
            newd[d[k]].sort(reverse=True)
        print(newd)
        res = []
        for k in newd:
            keyval = k
            for a in newd[k]:
                while keyval > 0:
                    res.append(a)
                    keyval -= 1
                keyval = k
        print(res)
        return res
        
