

#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.





#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #the number of elements visited for far in tree
        n = 0
        stack = []
        cur = root
        #while cur is not None or stack is not empty, we will traverse our tree
        while cur or stack:
            #keep going left
            while cur:
                stack.append(cur)
                cur = cur.left
            #while loop is done executing, cur is none, so we went to far down left or right and we pop the last element we added to the stack 
            #visiting / processing the node 
            cur = stack.pop()
            n += 1
            #current node we just popped is what we are looking for 
            if n == k:
                #we are gaurunteed k nodes in our tree, so this will ALWAYS EXECUTE at some point
                return cur.val
            #just processed current node, so go right since we are traversing inorder way
            cur = cur.right


#the idea behind this is that we do a inorder traversal, adding all nodes we visit to the stack, and once we hit a None node meaning current is null, then we pop the elements in order [1, 2, 3, 4], and this makes sense because inorder, although we are visiting root left right, we are actually popping from left root right
        
#solution with clearer names:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left #returns to while cur is not None to evaluate while cur is not None again
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


#pythontutor representation:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def kth_smallest(root, k):
    n, stack, cur = 0, [], root
    while cur is not None or len(stack) > 0:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right

# Example usage:
# Constructing a sample BST
#         5
#        / \
#       3   6
#      / \
#     2   4
#      \
#       1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.right = TreeNode(1)

# Finding the kth smallest element
k = 3
print("The", k, "th smallest element is:", kth_smallest(root, k))
