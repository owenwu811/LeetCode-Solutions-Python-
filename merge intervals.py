#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

#Example 1:

#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].



#python3 solution:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda n:n[0])
        first = [intervals[0]]
        for a, b in intervals[1:]:
            lastbiggest = first[-1][1]
            if a <= lastbiggest:
                first[-1][1] = max(b, lastbiggest)
            else:
                first.append([a, b])
        return first
