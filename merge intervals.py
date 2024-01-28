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


#my solution python3:

#the output list always has to include atleast the first element in the list of lists - [1] in this case
#output is always stretched out or new lists are added in order left to right, and so when a new list is added, the output[-1][-1] would read the 1st index of the most recently added list
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda n:n[0])
        output = [intervals[0]]
        for first, second in intervals[1:]:
            if first <= output[-1][1]:
                output[-1][1] = max(second, output[-1][1])
            else:
                output.append([first, second])
        return output

#practice run 12/25/23 - my solution:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda index: index[0])
        res = [intervals[0]]
        for first, second in intervals[1:]:
            if first <= res[-1][1]:
                res[-1][1] = max(second, res[-1][1])
            else:
                res.append([first, second])
        return res

#my solution run 12/27/23:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda sublist: sublist[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output


#1/4/24 refresher solution: 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #we sort by the 0th index of each sublist so that we know the 1st sublist's 0th index will always be the smallest element in our resulting list and that we only need to compare the 1st index element of our current sublist we are iterating over and our previous biggest sublist because we know that the 0th index is smaller than the 1st index of the sublist to the right
        intervals.sort(key=lambda n:n[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                #unpacking the 1st and 2nd values in each sublist 
                res.append([start, end])
        return res


#1/28/24 practice:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #we know that the 1st integer of the 1st sublist will always be a part of the output
        intervals.sort(key=lambda n:n[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            #we have some overlapping, and since we know that the 1st element of the previous list will be the smallest, we compare the 1st index of our current sublist and the previous sublist to see if we need to stretch
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            #no overlap, so don't stretch and just add to output
            else:
                output.append([start, end])
        return output
