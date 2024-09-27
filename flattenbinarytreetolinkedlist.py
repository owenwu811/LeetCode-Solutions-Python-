
#114
#medium


#Given the root of a binary tree, flatten the tree into a "linked list":

#The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
#The "linked list" should be in the same order as a pre-order traversal of the binary tree.




#my own solution using python3 after changing it a bit from someone else's solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        d = deque()
        d.append(root)
        d.append(None)
        while d:
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    if cur.right:
                        d.appendleft(cur.right)
                    if cur.left:
                        d.appendleft(cur.left)
                    cur.left = None
                    cur.right = d[0]
        return root
