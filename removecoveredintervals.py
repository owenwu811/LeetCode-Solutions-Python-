
#1288
#medium

#Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

#The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

#Return the number of remaining intervals.

 

#Example 1:

#Input: intervals = [[1,4],[3,6],[2,8]]
#Output: 2
#Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#Example 2:

#Input: intervals = [[1,4],[2,3]]
#Output: 1


#my own solution using python3:

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #[1     4]
        #   [2            8]
        #     [3        6]
        store = intervals.copy()
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    if intervals[j] in store:
                        store.remove(intervals[j])
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    if intervals[i] in store:
                        store.remove(intervals[i])
        return len(store)
