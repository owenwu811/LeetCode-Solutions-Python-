
#590
#easy

#Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

#Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

#Input: root = [1,null,3,2,4,null,5,6]
#Output: [5,6,3,2,4,1]


#my own solution using python3:

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.cur = []
        def f(root):
            if not root:
                return None  
            #print(root.val)
            for a in root.children:
                f(a)
            self.cur.append(root.val)
            


        f(root)
        return self.cur
