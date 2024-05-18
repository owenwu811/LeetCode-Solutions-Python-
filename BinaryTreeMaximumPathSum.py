



#A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

#The path sum of a path is the sum of the node's values in the path.

#Given the root of a binary tree, return the maximum path sum of any non-empty path.

# input: root = [-10,9,20,null,null,15,7]
# output: 42


#my solution that passed only 42/96 test cases: - failed root = [-10,9,20,null,null,15,7], giving 51 instead of 42 as output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #since they have to be connected, we do an inorder traversal at each level and add the total
        self.res = 0
        self.maxpath = 0
        def f(root):
            #question is how to handle null case?
            #root = [-10,9,20,null,null,15,7] - we should get 42 instead of 51 you are getting
            if root == None:
                return 0
            elif root.val > 0:
                self.res += root.val
                self.maxpath = max(self.maxpath, self.res) #maxpath becomes 9
            elif root.val <= 0:
                self.res += 0
                self.maxpath = max(self.maxpath, self.res)
                #problem here because if actual root of input tree is negative, we return 0 because it goes back to original recursive call
                #return 0 #if this block executes for the kickoff recursive call, where does the control flow go?
            l = f(root.left)
            r = f(root.right)
            return 1 + max(l, r)
        f(root)
        return self.maxpath
    


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
            #line below represents all left children of every node
            maxleft = dfs(root.left) #9, N > return value 0 | 15 (20s left child aka 20 recursive call came from maxright = dfs(root.right), N (15s left child) > return value 0 | N > return value 0 
            #line below represents all right children of every node
            maxright = dfs(root.right) #N (right child of 9) > return value 0 | 20 (after coming from return root.val + max(maxleft, maxright) line, N (15s right child) > return value 0 | 7 N > return value 0 
            maxleft = max(maxleft, 0) #0 0 0 maxleft becomes 15 after we hit bottom leaf of 15 (coming from return root.val + max(maxleft, maxright) where the return value will be 15 - the starter of this recursive call that returns 15 eventually is "maxright = dfs(root.right)"
            maxright = max(maxright, 0) #0 0 0 maxright becomes 7 after we hit bottom of leaf 7 (coming from return root.val + max(maxleft, maxright) where the return value will be 7
            #compute max path sum with split
            res[0] = max(res[0], root.val + maxleft + maxright) #-10, 9, 15, 42
            return root.val + max(maxleft, maxright) #9, 15, 7, 35, 25
        dfs(root)
        return res[0]


#             -10
#            9   20
#              15   7
