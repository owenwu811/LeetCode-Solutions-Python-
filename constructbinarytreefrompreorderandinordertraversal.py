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
        root = TreeNode(preorder[0]) #root of tree that changes from 3 to 9 to 20 at this line...
        mid = inorder.index(preorder[0])
        #keep digging left
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) #look at ordering of method. we want just [9] as the left partition of array p (preorder[1:mid + 1]) since 1 left 3 right inside of array i after axing 3 from both p and i arrays, so this now applies 1 and 3 to the p array as well ON A SMALLER SUBSET OF P [ 9, 20, 15, 7] instead of [3, 9, 20, 15, 7], so [9] = left and [20, 15, 7] = right of array p
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) 
        return root

        #p = [3, 9, 20, 15, 7] - 3 = original root of input
        #i = [9, 3, 15, 20, 7]

        #axe 3

        #p = [ 3(axed), 9, 20, 15, 7] - corresponds to preorder[1:mid + 1] - 9 becomes root of tree instead of 3! - 1 value in left + 3 values in right (partition)
        #i = [9, 3(axed), 15, 20, 7] - corresponds to inorder[:mid] - since left (1 node) and right (3 nodes) (for i), tell us how to partition the p array! cut right after 9 in p = [3, 9, 20, 15, 7] - [9] by itself = size 1, and [20, 15, 7]  = size 3, from here, with just [9] by itself, recursively run the algorithm to create left subtree, and with [20, 15, 7], recursively run the algorithm to create the right subtree from our input. repeat this process until we get to our base cases, finish with every node we need to create

       #axe 9

       #p = [3 (axed), 9(axed), 20, 15, 7] - 20 becomes the root of the tree instead of 9!
       #i = [9 (axed), 3(axed), 15, 20, 7] 

       #axe 20 

      #p = [3 (axed), 9 (axed), 20 (axed), 15, 7] 
      #i = [9 (axed), 3 (axed), 15, 20 (axed), 7] - i has 1 left and 1 right 


    #     3
    #   9  20
    #     15 7
