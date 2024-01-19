
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
                #prerequisites are satisfied when it has no pointers to this node, so we decrement the current node's attacker that has no attackers to it, and attackers to it were determined to be 0 because that's the only reason we appended the node onto our deque - [0, 5] means that 0 and 5 both have no attackers to them
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    d.append(neighbors)
        return visited == numCourses



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we want an array with all nodes as indexes and number of prerequisites as the values
        #if numCourses = 6, then we would have 6 0s indexes 0 through 5
        indegree = [0] * numCourses
        #adjacency list will store the dependencies on right
        adj = [[] for node in range(numCourses)]
        #which courses have which dependencies
        d = deque()
        for courses in prerequisites:
            adj[courses[1]].append(courses[0])
            indegree[courses[0]] += 1
        for index, value in enumerate(indegree):
            if value == 0:
                d.append(index)
        visitc = 0
        while len(d) > 0:
            visitc += 1
            currentnode = d.popleft()
            #for (2, 4) in adj[5]
            for node in adj[currentnode]:
                #no more attackers
                indegree[node] -= 1
                if indegree[node] == 0:
                    d.append(node)
        return visitc == numCourses

#1/15/24:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #if we have 6 courses, we want 0 from 0 through 5 - this array will be used to keep track of the courses that have no prerequisites and can add up to the result
        indegree = [0] * numCourses
        adj = [[] for node in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        for nodes in range(len(indegree)):
            if indegree[nodes] == 0:
                d.append(nodes)
        visited = 0
        while d:
            visited += 1
            currentnode = d.popleft()
            for node in adj[currentnode]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    d.append(node)
        return visited == numCourses




#again:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if we have 6 courses in total, we will have an array from 0 through 5
        indegree = [0] * numCourses
        adj = [[] for nodes in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[1]].append(sublist[0])
            indegree[sublist[0]] += 1 
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                #[0, 5] both have 0 attackers, so append them to the deque in order
                d.append(i)
        visitcount = 0
        while len(d) > 0:
            visitcount += 1
            #currentnode becomes 0 
            #currentnode becomes 5
            currentnode = d.popleft()
            #we have to make niehgbor take on every value in order in the corresponding right hand side 
            #for (2, 4) in adj[5]
            for neighbor in adj[currentnode]:
                #we then find node 5 as an index in indegree and decrement the associated value by 1, so indegree[5] -= 1
                indegree[neighbor] -= 1
                #if indegred[5] == 0, then append 5 onto the deque in order 
                if indegree[neighbor] == 0:
                    d.append(neighbor)
        return visitcount == numCourses


#1/16/24 refresher:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if we have 6 courses, we have 0 through 5 as the nodes and the number of the attackers to each node starting at 0
        indegree = [0] * numCourses
        adj = [[] for node in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].append(p[0])
            #adding attackers
            indegree[p[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        visitc = 0
        while len(d) > 0:
            visitc += 1
            currentnode = d.popleft()
            for righthandlist in adj[currentnode]:
                #removing attackers
                indegree[righthandlist] -= 1
                if indegree[righthandlist] == 0:
                    #making sure every course that has 0 attackers gets added to the deque by it's index / node value 
                    d.append(righthandlist)
        return visitc == numCourses



#1/17/24 refresher:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we assume that each course starts with no prerequisites first
        indegree = [0] * numCourses
        #if numCourses = 6, then we have an empty list on the right hand side for every key (0 through 5)
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[1]].append(sublist[0])
            #although we placed 0 in 1s place, we still have to find the node, which was the value at the left side from our prerequisites list, which corresponds with the node, which is the bottom index of our indegree list, and then we have to document that indegree's node has 1 more attacker
            indegree[sublist[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                #after we match all attackers with their victims, we check to see which courses have 0 attackers or prerequisites, and we add those courses to our deque list in order
                d.append(i)
        #while we have courses that have no attackers, we know that course can be visited and can contribute to our final result, which is if we can visit every course in our input or not
        visitc = 0
        while len(d) > 0:
            visitc += 1
            currentnode = d.popleft()
            #for (2, 4) in adj[5] if 5 = d.popleft()
            # our adjacent list looks like: 5: [2, 4]
            for neighbor in adj[currentnode]:
                #now we have to find node 2 in our indegree list and decrement it's attacker by 1: indegree[2] -= 1, and if indegree[2] == 0, then append 2 to to our deque in order. next, neighbor = 4, so we have to find node 4 and do the same process as with node 2 - indegree[4] -= 1 and if indegree[4] == 0 then append 4 to our deque in order
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    d.append(neighbor)
        return visitc == numCourses
        


#another of my slightly different solutions:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #originally, all courses are assumed to have 0 prerequisites
        indegree = [0] * numCourses
        adj = [[] for course in range(len(indegree))]
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        visitc = 0
        while len(d) > 0:
            for i in range(len(d)):
                visitc += 1
                leftside = d.popleft()
                #right side is a list
                for neighbor in adj[leftside]:
                    #will take on every node in order on the right hand side of adj list, and that new node has to be matched to an index in indegree and decrement the corresponding value by 1 - represents a cycle 
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return numCourses == visitc

