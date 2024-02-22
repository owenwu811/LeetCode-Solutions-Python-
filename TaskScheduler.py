
#Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

#However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

#Return the least number of units of times that the CPU will take to finish all the given tasks.

 

#Example 1:

#Input: tasks = ["A","A","A","B","B","B"], n = 2
#Output: 8
#Explanation: 
#A -> B -> idle -> A -> B -> idle -> A -> B
#There is at least 2 units of time between any two same tasks.




#python3 solution:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task takes one unit of time
        time = [0] * 26
        for letter in tasks:
            time[ord(letter) - ord('A')] += 1
        maxcount, maxvalue = 0, max(time)
        for char in time:
            if char == maxvalue:
                maxcount += 1
        return max((maxvalue - 1) * (n + 1) + maxcount, len(tasks))
        
