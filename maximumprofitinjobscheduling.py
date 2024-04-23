#We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

#You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

#If you choose a job that ends at time X you will be able to start another job that starts at time X.

#startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]

#python3 solution:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {} #empty dictionary
        def dfs(i):
            if i >= len(intervals): #len(intervals) = 4 since intervals = [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]
                return 0
            elif i in cache:
                return cache[i]
            #don't include
            res = dfs(i + 1) #recursive call for next tuple - if we don't include the current interval, it dosen't matter what previous end was because we didn't choose previous interval
            #include 
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1)) #intervals[i][1] is the endTime of the current tuple
            cache[i] = max(res, intervals[i][2] + dfs(j)) #Calculates the maximum profit either by skipping the current job (res) or by considering the profit of the current job plus the profit obtained from the next non-overlapping job (intervals[i][2] + dfs(j)). Stores this result in the cache for future reference.
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)


#we start at i, incrementing through list until find 1st interval that dosen't overlap with previous (call this index j), and we pass j in as a parameter. 

#job and interval both mean tuple

#startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
#tuples become 
# [(1, 3, 50), #i = 0
#  (2, 4, 10), #i = 1
#  (3, 5, 40), #i = 2
#  (3, 6, 70)  #i = 3
]

# for (1, 3, 50) and (2, 4, 10), 3 > 2, so there is overlap

#2/28/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1) #don't include
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)

#2/29/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1) #not include
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            res = max(res, intervals[i][2] + dfs(j))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)

#3/1/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)


#3/4/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)

#3/6/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            res = dfs(i + 1)
            #-1, -1 are placeholder values indicating that there are no constraints on the second and third elements of the tuples in the intervals list, so this binary search is only comparing 1st element of each tuple while ignoring the 2nd and 3rd elements. 
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1)) #binary search requires list to be sorted. calling bisect function from bisect module. it is searching for the position in the intervals list where the tuple (intervals[i][1], -1, -1) would be inserted while maintaining the sorted order. intervals is assumed to be a list of tuples.
            cache[i] = max(res, intervals[i][2] + dfs(j)) 
            res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)


#3/9/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #This line creates a list of tuples by zipping together the startTime, endTime, and profit lists.
        #Each tuple represents a job interval, containing the start time, end time, and associated profit.
        #The sorted function sorts these tuples based on the start times of the jobs.
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        #This line defines a recursive function named dfs that takes an index i as its parameter.
        #The function explores all possible job combinations starting from index i.
        def dfs(i):
            #This line serves as the base case for the recursion. If the index i exceeds or equals the length of intervals, indicating that all jobs have been considered, the function returns 0.
            if i >= len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            #This line recursively calls the dfs function with the next index i + 1. It computes the maximum profit obtained by considering jobs starting from the next index.
            res = dfs(i + 1)
            #This line uses the bisect.bisect function to find the insertion point for a virtual interval. The virtual interval (intervals[i][1], -1, -1) represents a job ending at the end time of the current job i. The insertion point j indicates the index of the next non-overlapping job after job i.
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            #This line calculates the maximum profit obtained by either skipping the current job i (dfs(i + 1)) or selecting it (intervals[i][2] + dfs(j)). It memoizes the result for index i in the cache dictionary.
            cache[i] = max(res, intervals[i][2] + dfs(j))
            #This line updates the local variable res with the maximum profit obtained from considering both skipping and selecting the current job i. This step is necessary for returning the maximum profit at the end of the function.
            res = max(res, intervals[i][2] + dfs(j))
            return res


        return dfs(0)



#This solution is for the "Maximum Profit in Job Scheduling" problem, where the goal is to find the maximum profit that can be obtained by selecting a subset of non-overlapping jobs. Each job has a start time, end time, and associated profit.

#Here's how the solution works:

#Sorting Intervals: The input job information (start time, end time, profit) is zipped together into tuples and sorted based on the start time of each job. This ensures that jobs are considered in chronological order.

#Dynamic Programming with Memoization (DFS): The solution utilizes a depth-first search (DFS) with memoization to explore all possible job combinations and determine the maximum profit.

#DFS Function (dfs):

#The dfs function takes an index i as an argument, representing the current job being considered.
#If i exceeds the length of intervals, indicating that all jobs have been considered, the function returns 0 (base case).
#If i has been memoized (cached), the memoized result is returned immediately.
#Otherwise, the function calculates the maximum profit:
#Recursively calls dfs(i + 1) to explore the next job.
#Uses binary search (bisect.bisect) to find the index j of the next non-overlapping job after job i.
#Calculates the maximum profit by considering either skipping the current job (dfs(i + 1)) or selecting the current job's profit plus the maximum profit from the next non-overlapping job (intervals[i][2] + dfs(j)).
#Memoizes the result for index i.
#Returns the maximum profit.
#Return: The dfs function is called with the initial index 0, and the result is returned as the maximum profit.

#Time Complexity: The time complexity of this solution depends on the number of jobs and the efficiency of the binary search operation. It is usually O(n log n) due to the sorting step and binary search.

#Space Complexity: The space complexity is O(n) due to the memoization cache.

#In summary, this solution efficiently finds the maximum profit by exploring all possible job combinations using dynamic programming with memoization. It considers each job and recursively determines the maximum profit that can be obtained by either selecting or skipping the job, ensuring that overlapping jobs are not selected.

#The intervals list is sorted based on the start times of the jobs.
#For a given job at index i, (intervals[i][1], -1, -1) represents a virtual interval that starts at the end time of the current job i and extends infinitely forward.
#bisect.bisect(intervals, (intervals[i][1], -1, -1)) finds the insertion point for this virtual interval within the sorted intervals list.
#This insertion point j represents the index of the next interval in the sorted list that starts after the end time of the current job i.
#Therefore, j is the index of the next non-overlapping job after job i.
#In summary, bisect.bisect is used to efficiently find the index of the next non-overlapping job by considering the end time of the current job and identifying the insertion point in the sorted list of intervals. This helps in determining which jobs can be considered next without overlapping with the current job i.

#3/14/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i in cache: 
                return cache[i]
            if i >= len(intervals):
                return 0
            res = dfs(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)


#3/18/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #n number of jobs
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(intervals):
                return 0
            res = dfs(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res


        return dfs(0)


#3/22/24 practice:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(intervals):
                return 0
            res = dfs(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            res = max(res, intervals[i][2] + dfs(j))
            return res
        return dfs(0)

#3/26/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def f(i):
            if i in cache:
                return cache[i]
            elif i >= len(intervals):
                return 0
            res = f(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + f(j))
            res = max(res, intervals[i][2] + f(j))
            return res
        return f(0)

#4/5/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def f(i):
            if i >= len(intervals):
                return 0
            if i in cache:
                return cache[i]
            res = f(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + f(j))
            res = max(res, intervals[i][2] + f(j))
            return res

        return f(0)

#4/23/24:

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def f(i):
            if i in cache:
                return cache[i]
            if i >= len(intervals):
                return 0
            res = f(i + 1)
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + f(j))
            res = max(res, intervals[i][2] + f(j))
            return res
        return f(0)
