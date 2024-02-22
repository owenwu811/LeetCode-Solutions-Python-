
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
        time = [0] * 26 # 0 - 25 with [0] for each one - counts frequency of each letter that appears from our input represented as capital letters from A to Z. Use list to store count of each task where index 0 maps to A, index 1 maps to B, etc
        for letter in tasks: #iterating through input array - ["A","A","A","B","B","B"]
            time[ord(letter) - ord('A')] += 1 #[0] becomes [1] for that particular character 
        maxcount, maxvalue = 0, max(time)
        for char in time:
            if char == maxvalue:
                maxcount += 1
        return max((maxvalue - 1) * (n + 1) + maxcount, len(tasks)) #last execution does not require cooldown + if n = 0, then len(tasks) will ALWAYS WIN OUT!




      #return max(mostfrequentletter - 1) * (cooldownperiod + 1) + countoflettersthathavesamefrequencyasmostfrequentletter
      # the reason we do (cooldownperiod + 1) is because each letter takes one unit of time, so it's really (cooldownperiod + timeforexecutingtask)
      # the reason we do (maxvalue - 1) is because the last execution of the most frequent letter does not require a cooldown 
      # idle time = cpu is inactive - we want to minimize idle time so cpu is kept busy
      # cool down time = prevents immediate re-execution of same letter AND introduces idle time for different letters
      # maxcount = count of letters with same frequency as most frequent task (most frequent letter). These letters are executed after letters with lower frequency to fill remaining idle time due to cooldown. We will idle time to keep cpu busy because each count [0] > [1] - of each letter takes 1 unit of time!
     

#2/22/24 refresher:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each letter takes one unit of time
        #we want the cpu to be occupied at all times
        time = [0] * 26
        for letter in tasks:
            time[ord(letter) - ord('A')] += 1
        maxvalue, maxfreq = max(time), 0
        for l in time:
            if l == maxvalue: maxfreq += 1
        return max((maxvalue - 1) * (n + 1) + maxfreq, len(tasks))
