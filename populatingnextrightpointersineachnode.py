#You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

#struct Node {
#  int val;
#  Node *left;
##  Node *right;
#  Node *next;
#}
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

#Initially, all next pointers are set to NULL.


#correct python3 solution:


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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: 
            return None
        d = deque()
        d.append(root)
        while d:
            prev = None
            for i in range(len(d)):
                cur = d.popleft()
                if prev: #don't need cur check because we know cur is root in 1st turn and we already have if not root check and if cur.left and if cur.right ensures that only not None get added to deque.
                    prev.next = cur #on 1st turn, this won't execute because we don't want a None type has no attribute next error
                prev = cur
                if cur.left:
                    d.append(cur.left)
                if cur.right:
                    d.append(cur.right)
            if prev: #seperation of levels
                prev.next = None
        return root


#9/21/24 review: (was able to re-solve without much difficulty)


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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
                prev = prev.next
        return root
