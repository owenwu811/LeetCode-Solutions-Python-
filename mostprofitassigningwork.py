
#You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

#difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
#worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
#Every worker can be assigned at most one job, but one job can be completed multiple times.

#For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
#Return the maximum profit we can achieve after assigning the workers to the jobs.

 

#Example 1:

#Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
#Output: 100
#Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.


#correct python3 solution:


#difficulty = [2,4,6,8,10]
#profit = [10,20,30,40,50]
#worker = [4,5,6,7]

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        pairs = sorted(zip(difficulty, profit))
        print(pairs) #[(2, 10), (4, 20), (6, 30), (8, 40), (10, 50)]
        max_profit = 0
        ans = 0
        j = 0

        for i in range(len(worker)): #each worker can only handle one job, so ans becomes 20, and we are onto worker 5. ans is 40, and we are onto worker 6. ans is 70, and we are onto worker 7.
            #worker 5 can't handle (6, 30) because 6 <= 5 is False, but worker 5 can still handle (4, 20), so ans becomes 40!
            #worker 6 can handle (6, 30) because 6 <= 6, so maxprofit becomes 30 - notice how maxprofit never gets reset because if the new worker can't handle the current job, we know they can atleast handle the previous tuple job because the input was sorted by difficult aka 1st value of each tuple!
            #worker 6 cannot handle (8, 40) because 8 <= 6 is False, so maxprofit stayed 30, and ans becomes 70 (40 + 30)
            #worker 7 cannot handle (8, 40), but since the tuples were sorted in ascending order by difficulty, we know worker 7 can atleast handle (6, 30), so maxprofit stays the same at 30, and ans becomes 100. we finished iterating through all workers, so we return 100
            while j < len(pairs) and pairs[j][0] <= worker[i]: #2 <= 4 - Yes, so max_profit becomes 10 since we are able to take that profit, but we don't add until the end because there may be bigger profits this worker can handle that we are missing out on later
                max_profit = max(max_profit, pairs[j][1]) #just because the worker can handle the current job dosen't mean we have to take it
                #j becomes 3 because we want to see if worker 6 can handle more than (6, 30)
                j += 1 #still on the same worker (4), but j now becomes (4, 20), and then 4 <= 4 - Yes, so max_profit becomes 20, but we still don't add until the end, and we increment j to 2, 6 <= 4 is False, so worker 4 can't produce profit of 30, so our while loop ends, and we add the 20 to the result (most profit worker 4 could have taken)
            ans += max_profit #it's only after the worker can't handle the job that we add to the final result the most one job that worker could handle because workers can only handle one job
        
        return ans
            
