
#700

#easy


#You are given the root of a binary search tree (BST) and an integer val.

#Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

#Input: root = [4,2,7,1,3], val = 2
#Output: [2,1,3]


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        d = deque()
        d.append(root)
        while d:
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    if cur.val == val:
                        return cur
                    d.append(cur.left)
                    d.append(cur.right)
