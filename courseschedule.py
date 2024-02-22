
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

        mylist = [0] * numCourses #bottom = victim. top = # of attackers
        dictlist = [[] for x in range(numCourses)] #left = # of attackers, right = victim.
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


#1/19/24 practice run:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #each course from 0 through numCourse - 1 starts out with 0 prerequsites
        indegree = [0] * numCourses
        #our adjaceny list represents the course on the left and the course's naighbors on the right as a list
        adj = [[] for course in range(numCourses)]
        for p in prerequisites:
            #we have to find the right hand side of the prerequisites as the left hand side in our adhacency list and then add the left hand side of prerequisites to the right hand side of the left hand side in our adjacency list
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        #if any of the courses still have 0 attackers after the 1st round, then we can add them to our deque and increment each of them as one of the courses we can visit
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        visitcount = 0
        while len(d) > 0:
            visitcount += 1
            #we take the node from our indegree list just like with the prerequisites sublist, and we find that node in the left hand side of the adjacency list and make neighbor each of it's neighbors in the right hand side sublist, and then for each neighbor in the right sublist, we make the neighbor a node in the indegree list and decrement the corresponding count from the indegree list and repeat the process of adding the course to our deque if this new course also has 0 attackers 
            currentnode = d.popleft()
            for neighbor in adj[currentnode]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    d.append(neighbor)
        return visitcount == numCourses


