


#2155
#medium

#You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:

#numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
#If i == 0, numsleft is empty, while numsright has all the elements of nums.
#If i == n, numsleft has all the elements of nums, while numsright is empty.
#The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.

#Return all distinct indices that have the highest possible division score. You may return the answer in any order.

 

#Example 1:

#Input: nums = [0,0,1,0]
#Output: [2,4]
#Explanation: Division at index
#- 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.
#- 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
#- 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
#- 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
#- 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
#Indices 2 and 4 both have the highest possible division score 3.
#Note the answer [4,2] would also be accepted.


#my own solution using python3:

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        #0 in left + 1 in right
        b = Counter(nums)
        f = defaultdict(int)
        t = defaultdict(list)
        for i in range(len(nums)):
            b[nums[i]] -= 1
            f[nums[i]] += 1
            cur = f[0] + b[1]
            t[cur].append(i + 1)
        tot = Counter(nums)
        first = tot[1]
        last = tot[0]
        #print(first, last)
        #print(t)
        t[first].append(0)
        t[last].append(len(nums))
        target = max(t.keys())
        new = set()
        for a in t[target]:
            new.add(a)
        print(new)
        return list(new)
