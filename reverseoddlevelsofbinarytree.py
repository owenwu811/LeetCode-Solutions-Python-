#Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

#For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
#Return the root of the reversed tree.

#A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

#The level of a node is the number of edges along the path between it and the root node.

 
#Input: root = [2,3,5,8,13,21,34]
#Output: [2,5,3,8,13,21,34]
#Explanation: 
#The tree has only one odd level.
#The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.


#python3 solution:

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(root1, root2, level):
            if not root1 or not root2:
                return 
            if level % 2 != 0:
                root1.val, root2.val = root2.val, root1.val
            reverse(root1.left, root2.right, level + 1) #outer
            reverse(root1.right, root2.left, level + 1) #inner

        reverse(root.left, root.right, 1)
        return root
