#Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

#The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).



#Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
#Output: 3
#Explanation: The paths that sum to 8 are shown.

#Input: Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
#Output: 3

#my original incorrect solution - 68/129 test cases passing. failed root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 case, giving 2 instead of 3 as output:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def f(root, pathsum):
            if not root:
                pathsum = 0
                return
            pathsum += root.val
            print(pathsum)
            if pathsum > targetSum:
                pathsum = 0
            if pathsum == targetSum:
                self.res += 1
                pathsum = 0
            f(root.left, pathsum)
            f(root.right, pathsum)
        f(root, 0)
        return self.res

#correct solution in python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        
        def dfs(node, current_sum):
            if not node:
                return
            current_sum += node.val
            if current_sum == targetSum:
                self.res += 1
            # continue the path with left and right children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        def traverse(node):
            if not node:
                return
            # start a new path from the current node
            dfs(node, 0)
            traverse(node.left) #traverse(node.left) and traverse(node.right) are just starting a new path sum calculation from the left and right children
            traverse(node.right)
        
        traverse(root)
        return self.res

#why this solution is correct and what differences between my (incorrect) solution and the new (correct) solution:

#Issues with Your Solution:
#Path Reset: When pathsum exceeds targetSum, you reset pathsum to 0. This prevents paths with nodes having negative values or combinations of nodes summing up correctly from being considered.

#Single Path Consideration: The function f only considers paths from the root downwards without starting new paths from each node within the tree.

#Not Covering All Paths: If you have a tree structure and consider only the path starting from the root, you miss out on many potential paths that start from intermediate nodes.


#lesson learned: the implication is that paths can start from any node because of the description: The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

#why the new solution works:

#Why This Solution Works:

#New Paths from Each Node: The traverse function ensures that a new path sum calculation (dfs) starts from every node in the tree. This means paths starting from any node, not just the root, are considered.

#No Path Reset: The dfs function does not reset the path sum if it exceeds targetSum. It allows the path sum to continue being calculated as it traverses the tree, thus considering all combinations of node values.

#Recursive Check for All Nodes: By recursively calling dfs and traverse, this solution checks all possible paths starting from each node, ensuring all potential paths are considered.


#practice again:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #we need to consider an empty path from each and every node in the tree due to description that path does not need to start or end at the root or leaf
        #do not reset pathsum to 0 just because it's negative because future pathsums could make it exactly equal to targetsum
        self.res = 0
        def dfs(root, current_sum):
            if not root: #cannot change current_sum, so go to left subtree of traverse to start a new pathsum there with dfs(root, 0) inside of the traverse function after traverse(root.left) is called
                return #eventually, we will get here, so that's why nothing is needed after dfs(root.right, current_sum). marks branch of tree and prevents infinite recursion
            current_sum += root.val
            if current_sum == targetSum:
                self.res += 1
            dfs(root.left, current_sum) #notice we aren't resetting the current_sum just because it exceeds targetSum like you did in your incorrect solution - just letting it propogate down
            dfs(root.right, current_sum)
        def traverse(root):
            if not root:
                return
            dfs(root, 0)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.res

#6/3/24 review:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def f(root, pathsum):
            if not root:
                return
            pathsum += root.val
            if pathsum == targetSum:
                self.res += 1
            f(root.left, pathsum)
            f(root.right, pathsum)
        def traverse(root):
            if not root:
                return
            f(root, 0)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.res

#6/4/24 refresher:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(root, pathsum):
            if not root:
                return
            pathsum += root.val
            if pathsum == targetSum:
                self.res += 1
            dfs(root.left, pathsum)
            dfs(root.right, pathsum)
        
        def traverse(root):
            if not root:
                return
            dfs(root, 0)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.res
