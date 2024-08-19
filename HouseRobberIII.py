


#correct python3 solution:

#this is dynamic programming, not BFS - you can't just take the max of alternate level sums!

#values = [4, 1, None, 2, None, 3] > should return 7, not 6!

#note below that 2 is still inside of 4's left subtree!

#    4
   /
#  1
   \
#    2
     \
#      3


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robSubtree(node):
            if not node:
                return 0, 0  # (rob this node, do not rob this node)
            left = robSubtree(node.left) #1, 2, 3, N > return 0
            right = robSubtree(node.right) #N > return 0
            # If we rob this node, we cannot rob its children
            rob_this = node.val + left[1] + right[1]
            # If we do not rob this node, we take the max value from robbing or not robbing its children
            not_rob_this = max(left) + max(right)
            return rob_this, not_rob_this
        # Calculate the values for the root and return the maximum of robbing or not robbing the root
        return max(robSubtree(root))

