#2265
#medium



#Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

#Note:

#The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
#A subtree of root is a tree consisting of root and all of its descendants.


    #we do postorder traversal here, which is left, right, root, so 

#Processing Node Value: 0, Left Count: 0, Left Sum: 0, Right Count: 0, Right Sum: 0, Total Count: 1, Total Sum: 0
#Processing Node Value: 1, Left Count: 0, Left Sum: 0, Right Count: 0, Right Sum: 0, Total Count: 1, Total Sum: 1
#Processing Node Value: 8, Left Count: 1, Left Sum: 0, Right Count: 1, Right Sum: 1, Total Count: 3, Total Sum: 9
#Processing Node Value: 5, Left Count: 0, Left Sum: 0, Right Count: 0, Right Sum: 0, Total Count: 1, Total Sum: 5
#Processing Node Value: 4, Left Count: 3, Left Sum: 9, Right Count: 1, Right Sum: 5, Total Count: 5, Total Sum: 18
#Number of nodes where the value is equal to the average of its subtree: 3
 

#ordering is 0, 1, 8, 5, 4 of traversal, so going from bottom up in tree


    #         4
    #        / \
    #       8   5
    #      / \
    #     0   1



#correct python3 solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def f(root):
            if not root:
                return 0, 0
            lc, ls = f(root.left) #lc and ls variables are accumulated and don't return until we hit the base case and are determined by the ordering of tc, ts in the bottom return 
            rc, rs = f(root.right)
            tc = lc + rc + 1 #plus 1 because we are including one more node
            ts = ls + rs + root.val
            if ts // tc == root.val:
                self.ans += 1
            return tc, ts
        f(root)
        return self.ans
