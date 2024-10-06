
#3092
#medium
#42% acceptance rate



#Topics
#Companies

#Hint
#The problem involves tracking the frequency of IDs in a collection that changes over time. You have two integer arrays, nums and freq, of equal length n. Each element in nums represents an ID, and the corresponding element in freq indicates how many times that ID should be added to or removed from the collection at each step.

#Addition of IDs: If freq[i] is positive, it means freq[i] IDs with the value nums[i] are added to the collection at step i.
#Removal of IDs: If freq[i] is negative, it means -freq[i] IDs with the value nums[i] are removed from the collection at step i.
#Return an array ans of length n, where ans[i] represents the count of the most frequent ID in the collection after the ith step. If the collection is empty at any step, ans[i] should be 0 for that step.

 

#Example 1:

#Input: nums = [2,3,2,1], freq = [3,2,-3,1]

#Output: [3,3,2,2]

#Explanation:

#After step 0, we have 3 IDs with the value of 2. So ans[0] = 3.
#After step 1, we have 3 IDs with the value of 2 and 2 IDs with the value of 3. So ans[1] = 3.
#After step 2, we have 2 IDs with the value of 3. So ans[2] = 2.
#After step 3, we have 2 IDs with the value of 3 and 1 ID with the value of 1. So ans[3] = 2.



#my own TLE solution that passed 562/623:

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        res = []
        maxval = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += freq[i]
            res.append(max(d.values()))
        return res

#correct python3 solution: (could not solve myself and got TLE)


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        res = []
        myheap = []
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += freq[i]
            heapq.heappush(myheap, [-1 * d[nums[i]], nums[i]])
            while d[myheap[0][1]] < -1 * myheap[0][0]: #this line is critical to make sure that this line ensures that the heap always reflects the most up-to-date frequency of elements by removing any elements that no longer have the highest frequency according to the dictionary d.
                heapq.heappop(myheap)
            res.append(-1 * myheap[0][0])
        return res
