#We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

#You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

#If you choose a job that ends at time X you will be able to start another job that starts at time X.

#startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]

#python3 solution:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {} #empty dictionary
        def dfs(i):
            if i >= len(intervals): #len(intervals) = 4 since intervals = [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]
                return 0
            elif i in cache:
                return cache[i]
            #don't include
            res = dfs(i + 1) #recursive call for next tuple - if we don't include the current interval, it dosen't matter what previous end was because we didn't choose previous interval
            #include 
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1)) #intervals[i][1] is the endTime of the current tuple
            cache[i] = max(res, intervals[i][2] + dfs(j)) #Calculates the maximum profit either by skipping the current job (res) or by considering the profit of the current job plus the profit obtained from the next non-overlapping job (intervals[i][2] + dfs(j)). Stores this result in the cache for future reference.
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)


#we start at i, incrementing through list until find 1st interval that dosen't overlap with previous (call this index j), and we pass j in as a parameter. 

#job and interval both mean tuple

#startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
#tuples become 
# [(1, 3, 50), #i = 0
#  (2, 4, 10), #i = 1
#  (3, 5, 40), #i = 2
#  (3, 6, 70)  #i = 3
]

# for (1, 3, 50) and (2, 4, 10), 3 > 2, so there is overlap

#2/28/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1) #don't include
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)

#2/29/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1) #not include
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            res = max(res, intervals[i][2] + dfs(j))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)

#3/1/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)
