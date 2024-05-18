



#A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

#The path sum of a path is the sum of the node's values in the path.

#Given the root of a binary tree, return the maximum path sum of any non-empty path.

# input: root = [-10,9,20,null,null,15,7]
# output: 42


#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #root = [-10,9,20,null,null,15,7]
        res = [root.val] #[-10]
        #return max path sum without split
        def dfs(root):
            if root == None:
                return 0
            maxleft = dfs(root.left)
            maxright = dfs(root.right)
            maxleft = max(maxleft, 0)
            maxright = max(maxright, 0)
            #compute max path sum with split
            res[0] = max(res[0], root.val + maxleft + maxright)
            return root.val + max(maxleft, maxright)
        dfs(root)
        return res[0]
            
