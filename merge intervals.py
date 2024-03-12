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



#2/2/24 practice:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sorting by the 1st element of each sublist, which is garunteed to have only two elements
        intervals.sort(key=lambda n:n[0])
        #the first sublist's 1st element is garunteed to be in the input list because we sorted by the 0th index of every sublist, but the 1st index element may be stretched
        output = [intervals[0]]
        #since we already inputted the 1st sublist in our result list, we can start unpacking and iterating from the 1st sublist in our input
        for start, end in intervals[1:]:
            #will be the 1st sublist's 1st index element compared to the current sublist's 0th element (2nd sublist in our input array)
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])
        return output

#2/20/24:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda n:n[0]) #to ensure that intervals[i][0] will be in output
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res

#2/26/24:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda n:n[0]) #sort each of the sublists by the 0th index value
        output = [intervals[0]] #at this point, we know that intervals[0][0] has to be the 1st element in our output list
        for first, second in intervals[1:]:
            #we are comparing to output[-1][1] because output[-1][1] is dynamic while intervals[-1][1] is static and is always the very last element in the input: intervals[-1][1] of intervals = [[1,3],[2,6],[8,10]] is 10, and intervals[-1][1] of intervals = [[1,3],[2,6],[8,10],[15,18]] is 18. This is not correct because we want to compare the current sublist's 1st index to the left one sublist's 1st index
            if first <= output[-1][1]: #there is overlap between current[0] and previous[1], so since previous[0] must be smaller than previous[1], we only need to compare previous[1] and current[1] since we want to merge current and previous and only get [smallestofboth, largestofboth] into one array
                output[-1][1] = max(output[-1][1], second)
            else:
                output.append([first, second])
        return output

#3/6/24:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda n:n[0]) #we sort each sublist by comparing the 0th index of each sublist
        output = [intervals[0]]
        for first, second in intervals[1:]:
            if first <= output[-1][1]:
                output[-1][1] = max(output[-1][1], second)
            else:
                output.append([first, second])
        return output

#3/12/24:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda n:n[0])
        output = [intervals[0]]
        for first, second in intervals[1:]:
            if first <= output[-1][1]:
                output[-1][1] = max(second, output[-1][1])
            else:
                output.append([first, second])
        return output
