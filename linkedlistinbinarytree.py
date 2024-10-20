
#1367
#medium
#52.5% acceptance rate


#Given a binary tree root and a linked list with head as the first node. 

#Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

#In this context downward path means a path that starts at some node and goes downwards.


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        tmp = []
        while head:
            tmp.append(str(head.val))
            head = head.next
        print(tmp)
        self.cur = []
        self.ans = [False]
        def f(root):
            if not root:
                return None
            self.cur.append(str(root.val))
            print("".join(self.cur))
            if "".join(tmp) in "".join(self.cur):
                self.ans[0] = True
            l = f(root.left)
            r = f(root.right)
            self.cur.pop()
        f(root)
        return self.ans[0]
