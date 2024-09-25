
#1382
#medium

#Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

#A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


#my own solution using python3 after making a change from level order to inorder traversal after looking at someone's solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.res = []
        def f(root):
            if not root:
                return None
            f(root.left)
            self.res.append(root.val)
            f(root.right)
        f(root)
        ans = self.res
        print(ans)
        def f(l, r):
            if (l > r):
                return None
            mid = (l + r) // 2
            root = TreeNode(ans[mid])
            root.left = f(l, mid - 1)
            root.right = f(mid + 1, r)
            return root
        return f(0, len(ans) - 1)
