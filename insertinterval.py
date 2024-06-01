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
  
#my solution - python3 - 12/17/2023

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for List in range(len(intervals)):
            if intervals[List][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[List:]
            elif intervals[List][1] < newInterval[0]:
                res.append(intervals[List]) #we know the current list [[here]] that we are on is next in the result because even the biggest element of our current list [[here]] is smaller than the smallest element of newList
            else: #we need to stretch newInterval out because there is some overlap between newInterval and our current sublist [[here]] that we are iterating over - and then we return to the for loop - if, with the newInterval that has been merged is smaller than the next iteration of the original list of lists - [[], [here]], then append newInterval because newInterval would be the next biggest one
                newInterval = [min(intervals[List][0], newInterval[0]), max(intervals[List][1], newInterval[1])]
        res.append(newInterval) #this line of code is only to catch the case where intervals is nothing and newInterval has something, so we still have to add newInterval list to the result before returning the result 
        return res

#refresher 12/25/23 - my solution:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for lists in range(len(intervals)):
            if newInterval[1] < intervals[lists][0]:
                res.append(newInterval)
                return res + intervals[lists:]
            elif intervals[lists][1] < newInterval[0]:
                res.append(intervals[lists])
            else:
                newInterval = [min(newInterval[0], intervals[lists][0]), max(newInterval[1], intervals[lists][1])]
        res.append(newInterval)
        return res
     
#1/2/24 refresher - my solution with explanation:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for sublist in range(len(intervals)):
            #the interval we are trying to insert's biggest number is still smaller than the smallest number of our current sublist, so insert the interval first before returning the rest of our given list unaltered 
            if newInterval[1] < intervals[sublist][0]:
                res.append(newInterval)
                return res + intervals[sublist:]
            elif newInterval[0] > intervals[sublist][1]:
                res.append(intervals[sublist])
            else: #overlapping case - we stretch out both sides 
                newInterval = [min(newInterval[0], intervals[sublist][0]), max(newInterval[1], intervals[sublist][1])]
        res.append(newInterval)
        return res


#1/7/24 refresher - my solution with explanation:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for lists in range(len(intervals)):
            if newInterval[1] < intervals[lists][0]:
                res.append(newInterval)
                return res + intervals[lists:]
            elif newInterval[0] > intervals[lists][1]:
                res.append(intervals[lists])
            else:#in this case, our current sublist in our intervals input overlaps with newInterval that we want to insert into intervals, so stretch newInterval out by comparing both ends to create a new newInterval list to override the old one before inserting newInterval into intervals in future iterations based on it's proper place
                newInterval = [min(intervals[lists][0], newInterval[0]), max(intervals[lists][1], newInterval[1])]
        res.append(newInterval)
        return res


#1/15/24 refresher:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for sublist in range(len(intervals)):
            #non overlapping
            if newInterval[1] < intervals[sublist][0]:
                res.append(newInterval)
                return res + intervals[sublist:]
            #non overlapping
            elif newInterval[0] > intervals[sublist][1]:
                res.append(intervals[sublist])
            #overlapping
            else:
                newInterval = [min(newInterval[0], intervals[sublist][0]), max(newInterval[1], intervals[sublist][1])]
        res.append(newInterval)
        return res



#1/28/24 review:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #the output is a list
        res = []
        #looping and indexing into our input list
        for sublist in range(len(intervals)):
            if newInterval[0] > intervals[sublist][1]:
                #we are appending a list - intervals[sublist], not a particular integer - intervals[sublist][1]!!!!!
                res.append(intervals[sublist])
            elif newInterval[1] < intervals[sublist][0]:
                res.append(newInterval)
                return res + intervals[sublist:]
            else:
                #overlap exists, so we need to find the bigger of the two maxes and get the smallest and biggest of both sublists on both the left and side sides of both sublists and make a new newInterval sublist
                newInterval = [min(intervals[sublist][0], newInterval[0]), max(intervals[sublist][1], newInterval[1])]
        #if intervals is empty, we still need to merge them by adding just newInterval and returning result
        res.append(newInterval)
        return res

#2/5/24 refresher:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for sublist in range(len(intervals)):
            if newInterval[0] > intervals[sublist][1]:
                res.append(intervals[sublist])
            elif newInterval[1] < intervals[sublist][0]:
                res.append(newInterval)
                return res + intervals[sublist:]
            else:
                newInterval = [min(newInterval[0], intervals[sublist][0]), max(newInterval[1], intervals[sublist][1])]
        res.append(newInterval)
        return res

#2/8/24:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for sublist in range(len(intervals)):
            if newInterval[1] < intervals[sublist][0]:
                res.append(newInterval)
                return res + intervals[sublist:]
            elif newInterval[0] > intervals[sublist][1]: #we append the current input sublist, but since we haven't placed newIntervals yet, we don't return yet 
                res.append(intervals[sublist])
            else: #if the current sublist overlaps with newInterval in anyway, then we need to stretch newInterval out by the smallest of both and largest of both
                newInterval = [min(newInterval[0], intervals[sublist][0]), max(newInterval[1], intervals[sublist][1])]
        res.append(newInterval) #if intervals is [] and newInterval is [2, 5], then we still need to append newInterval to empty res list before returning 
        return res

#2/20/24:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else: #overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

#3/20/24 refresher:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res

#4/11/24 refresher:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

#5/19/24 (really struggled with and missed - had to look at solution):

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]: #no overlap - REMEMBER THAT THE TWO IF CONDITIONALS COVER CASES WHERE NO OVERLAP 
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]: #no overlap - REMEMBER 
                res.append(newInterval)
                return res + intervals[i:]
            else: #there is overlap
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res

#5/20/24 refresher:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]: #no overlap - input to left, so append current input sublist into res and keep iterating over input
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]: #no overlap - input to right, so append newInterval to res and return res with the rest of intervals
                res.append(newInterval)
                return res + intervals[i:]
            else: #is overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


#5/21/24 review:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: #there is overlap
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res

#6/1/24 review:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res



