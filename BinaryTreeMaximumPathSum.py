



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

#https://algo.monster/liteproblems/124

#when dealing with trees, recursion is often a natural approach. Since we are looking for the maximum path sum, at every node we have a choice: include that node on a path extending left or right, or start a new path through that node. 
#We can recursively find the maximum path sums going through the left child and the right child. However, when combining these sums at a node, we must realize that we cannot include both child paths since that would create a loop, not a valid path.

#The solution's intuition hinges on realizing that for any node, the maximum sum wherein that node is the highest point (i.e., the 'root' of that path) is its value plus the maximum sums of its left and right subtrees. We only add the subtree sums if they are positive, since any path would only include a subtree if it contributed positively to the total sum.

#We define the dfs function that does the following:

#When the node is None, return 0 because an empty node contributes nothing to the path sum.
#Recursively calculate the maximum path sum for the left and right subtrees. If the sum is negative, we reset it to 0, as described earlier.
#Calculate the potential maximum path sum at the current node by adding the node's value to the maximum path sums from both subtrees. This represents the largest value that could be achieved when passing through that node and potentially including both left and right paths (but not combining them).
#Update a global variable ans that tracks the overall maximum path sum found anywhere in the tree with this new potential maximum.
#Finally, for the recursion to continue upwards, return the node's value plus the greater of the two maximum sums from the left or right subtree. This represents the best contribution that node can make towards a higher path.


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


#5/19/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] #so we can modify the value inside recursive function
        def dfs(root):
            if not root: #base case
                return 0
            maxleft = dfs(root.left)
            maxright = dfs(root.right)
            #after we hit leaf node
            maxleft = max(maxleft, 0)
            maxright = max(maxright, 0)
            #considering split
            res[0] = max(res[0], root.val + maxleft + maxright)
            #value to return to parent
            return root.val + max(maxleft, maxright)

        

        dfs(root)
        return res[0]

#5/20/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def f(root):
            if root == None:
                return 0
            maxleft = f(root.left)
            maxright = f(root.right)
            maxleft = max(maxleft, 0)
            maxright = max(maxright, 0)
            res[0] = max(res[0], root.val + maxleft + maxright)
            return root.val + max(maxleft, maxright)
        f(root)
        return res[0]


#5/21/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def f(root):
            if not root:
                return 0
            maxleft = f(root.left)
            maxright = f(root.right)
            maxleft = max(maxleft, 0)
            maxright = max(maxright, 0)
            res[0] = max(res[0], root.val + maxleft + maxright)
            return root.val + max(maxleft, maxright)
        f(root)
        return res[0]


#5/29/24 review (my own solution):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def f(root):
            if root is None:
                return 0
            l = f(root.left)
            r = f(root.right)
            maxleft = max(0, l)
            maxright = max(0, r)
            res[0] = max(res[0], root.val + maxleft + maxright)
            return root.val + max(maxleft, maxright)
        f(root)
        return res[0]
        
#6/7/24 review (solved but didn't quite understand the split part):


#the actual result of the maxPathSum function can indeed be considered with the split.!

#    1
#   2 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            maxleft = max(0, l)
            maxright = max(0, r)
            res[0] = max(res[0], root.val + maxleft + maxright) #1 + 2 + 3 = 6 (actual output)
            return root.val + max(maxleft, maxright) #1 + max(2, 3) = 4
        f(root)
        return res[0] #6


#we need the line - return root.val + max(maxleft, maxright) - because this is because the maximum path sum of result also depends on having the values propagate up the tree to the root. 
#another reason why we need: return root.val + max(maxleft, maxright) - Without this line, the parent node wouldn't receive information about the best possible path sum from either of its children, causing it to miss potential paths that could contribute to a higher global sum when combined with other nodes.

        
#7/8/24 refresher: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = [root.val]
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            maxleft = max(0, l)
            maxright = max(0, r)
            self.res[0] = max(self.res[0], root.val + maxleft + maxright)
            return root.val + max(maxleft, maxright)

        f(root)
        return self.res[0]
        
