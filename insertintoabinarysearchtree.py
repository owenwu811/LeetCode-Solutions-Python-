
#medium

#701


#You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

#Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


#Input: root = [4,2,7,1,3], val = 5
#Output: [4,2,7,1,3,5]

#correct solution using python3:


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:                ## check if the end is reached (base case)
            return TreeNode(val)    ## add the value if the end is reached

        if val > root.val:          ## recursive call to go right
            root.right = self.insertIntoBST(root.right, val)

        elif val < root.val:        ## recursive call to go left
            root.left = self.insertIntoBST(root.left, val)  

        return root    
