

#510
#medium

#Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

#The successor of a node is the node with the smallest key greater than node.val.

#You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

#class Node {
#    public int val;
#    public Node left;
#    public Node right;
#    public Node parent;
#}



#my own solution using python3:


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        self.cur = []
        self.seen = set()
        def f(node):
            if not node or node.val in self.seen:
                return None
            print(node.val)
            self.cur.append(node.val)
            self.seen.add(node.val)
            f(node.right)
            f(node.left)
            f(node.parent)
        f(node)
        print(self.cur)
        self.cur.sort()
        if self.cur:
            if node.val == max(self.cur):
                return None
        for c in self.cur:
            if c > node.val:
                return Node(c)


