

#2323
#medium

#You are given two 0-indexed integer arrays jobs and workers of equal length, where jobs[i] is the amount of time needed to complete the ith job, and workers[j] is the amount of time the jth worker can work each day.

#Each job should be assigned to exactly one worker, such that each worker completes exactly one job.

#Return the minimum number of days needed to complete all the jobs after assignment.

 

#Example 1:

#Input: jobs = [5,2,4], workers = [1,7,5]
#Output: 2
#Explanation:
#- Assign the 2nd worker to the 0th job. It takes them 1 day to finish the job.
#- Assign the 0th worker to the 1st job. It takes them 2 days to finish the job.
#- Assign the 1st worker to the 2nd job. It takes them 1 day to finish the job.
#It takes 2 days for all the jobs to be completed, so return 2.
#It can be proven that 2 days is the minimum number of days needed.


#my own solution using python3:

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort(reverse=True)
        workers.sort(reverse=True)
        print(jobs)
        print(workers)
        res = []
        for i, w in enumerate(workers):
            if workers[i] < jobs[i]:
                print(workers[i], jobs[i])
                print(math.ceil(jobs[i] / workers[i]))
                res.append(math.ceil(jobs[i] / workers[i]))
        print(res)
        if not res:
            return 1
        return max(res)


        
