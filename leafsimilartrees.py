
#872
#easy

#Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

#For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

#Two binary trees are considered leaf-similar if their leaf value sequence is the same.

#Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

#Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
#Output: true

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.first = []
        def f(root1):
            if not root1:
                return None 
            if not root1.left and not root1.right:
                self.first.append(root1.val)
            l = f(root1.left)
            r = f(root1.right)

        f(root1)
        self.second = []
        def f(root2):
            if not root2:
                return None
            if not root2.left and not root2.right:
                self.second.append(root2.val) 
            l = f(root2.left)
            r = f(root2.right)

        f(root2)
        print(self.first)
        print(self.second)
        return self.first == self.second
