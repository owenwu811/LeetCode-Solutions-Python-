

#1650
#medium

#Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

#Each node will have a reference to its parent node. The definition for Node is below:

#class Node {
#    public int val;
#    public Node left;
#    public Node right;
#    public Node parent;
#}
#According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."


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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        one = []
        two = []
        def f(p):
            if not p:
                return
            #print(p.val)
            one.append(p.val)
            f(p.parent)


        f(p)
        def f(q):
            if not q:
                return
            #print(q.val)
            two.append(q.val)
            f(q.parent)
        f(q)
        print(one, two)
        for o in one:
            if o in two:
                return Node(o)
