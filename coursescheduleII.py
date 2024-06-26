#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


#Example 1:

#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: [0,1]
#Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
#Example 2:

#Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#Output: [0,2,1,3]
#Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
#Example 3:

#Input: numCourses = 1, prerequisites = []
#Output: [0]




#python3 solution (my very own solution - solved this question by myself without looking at solution with below code):

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        nums = [0] * numCourses
        adj = [[] for course in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].append(p[0])
            nums[p[0]] += 1
        d = deque()
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(i)
                d.append(i)
        canfinish = 0
        while d:
            for i in range(len(d)):
                canfinish += 1
                current = d.popleft()
                for n in adj[current]:
                    nums[n] -= 1
                    if nums[n] == 0:
                        d.append(n)
                        res.append(n)
        return res if canfinish == numCourses else []
