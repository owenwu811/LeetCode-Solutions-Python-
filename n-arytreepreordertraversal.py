

#589
#easy

#Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

#Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

#Input: root = [1,null,3,2,4,null,5,6]
#Output: [1,3,5,6,2,4]


#my own solution using python3:

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        def f(root):
            if not root:
                return None 
            print(root.val)
            self.res.append(root.val)
            for a in root.children:
                f(a)
        f(root)
        return self.res
