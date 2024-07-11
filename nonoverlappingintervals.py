
#Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#intervals = [[1,2],[2,3],[3,4],[1,3]], output - 1 because we can remove [1, 3]

#remember that the goal here is to count the the minimum frequency of intervals we must remove
#[1, 2] [2, 3] - does not count as overlap
#   -----
# -------- -----
#we would remove the left one 1 line above instead of the left one 2 lines above because we want to minimize the chances of overlapping with future intervals (one line above right one represents future intervals), so remove the one sticking out longer to the right to minimize it touching another stick in the future


#you know that each input list only has 2 elements, so only an index 0 and an index 1 in each sublist
#we are essentially comparing pairs of lists in each iteration to determine overlap and then if there is overlap, we choose one of the two pairs to remove based on which one has an earlier end to reduce chances of overlapping with future lists to the right

#python3 solution:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() #sorting by 0th index, so intervals.sort(key=lambda n:n[0]) works too and means the same thing as intervals.sort() for this problem. if 0th index ties, then sort by 1st index. if [1, 2] and [1, 2], then order dosen't matter. [1, 2], [1, 3] - 0th ties, so sort by 1st
        res = 0 # we want the minimum number of intervals, so ideally 0 because we can't remove negative intervals
        mostrecentend = intervals[0][1] #mostrecentend = 2 from [1, 2]
        for start, end in intervals[1:]:
            if start >= mostrecentend: #no overlap between current array and previous array because if start touches mostrecentend, it dosen't count - [1, 2], [2, 3]
                mostrecentend = end #move mostrecentend up to the current end so we can find potential overlaps in future comparisons between start and mostrecentend
            else: #we do have overlap, so we have to remove one or the other
                res += 1 #accounting for frequency of how many we want to remove
                mostrecentend = min(mostrecentend, end) #we remove the 1st ending one to reduce the chances of overlaps in the future, so delete the longer stick that's sticking out more to the right by only keeping the stick that's not poking out more to the right
        return res

#4/17/24 refresher:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0 #ideally, we would want to remove nothing. you can't remove negative frequency of intervals
        intervals.sort() #sort by the 0th index. if the 0th index tie, compare the 1st index. you only have 2 elements in each sublist
        prevend = intervals[0][1] 
        for start, end in intervals[1:]:
            if start >= prevend: #no overlap because [1, 2] and [2, 3] dosen't count as overlap
                prevend = end #keep moving right to catch any future potential overlaps
            else: #there is an overlap, so select the shorter stick to delete
                res += 1
                prevend = min(end, prevend) #you can think of prevend as the current end interval most recent compared one
        return res
                 
            

#4/18/24:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        #we know each input has only 2 elements in each sublit
        res = 0 #ideally, we want to remove nothing because we can't remove negative count of intervals
        prevend = intervals[0][1] 
        for start, end in intervals[1:]:
            if start >= prevend: #no overlap
                prevend = end
            else:
                res += 1 #we have to remove one or the other
                prevend = min(end, prevend) #remove shorter poking stick
        return res

#4/19/24 practice:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend: #no overlap 2] [2
                prevend = end
            else: #remove longer right pointing stick to prevent overlap since we want minimum number
                res += 1 #we must remove one log or another since there is overlap
                prevend = min(prevend, end)
        return res

#4/22/24:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                res += 1
                prevend = min(prevend, end)
        return res

#4/24/24 refresher:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                res += 1
                prevend = min(prevend, end)
        return res

#4/28/24 practice:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend: #no overlap, so set prevend to the current end so we can catch potential overlaps in the future iterations
                prevend = end
            else: #there is an overlap, so increment res, and then choose to tank the smaller log to the right to minimize the chance of overlap in the future 
                res += 1
                prevend = min(end, prevend)
        return res

#5/9/24 practice:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #how many intervals to remove to make rest non overlapping
        res = 0
        intervals.sort()
        prevend = intervals[0][1]
        for first, second in intervals[1:]:
            if prevend <= first:
                prevend = second
            else:
                res += 1
                prevend = min(prevend, second)
        return res


#5/19/24:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                res += 1
                prevend = min(prevend, end)
        return res


#6/17/24 review:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevend = [intervals[0]]
        for start, end in intervals[1:]:
            if start >= prevend[-1][1]:
                prevend[-1][1] = end
            else:
                res += 1
                prevend[-1][1] = min(prevend[-1][1], end)
        return res

#7/11/24 refresher:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevend = [intervals[0]]
        for start, end in intervals[1:]:
            if start >= prevend[-1][1]:
                prevend[-1][1] = end
            else:
                res += 1
                prevend[-1][1] = min(end, prevend[-1][1])
        return res
    
