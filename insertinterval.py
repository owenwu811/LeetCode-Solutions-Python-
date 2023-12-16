#You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

#Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

#Return intervals after the insertion.

 

#Example 1:

#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]



#Python3 solution:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #newInterval, the static list, is absolutely smaller than the current intervals list, so add newInterval first in the final result list 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: #newInterval, the static list, is absoutely bigger than the current intervals list, so add intervals list first in the final result list
                res.append(intervals[i])
            else: #the newinterval list is neither absolutely bigger or absolutely smaller than the first interval, so merge both, and this merged one will be the next sublist in the resulting list
                newInterval = [min([intervals[i][0], newInterval[0]]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval) #without this line, we would fail test case intervals = [] newInterval = [5, 7] because you would get [] as output instead of [[5, 7]] 
        return res


