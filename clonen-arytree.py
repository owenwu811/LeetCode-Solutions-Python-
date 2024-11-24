
#1490 - NEED TO REVIEW BECAUSE COULD NOT SOLVE ON OWN
#medium

#Given a root of an N-ary tree, return a deep copy (clone) of the tree.

#Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

#class Node {
##    public int val;
#    public List<Node> children;
#}
#Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).


#correct python3 solution (could not solve on my own):

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        d = dict()
        def f(root):
            if not root:
                return None
            copy = Node(root.val)
            d[root] = copy
            for a in root.children:
                copy.children.append(f(a))
            return copy
        return f(root)
