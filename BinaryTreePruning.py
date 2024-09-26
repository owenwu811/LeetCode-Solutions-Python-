
#Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

#A subtree of a node node is node plus every node that is a descendant of node.



#my own solution using python3 after looking at hint that the solution was identical to a similar question's solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(root):
            if not root:
                return 
            root.left = f(root.left) 
            root.right = f(root.right)
            #we will get here when we hit the bottom left of the tree and determined that we are a leaf on both sides
            if root.val == 0 and not root.left and not root.right:
                return None #this is the actual deletion of the node
            return root
        return f(root)


#you can think of it as starting from the bottom up since we dig all the way to the left and prune any nodes with value of 0


#         1
#        / \
#       0   1
#      /   / \
#     0   0   1
#    N N - this is when we first get to the if root.val == 0 and not root.left and not root.right because we finished with the N to the right of the bottom subtree

# after return None in the 2nd if statement, we backtrack to root.right = f(root.right), which happens to be None since the 2nd level's 0 has a right child of None, so the if root.val == 0 is visited again
