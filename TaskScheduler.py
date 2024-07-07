
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
        #MAXVALUE - 1 REPRESENTS THE LAST EXECUTION OF THE MOST FREQUENTLY OCCURING LETTER 
        return max((maxvalue - 1) * (n + 1) + maxcount, len(tasks)) #last execution does not require cooldown + if n = 0, then len(tasks) will ALWAYS WIN OUT!




      #return max(mostfrequentletter - 1) * (cooldownperiod + 1) + countoflettersthathavesamefrequencyasmostfrequentletter
      # the reason we do (cooldownperiod + 1) is because each letter takes one unit of time, so it's really (cooldownperiod + timeforexecutingtask)
      # the reason we do (maxvalue - 1) is because the last execution of the most FREQUENT letter does not require a cooldown 
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


#2/22/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxcount, maxvalue = 0, max(count)
        for l in count:
            if l == maxvalue:
                maxcount += 1
        #by using addition instead of multiplication - (maxvalue - 1) + (n + 1), we would not be repeating the same letter more than once, which is wrong
        return max((maxvalue - 1) * (n + 1) + maxcount, len(tasks)) #by using addition instead of multiplication - (maxvalue - 1) + (n + 1), we would be calculating the total length of all cycles combined rather than the total time units needed to complete all cycles. This means we would be summing up the length of each cycle individually rather than considering the repetition of cycles.

#2/23/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxfreq, maxval = 0, max(count)
        for l in count:
            if l == maxval:
                maxfreq += 1
        return max((maxval - 1) * (n + 1) + maxfreq, len(tasks))


#2/25/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #task = letter
        #if we encounter a letter and another letter adjacent to it, you must wait cooling time and add this cooling time to your result
        freq = [0] * 26 #our input array can have any of the 26 letters
        for letter in tasks:
            freq[ord(letter) - ord('A')] += 1
        howmanymax, maximumfreq = 0, max(freq)
        for l in freq:
            if l == maximumfreq:
                howmanymax += 1
        #maxfreq - 1 because there is no cooling period (n) for the lastly executed most frequent task, and we want to minimize cooling period and keep cpu occupied at all times - n + 1 just means we have to account for the cooling period that was costed by trying to execute the same letter again. If n = 0, then len(tasks) will win out because cooling time was nothing, so the least time you could get was going through every letter in the array once
        return max((maximumfreq - 1) * (n + 1) + howmanymax, len(tasks))

#2/28/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #cooling time = n
        freq = [0] * 26
        for letter in tasks:
            freq[ord(letter) - ord('A')] += 1
        maxmax = max(freq)
        cntmax = 0
        for l in freq:
            if l == maxmax:
                cntmax += 1
        return max((maxmax - 1) * (n + 1) + cntmax, len(tasks))
        

#3/5/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #tasks is an array that is represented by string letters that occur between A and Z. 
        #we are given a cooling time that must be added to the total time when we process adjacent letters
        count = [0] * 26
        res = 0
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxmax, maxfreq = 0, max(count)
        for l in count:
            if l == maxfreq:
                maxmax += 1
        return max((maxfreq - 1) * (n + 1) + maxmax, len(tasks))

#3/8/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #cooling time = n
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxfreq, maxcount = 0, max(count)
        for l in count:
            if l == maxcount:
                maxfreq += 1
        # + maxfreq is for proper spacing between tasks. Tasks with the same max frequency would be executed back to back without proper cooling intervals (tasks or letters), leading to suboptimal performance. 
        # the reason we need to space out tasks with the same maximum frequency is because we want to choose to execute the tasks (letters) that occur the most frequently first to optimize performance
        return max((maxcount - 1) * (n + 1) + maxfreq, len(tasks))
     

#3/11/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #n number of intervals
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxmax, maxcount = max(count), 0
        for l in count:
            if l == maxmax:
                maxcount += 1
        return max((maxmax - 1) * (n + 1) + maxcount, len(tasks))


#3/15/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task = a letter
        #if you execute one letter right after executing the same letter, you must seperate it by n intervals, so n = the cooling time
        #we want the minimum number of intervals to complete all letters
        count = [0] * 26 #make room for all letters
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxval, howmanymax = max(count), 0
        for l in count:
            if l == maxval:
                howmanymax += 1
        #last iteration of the most frequent letter has no cooldown, so subtract 1
        return max((maxval - 1) * (n + 1) + howmanymax, len(tasks))


#3/19/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxval, howmanymax = max(count), 0
        for l in count:
            if l == maxval:
                howmanymax += 1
        return max((maxval - 1) * (n + 1) + howmanymax, len(tasks))


#3/22/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #task = letter that is processed
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxval, howmanymax = max(count), 0
        for l in count:
            if l == maxval:
                howmanymax += 1
        #must consider cooldown period
        return max((maxval - 1) * (n + 1) + howmanymax, len(tasks))


#3/25/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxval, maxcount = max(count), 0
        for l in count:
            if l == maxval:
                maxcount += 1
        return max((maxval - 1) * (n + 1) + maxcount, len(tasks))


#4/1/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #task = letter
        count = [0] * 26 #we have letters from a through z
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxval, howmanymax = max(count), 0
        for l in count:
            if l == maxval:
                howmanymax += 1
        return max((maxval - 1) * (n + 1) + howmanymax, len(tasks))

#4/13/24:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #task = letter
        #identical letters must be seperated by n intervals
        count = [0] * 26
        for letter in tasks:
            count[ord(letter) - ord('A')] += 1
        maxcnt, maxval = 0, max(count)
        for l in count:
            if l == maxval:
                maxcnt += 1
        return max((maxval - 1) * (n + 1) + maxcnt,len(tasks))


#5/13/24 refresher:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = [0] * 26
        for letter in tasks:
            res[ord(letter) - ord('A')] += 1
        maxcnt, maxval = 0, max(res)
        for l in res:
            if l == maxval:
                maxcnt += 1
        return max((maxval - 1) * (n + 1) + maxcnt, len(tasks))

#6/7/24 review:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = [0] * 26
        for letter in tasks:
            res[ord(letter) - ord('A')] += 1
        maxvalue, howmanymax = max(res), 0
        for letters in res:
            if letters == maxvalue:
                howmanymax += 1
        #howmanymax here is the idle time according to the formula given on grokking where maxval + idletime something? I also think that cooling period includes the idle time?
        return max((maxvalue - 1) * (n + 1) + howmanymax, len(tasks))

