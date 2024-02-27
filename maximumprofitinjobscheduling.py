#We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

#You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

#If you choose a job that ends at time X you will be able to start another job that starts at time X.

#startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]

#python3 solution:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit)) #list of 3 tuples - 
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
