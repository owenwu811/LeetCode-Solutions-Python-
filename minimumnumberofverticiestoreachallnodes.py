
#1557
#medium


#Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

#Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

#Notice that you can return the vertices in any order.

#my own solution using python3 after reading hint: We only have to count the number of nodes with zero incoming edges:

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes, attackers, ans = [], [], []
        for i in range(len(edges)):
            attackers.append(edges[i][1])
            for j in range(len(edges[i])):
                nodes.append(edges[i][j])
        print(nodes)
        print(attackers)
        print(set(nodes))
        print(set(attackers))
        g = set(nodes).difference(set(attackers))
        print(g)
        for i in g:
            ans.append(i)
        return ans
        
