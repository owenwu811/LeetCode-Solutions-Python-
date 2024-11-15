
#1469
#easy

#In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

#Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

#Input: root = [1,2,3,null,4]
#Output: [4]
#Explanation: Light blue node is the only lonely node.
#Node 1 is the root and is not lonely.
#Nodes 2 and 3 have the same parent and are not lonely.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def f(root):
            if not root:
                return None 
            if root.left and not root.right:
                print(root.left.val)
                self.res.append(root.left.val)
            if root.right and not root.left:
                print(root.right.val)
                self.res.append(root.right.val)
            l = f(root.left)
            r = f(root.right)

        f(root)
        return self.res
