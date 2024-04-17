
#Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#intervals = [[1,2],[2,3],[3,4],[1,3]], output - 1 because we can remove [1, 3]

#remember that the goal here is to count the the minimum frequency of intervals we must remove
#[1, 2] [2, 3] - does not count as overlap
#   -----
# -------- -----
#we would remove the left one 2 lines above instead of the left one one line above because we want to minimize the chances of overlapping with future intervals (one line above right one represents future intervals)


#we are essentially comparing pairs of lists in each iteration to determine overlap and then if there is overlap, we choose one of the two pairs to remove based on which one has an earlier end to reduce chances of overlapping with future lists to the right

#python3 solution:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() #sorting by 0th index. if 0th index ties, then sort by 1st index. if [1, 2] and [1, 2], then order dosen't matter. [1, 2], [1, 3] - 0th ties, so sort by 1st
        res = 0 # we want the minimum number of intervals, so ideally 0 because we can't remove negative intervals
        mostrecentend = intervals[0][1] #mostrecentend = 2 from [1, 2]
        for start, end in intervals[1:]:
            if start >= mostrecentend: #no overlap between current array and previous array because if start touches mostrecentend, it dosen't count - [1, 2], [2, 3]
                mostrecentend = end #move mostrecentend up to the current end so we can find potential overlaps in future comparisons between start and mostrecentend
            else: #we do have overlap, so we have to remove one or the other
                res += 1 #accounting for frequency of how many we want to remove
                mostrecentend = min(mostrecentend, end) #we remove the 1st ending one to reduce the chances of overlaps in the future
        return res
