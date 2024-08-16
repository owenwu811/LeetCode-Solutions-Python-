#Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

#Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
#Output: [3,9,20,null,null,15,7]

#python3 solution:

#Inorder Traversal: This is a depth-first traversal where the order of visiting nodes is left subtree → root → right subtree.
#Postorder Traversal: This is also a depth-first traversal where the order is left subtree → right subtree → root. (important to know)

#Finding the Root in Inorder:
#To divide the inorder list into left and right subtrees, the position of the root node in inorder is determined.
#mid = inorder.index(root.val) finds this position (mid), where:
#inorder[:mid] represents the left subtree.
#inorder[mid+1:] represents the right subtree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder.pop()) #The last element in the postorder list is always the root of the current subtree because postorder traversal processes the root node last!
        mid=inorder.index(root.val)
        root.left=self.buildTree(inorder[:mid],postorder[:mid])
        root.right=self.buildTree(inorder[mid+1:],postorder[mid:])
        return root


#Why postorder[mid:] Is Correct
#In the recursive call for the right subtree of 20, we use postorder[mid:] to include all elements that are part of the right subtree, as well as its root.

#What Happens If We Use postorder[mid + 1:]?
#If we incorrectly use postorder[mid + 1:]:

#In the call for the right subtree of 20:
#inorder = [15, 20, 7]
#The correct postorder segment should be [15, 7, 20].
#If we use postorder[mid + 1:], we would skip over the necessary elements, incorrectly slicing the list and missing 20, which leads to an incomplete or incorrect tree structure.
#Using postorder[mid + 1:] would shift the segment and omit the root of the right subtree, causing errors in tree reconstruction. This is why postorder[mid:] is essential for correctly aligning the elements with the respective subtrees.
