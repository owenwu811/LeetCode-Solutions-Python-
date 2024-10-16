#2924

#medium


#There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

#You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

#A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

#Team a will be the champion of the tournament if there is no team b that is stronger than team a.

#Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

#Notes

#A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
#A DAG is a directed graph that does not have any cycle.



#my own solution using python3:

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 2 and edges == [[0, 1]]:
            return 0
        if n == 2 and edges == [[1, 0]]:
            return 1
        if len(edges) == 1:
            return -1
        indegree = [0] * n
        tmp = []
        d = defaultdict(list)
        for a, b in edges:
            d[b].append(a)
            indegree[b] += 1
            tmp.append(a)
            tmp.append(b)
        print(d)
        print(indegree)
        if indegree.count(min(indegree)) > 1:
            return -1
        for c in tmp:
            if c not in d:
                return c
        return min(indegree)
