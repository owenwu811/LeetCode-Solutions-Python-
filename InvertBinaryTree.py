#Given the root of a binary tree, invert the tree, and return its root.


#Example 1:


#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]
#Example 2:


#Input: root = [2,1,3]
#Output: [2,3,1]
#Example 3:

#Input: root = []
#Output: []
 

#Constraints:

#The number of nodes in the tree is in the range [0, 100].
#-100 <= Node.val <= 100


#Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #here, root represents the entire binary tree as shown by the method signature, and we want to check that a tree exists before proceeding - root:Optional[TreeNode]
        if not root: #base case as terminating condition when we've reached bottom of tree. Returns None if there is not another node below the current node and applies to both the left and right tree.
            return None
        #Swap the left and right children of the current Node
        #root.right overtakes root.left, and root.left overtakes root.right
        root.left, root.right = root.right, root.left
        #Recursively invert the left and right subtrees
        #This line is just recalling the entire invertTree function except moving down one node to the left
        self.invertTree(root.left) # just means passing the new left node as an argument and executing all code in the function again
        self.invertTree(root.right)     
        return root #return root meaning return the entire tree after it's inverted because it would make sense as root is the tree itself. you can tell that root is tree because root is 4 2 7 1 3 6 9, and the picture shows that the tree consists of 4 2 7 1 3 6 9, so it makes sense that root is equal to tree or the tree itself.
        
        
 #note that, in a binary tree, the left side is smaller than the right side
        
        
 #invert binary tree basically is flipping the children and then going to the left child, and flipping (literally just swapping places) that left child's children, and then going to the right child, flipping that right child's children, and keep going until you reach the bottom of the tree.
        
 #if the three is 
 #.      a
 #      b c
 #.    d e f
 # we are flipping the 2nd level, and then we are flipping the 2nd level's children, and we keep doing this until we reach the bottom
 #       a
 #      c b
 #.    d e f
 # when a level has an odd number of nodes, the middle one stays, but the left and right are swapped, but when the level has an even number of nodes, the left becomes the right, and the right becomes the left
 # inverting means like anagram backwards, not just replacing the left side with the right side, so 1 3 6 9 should become 9 6 3 1 (backwards to forwards), not 6 9 1 3.
 
 
 #6/9/23 refresher (my solution):
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#12/25/23 refresher ( my solution with my own explanation):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if root is None, then none == none, so there's nothing to invert, so just return the root becuase it's already inverted
        #this is also base case if we hit bottom of subtree itself since, at the bottom, there's nothing to invert, so just return root for that particular function call that started it - either l or r
        if root is None:
            return root
        #swap left and right nodes at current level of tree
        root.left, root.right = root.right, root.left
        #recurvisely go down until hitting bottom of left
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        return root


#3/5/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        

#my own solution python3 4/29/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(root):
            if root == None:
                return None
            root.left, root.right = root.right, root.left
            l = f(root.left)
            r = f(root.right)
            return root
        return f(root)
