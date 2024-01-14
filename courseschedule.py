
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#Return true if you can finish all courses. Otherwise, return false.

 

#Example 1:

#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. 
#To take course 1 you should have finished course 0. So it is possible.




#tips: use the picture

#for dictlist, left side will be # of attackers while right side will be victim
#for mylist, the top will be # of attackers while bottom will be victim 
#for prerequisites list, right will be attacker while left will be victim 

# python3 solution:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mylist = [0] * numCourses
        dictlist = [[] for x in range(numCourses)]
        for p in prerequisites:
            dictlist[p[1]].append(p[0])
            mylist[p[0]] += 1
        d = deque()
        for i in range(numCourses):
            if mylist[i] == 0:
                d.append(i)
        visited = 0
        while len(d) > 0:
            node = d.popleft()
            visited += 1
            for victim in dictlist[node]:
                mylist[victim] -= 1
                if mylist[victim] == 0:
                    d.append(victim)
        return visited == numCourses


#another run:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        dictlist = [[] for attacker in range(numCourses)]
        for p in prerequisites:
            dictlist[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                d.append(i)
        visited = 0
        while len(d) > 0:
            visited += 1
            v = d.popleft()
            for victim in dictlist[v]:
                indegree[victim] -= 1
                if indegree[victim] == 0:
                    d.append(victim)
        return visited == numCourses
