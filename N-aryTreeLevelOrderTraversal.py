#Given an n-ary tree, return the level order traversal of its nodes' values.

#Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

#Example 1:



#Input: root = [1,null,3,2,4,null,5,6]
#Output: [[1],[3,2,4],[5,6]]


#my own solution using python3 after understanding the node.children input:

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        d = deque()
        d.append(root)
        res = []
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    for n in cur.children: #the format is different because apparently children is just a list of values you have to iterate through, so you can't do d.append(cur.left)
                        d.append(n)
            if level:
                res.append(level)

        return res
