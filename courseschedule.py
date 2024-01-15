
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



#another run:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]* numCourses
        adj = [[] for x in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        for i in range(len(indegree)): # works too instead of for i in range(numCourses): but must have LEN indegree and not just range indegree
            if indegree[i] == 0:
                d.append(i)
        visited = 0
        while len(d) > 0:
            #the victims will be mapped to the attacker in the adj list, which will then be mapped to a victim in the adj list, which will then be mapped to an attacker that will be decremented by 1 in the indegree list
            node = d.popleft()
            #we could visit them becuase they have no prerequisites
            visited += 1
            #adj[node] = right side of adj list
            for victim in adj[node]:
                #indegree[victim] = top of indegree list
                indegree[victim] -= 1
                if indegree[victim] == 0:
                    d.append(victim)
        return numCourses == visited




class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses #6 0s from 0 to 5 inclusive if numCourses == 6
        #set an empty list for each node from 0 through 5 inclusive
        a = [[] for x in range(numCourses)]
        for p in prerequisites:
            a[p[1]].append(p[0])
            #pairs[0], the victim in prerequisites, is now on the right side of adjacent list, which corresponds to the bottom indexes of indegree list, so pass pairs[0] as an index inside of indegree list to get the value of indegree list, or number of attackers
            indegree[p[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        visited = 0
        while len(d) > 0:
            visited += 1
            currnode = d.popleft()
            #for (2, 4) in adj[5]
            for neighbors in a[currnode]:
             #find index 2 in the indegree list and decrement the corresponding value by 1 - do the same with index 4 since neighbors takes on 2, 4 as adj: 5: [2, 4] because out deque looks like [0, 5], which we popped 0 off, which was already processed the same way and just showing you 5's example, but our deque = [5], and we would pop 5 off, and currnode would be set to 5, and then we would let neighbor take on 2 and 4 since adj = 5: [2, 4], and then we find index 2 and 4 in indegree list and decrement the respective values by 1
                #prerequisites are satisfied when it has no pointers to this node, so we decrement the current node's attacker that has no attackers to it 
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    d.append(neighbors)
        return visited == numCourses
