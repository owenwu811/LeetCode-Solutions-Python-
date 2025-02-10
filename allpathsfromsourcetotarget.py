#797
#medium


#Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

#The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


#correct python3 solution (could not solve myself):

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        def dfs(idx, cur):
            if idx == len(graph) - 1:
                self.res.append(cur.copy())
                return 
            for nei in graph[idx]:
                cur.append(nei)
                dfs(nei, cur)
                cur.pop()
        dfs(0, [0])
        return self.res


#12/18/24 review (still could not solve again!):

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        def dfs(idx, node):
            if idx == len(graph) - 1:
                self.res.append(node.copy())
                return 
            for nei in graph[idx]:
                node.append(nei)
                dfs(nei, node) #NEI, NODE HERE BECAUSE YOU ARE VISITING IT'S NEIGHBOR, SO NEI BECOMES THE NEW INDEX
                node.pop()

        dfs(0, [0])
        return self.res


#2/9/25 review (still could not solve again):

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        def f(i, cur):
            if i == len(graph) - 1: #len(graph), not len(cur)! - i == len(graph) - 1 not len(cur) == len(graph)!
                self.res.append(cur[:])
                return 
            for a in graph[i]:
                cur.append(a)
                f(a, cur)
                cur.pop()

        f(0, [0])
        return self.res
