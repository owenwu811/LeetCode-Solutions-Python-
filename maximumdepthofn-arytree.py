

#559
#easy

#Given a n-ary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

#Input: root = [1,null,3,2,4,null,5,6]
#Output: 3


#my own solution using python3:

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        d = deque()
        d.append(root)
        res = []
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    for a in cur.children:
                        d.append(a)
            if level:
                res.append(level)
        print(res)
        return len(res)
