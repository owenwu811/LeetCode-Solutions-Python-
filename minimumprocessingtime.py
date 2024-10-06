

#2895
#medium

#You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.

#You are given an array processorTime representing the time each processor becomes available and an array tasks representing how long each task takes to complete. Return the minimum time needed to complete all tasks.

 

#Example 1:

#Input: processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]

#Output: 16

#Explanation:

#Assign the tasks at indices 4, 5, 6, 7 to the first processor which becomes available at time = 8, and the tasks at indices 0, 1, 2, 3 to the second processor which becomes available at time = 10. 

#The time taken by the first processor to finish the execution of all tasks is max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16.

#The time taken by the second processor to finish the execution of all tasks is max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13.


#my own solution using python3:

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        groups = len(tasks) // len(processorTime)
        print(groups)
        res = 0
        tmp = deque()
        for i in range(0, len(tasks) - groups + 1, groups):
            window = tasks[i: i + groups]
            print(window)
            tmp.appendleft(window)
        print(tmp)
        for i in range(len(processorTime) -1, -1, -1):
            print(processorTime[i])
            c = []
            for j in range(len(tmp[i]) -1, -1, -1):
                print(tmp[i][j])
                c.append(processorTime[i] + tmp[i][j])
            print(c)
            res = max(res, max(c))
        return res
                

            


