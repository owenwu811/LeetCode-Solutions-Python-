

#253
#medium


#Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

#Example 1:

#Input: intervals = [[0,30],[5,10],[15,20]]
#Output: 2
#Example 2:

#Input: intervals = [[7,10],[2,4]]
#Output: 1


#my own solution using python3 after watching neetcode's explanation:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        start, end = [], []
        for a, b in intervals:
            start.append(a)
            end.append(b)
        start.sort()
        end.sort()
        i, j = 0, 0
        res = 1
        cur = 0
        print(start, end)
        while i < len(start) and j < len(end):
            while i < len(start) and j < len(end) and start[i] < end[j]:
                print(i, j)
                cur += 1
                res = max(res, cur)
                i += 1
            print(res)
            cur -= 1 #must decrement cur here because a meeting just ended!!!
            j += 1
        return res

#10/16/24 review:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 1
        intervals.sort()
        start, end = [], []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        i, j = 0, 0
        cur = 0
        start.sort()
        end.sort()
        while i < len(start) and j < len(end):
            while i < len(start) and j < len(end) and start[i] < end[j]:
                cur += 1
                i += 1
                res = max(res, cur)
            cur -= 1
            res = max(res, cur)
            j += 1
        return res
            