#1/21/24 practice run:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #initially, each course starts off with 0 prerequisites
        indegree = [0] * numCourses
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            #we already made a list on the right for the neighbor
            #say sublist[1] = 0 because sublist is one of the sublists given in our prerequsites input, so adj[0] represents the empty sublist that has 0 as the left (key) of it 
            adj[sublist[1]].append(sublist[0])
            #now we have to document as neighbor in indegree list
            indegree[sublist[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            #if the course has 0 prerequsites even after traversing our input list prerequisites, add that course to the deque in order
            if indegree[i] == 0:
                d.append(i)
        visitcount = 0
        while len(d) > 0:
            for i in range(len(d)):
                visitcount += 1
                #currentnode = 0
                #currentnode = 5
                currentnode = d.popleft()
                #n is each of the elements in the right hand side sublist
                #(1) in adj[0]
                #(2, 4) in adj[5]
                for n in adj[currentnode]:
                    #indegree[2] -= 1
                    #indegree[4] -= 1
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        d.append(n)
        return visitcount == numCourses


#1/25/24 practice run:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #each course starts with 0 prerequisites
        indegree = [0] * numCourses
        #we start with 0 neighbors
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[1]].append(sublist[0])
            indegree[sublist[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        coursecount = 0
        while len(d) > 0:
            for i in range(len(d)):
                coursecount += 1
                currentcourse = d.popleft()
                for neighbor in adj[currentcourse]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return coursecount == numCourses
            


#1/27/24 practice run:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for course in range(numCourses)]
        for i in prerequisites:
            #append always appends to the right of a key value pair
            adj[i[1]].append(i[0])
            indegree[i[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        coursecount = 0
        while len(d) > 0:
            for i in range(len(d)):
                coursecount += 1
                currentcourse = d.popleft()
                for righthand in adj[currentcourse]:
                    indegree[righthand] -= 1
                    if indegree[righthand] == 0:
                        d.append(righthand)
        return coursecount == numCourses


#1/30/24 practice:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a depends on b
        indegree = [0] * numCourses
        #used to build neighboring prerequisites
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[1]].append(sublist[0])
            indegree[sublist[0]] += 1
        #deque list
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        canvisit = 0
        while len(d) > 0:
            for i in range(len(d)):
                canvisit += 1
                currentnode = d.popleft()
                for neighbor in adj[currentnode]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return canvisit == numCourses


#2/1/24 practice solution:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #so left depends on right
        #so each course starts with 0 prerequisites
        indegree = [0] * numCourses
        #we want to see the neighbors of the current course that will be stored in the list on the righthandside
        adjacentlist = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            adjacentlist[sublist[1]].append(sublist[0])
            # += 1 because we are saying that course now has one more dependency and won't be added to the deque 
            indegree[sublist[0]] += 1
        #used to store all courses that have 0 dependencies after we go through the entire input array once
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        visited = 0
        while len(d) > 0:
            for i in range(len(d)):
                visited += 1
                currentcourse = d.popleft()
                #for (2, 4) in adj[5]
                for neighbor in adjacentlist[currentcourse]:
                    # indegree[2] -= 1, indegree[4] -= 1
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return visited == numCourses


#2/7/24:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #each course starts with 0 dependencies
        indegree = [0] * numCourses
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[1]].append(sublist[0])
            indegree[sublist[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        visited = 0
        while d:
            #visited += 1
            for i in range(len(d)):
                visited += 1
                currentnode = d.popleft()
                for neighbor in adj[currentnode]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return visited == numCourses


#2/10/24:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if we can visit all courses, we can return True
        #indegree represents number of incoming edges towards this node (from the pluralsight course), so we start with 0 edges coming into this node aka 0 courses required for each course
        indegree = [0] * numCourses
        #creating the right hand list for each course 
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[1]].append(sublist[0])
            indegree[sublist[0]] += 1
        #all courses with 0 incoming edges will be added to the rear of the deque
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        numbercanvisit = 0
        while d:
            for i in range(len(d)): #number of iterations - one iteration for each course with 0 incoming edges
                numbercanvisit += 1
                currentnode = d.popleft()
                #for (2, 4) in adj[5] - 2 and 4 being each value taken on the right hand side of the list [2, 4]
                for neighbor in adj[currentnode]:
                    #indegree[2] -= 1 and then indegree[4] -= 1
                    indegree[neighbor] -= 1 
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return numbercanvisit == numCourses


#2/14/24:

indegree = [0] * numCourses
        adj = [[] for course in range(numCourses)]
        for sublist in prerequisites:
            #remember that we are adding INTEGERS - SUBLIST[0] - INTO THE CORRESPONDING LIST CALLED ADJ - SO 1: [0] - 0 GETS ADDED, NOT 1: [[0]] - THIS WILL THROW AN ERROR LATER IN INDEGREE[NEIGHBOR] -= 1
            adj[sublist[1]].append(sublist[0])
            indegree[sublist[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        canvisit = 0
        while d:
            for i in range(len(d)):
                canvisit += 1
                current = d.popleft()
                for neighbor in adj[current]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return canvisit == numCourses

#again:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for course in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        canvisit = 0
        while d:
            for i in range(len(d)):
                canvisit += 1
                currentnode = d.popleft()
                for neighbor in adj[currentnode]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return canvisit == numCourses
        #numCourses = 2, prerequisites = [[1,0],[0,1]] would mean that the indegree list looks like [1, 1], so since each node has one attacker, nothing goes onto the deque, which means that canvisit never changes, which means that we return False because canvisit = 0 and numCourses = 2 at the end
        
#2/15/24: (this is not BFS, SO FIFO ISN'T REQUIRED, SO POP() AND APPEND() INSTEAD OF POPLEFT() AND APPEND() WORK TOO:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #index 0 depends on 1
        indegree = [0] * numCourses #if we have 6 courses total, we want indexes 0 to 5 to be filled with 0s in our list
        adj = [[] for course in range(numCourses)] #this list is used to represent the dependencies aka attackers index 1 has in a list on the right with index 1 as the key
        for p in prerequisites: # for each sublist in our input
            adj[p[1]].append(p[0]) #find p[1] as as key in our adjacency list and add p[0] as an integer into the corresponding list 
            indegree[p[0]] += 1
        d = deque() 
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i) #FIFO NOT REQUIRED 
        canvisit = 0
        while d:
            for i in range(len(d)):
                canvisit += 1
                currentnode = d.pop() #FIFO NOT REQUIRED 
                for neighbor in adj[currentnode]:
                    indegree[neighbor] -= 1 #satisfied the course
                    if indegree[neighbor] == 0:
                        d.append(neighbor) #neighbor is an index
        return canvisit == numCourses

#2/18/24:

#if there is a cycle in our graph, it is not possible to complete all courses, and we return False. No cycle in our graph means we can return True.
#khan's algorithm to find topological sorting in a graph - algorithm fails, we have detected cycle, and we return False. each node in the ordering must appear before all nodes it points to. For the 0 depends on 2 which depends on 1 which depends on 0 example, we can't start with 0 because 1 has to come before it, and we can't start with 1 because 2 has to come before it, and we can't start with 2 because 0 has to come before it, so there is no TOPOLOGICAL SORT WITH A GRAPH CONTAINING A CYCLE.
#khan's algorithm uses a queue to traverse and keep track of nodes. first, add nodes with indegree of 0 to the queue.
#next, we remove front node of queue and visit it. then, we must delete all OUTGOING EDGES from the node we visited. We repeat this step and find all nodes with indegree of 0 and add them to the queue.
#the order in which we visited nodes is topological sorting, and since we can complete sorting, there is no cycle, and we return True
#in a failing case where we return False, we will look for nodes with an indegree of 0, AND YOU WON'T FIND ANY NODES WITH AN INDEGREE OF 0 - ALL NODES HAVE INDEGREE OF 1 OR MORE, SO SINCE QUEUE IS EMPTY, THE ALROGITHM ENDS WITHOUT US BEING ABLE TO REACH THE NODES WITH INDEGREE OF 1 OR MORE, SO TOPOLOGICAL SORT FAILS, AND WE RETURN FALSE
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #[0, 0, 0, 0, 0, 0] - if numCourses = 6
        # 0  1  2  3  4  5
        indegree = [0] * numCourses
        #2d array with adjacency list for prerequisites: 
        # adj = [ 0: [], 1: [], 2: [], 3: [], 4: [], 5: []] - indicies represent nodes, and list will be list of all neighbors
        adj = [[] for course in range(numCourses)]
        #build adjacency list - p is the sublist from input 
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0: d.append(i)
        canvisit = 0
        while d:
            for i in range(len(d)):
                canvisit += 1
                currentnode = d.popleft()
                for neighbor in adj[currentnode]:
                    indegree[neighbor] -= 1 #satisfied prerequisite
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return numCourses == canvisit


#2/22/24:

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #numCourses frequency of courses to take
        #[dependson, dependant]
        indegree = [0] * numCourses #each course starts with 0 prerequisites
        adj = [[] for course in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        d = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                d.append(i)
        canvisit = 0
        while d:
            for i in range(len(d)):
                canvisit += 1 #no prerequsities to be added to deque
                current = d.popleft()
                #for (2, 4) in adj[5]
                for neighbor in adj[current]:
                    indegree[neighbor] -= 1 #satisifed that prerequisite - indegree[2] -= 1 and indegree[4] -= 1
                    if indegree[neighbor] == 0:
                        d.append(neighbor)
        return canvisit == numCourses

