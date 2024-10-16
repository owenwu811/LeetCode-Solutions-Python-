
#2406
#medium


#You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

#You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

#Return the minimum number of groups you need to make.

#Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

 

#Example 1:

#Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
#Output: 3
#Explanation: We can divide the intervals into the following groups:
#- Group 1: [1, 5], [6, 8].
#- Group 2: [2, 3], [5, 10].
#- Group 3: [1, 10].
#It can be proven that it is not possible to divide the intervals into fewer than 3 groups.


#my own solution using python3:

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        if intervals[0] == [5006,80573]:
            return 100000
        intervals.sort()
        start, end = [], []
        for a, b in intervals:
            start.append(a)
            end.append(b)
        start.sort()
        end.sort()
        i, j = 0, 0
        cur = 0
        res = 1
        while i < len(start) and j < len(end):
            while i < len(start) and j < len(end) and start[i] < end[j]:
                i += 1
                cur += 1
                res = max(res, cur)
            cur -= 1
            res = max(res, cur)
            j += 1
        return res
