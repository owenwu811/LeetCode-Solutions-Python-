#Input: root = [1,null,2,3]
#Output: [3,2,1]

#  1
#     2
#  3

#postorder traversal follows left, right, root ordering


#python3 solution:

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def f(root):
            if not root:
                return #1's left is N, 3's left is N, 3's right is N
            l = f(root.left) #2's left is 3
            r = f(root.right) #2
            res.append(root.val) 
        f(root)
        return res #[3, 2, 1]


#8/24/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def f(root):
            if not root:
                return
            l = f(root.left)
            r = f(root.right) 
            self.res.append(root.val) #must append the root value here!

        f(root)
        return self.res
