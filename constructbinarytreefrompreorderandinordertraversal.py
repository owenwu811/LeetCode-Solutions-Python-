#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

#preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#output: [3,9,20,null,null,15,7]




#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: #base case 
            return None
        root = TreeNode(preorder[0]) #root of tree
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) #look at ordering of method
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) 
        return root

        #p = [3, 9, 20, 15, 7] - 3 is the root of the input tree
        #i = [9, 3, 15, 20, 7]

        #axe 3

        #p = [ 3(axed), 9, 20, 15, 7] - this corresponds to preorder[1:mid + 1] - now, 9 becomes the root of the tree instead of 3! - 1 value in left + 3 values in right (partition)
        #i = [9, 3(axed), 15, 20, 7] - this corresponds to inorder[:mid] - so since left is 1 node and right is 3 nodes (for i), they tell us how to partition the p array! so we cut right after 9 in p = [3, 9, 20, 15, 7], so [9] by itself is size 1, and [20, 15, 7] is size 3, and then from here, with the [9] by itself, we will recursively run the algorithm to create the left subtree, and with [20, 15, 7], we will recursively run the algorithm to create the right subtree from our input, and we repeat this process until we get to our base cases and we finish with every node we need to create

       #axe 9

       #p = [3 (axed), 9(axed), 20, 15, 7] - now 20 becomes the root of the tree instead of 9!
       #i = [9 (axed), 3(axed), 15, 20, 7] 

       #axe 20

      #p = [3 (axed), 9 (axed), 20 (axed), 15, 7] 
      #i = [9 (axed), 3 (axed), 15, 20 (axed), 7] - notice how i has 1 left and 1 right 


    #     3
    #   9  20
    #     15 7
