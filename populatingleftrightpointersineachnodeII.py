

#Given a binary tree

#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

#Initially, all next pointers are set to NULL.



#117


#correct python3 solution - essentially same as #116

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        d = deque()
        d.append(root)
        while d:
            prev = None
            for i in range(len(d)):
                cur = d.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    d.append(cur.left)
                if cur.right:
                    d.append(cur.right)
            if prev:
                prev.next = None
        return root
