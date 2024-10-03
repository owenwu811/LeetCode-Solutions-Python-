

#medium
#1448

#resources that helped a lot in leading up to me solving this question completely by myself: https://www.hellointerview.com/learn/code/depth-first-search/fundamentals


#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

#Return the number of good nodes in the binary tree.


#my own solution using python3:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.stack = []
        self.res = 0
        def f(root):
            if not root:
                return 
            self.stack.append(root.val)
            print(self.stack)
            if self.stack[-1] == max(self.stack):
                self.res += 1
            l = f(root.left)
            r = f(root.right)
            self.stack.pop()
            return root
        f(root)
        return self.res
