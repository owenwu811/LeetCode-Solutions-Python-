
#1791
#easy

#There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

#You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

#Input: edges = [[1,2],[2,3],[4,2]]
#Output: 2
#Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

#my own solution using python3:

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[1])
        print(d)
        maxlen = 0
        for k in d:
            maxlen = max(maxlen, len(d[k]))
        for k in d:
            if len(d[k]) == maxlen:
                return k
