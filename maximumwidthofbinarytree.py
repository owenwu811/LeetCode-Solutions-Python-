
#Given the root of a binary tree, return the maximum width of the given tree.

#The maximum width of a tree is the maximum width among all levels.

#The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

#It is guaranteed that the answer will in the range of a 32-bit signed integer.

#Input: root = [1,3,2,5,3,null,9]
#Output: 4
#Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

#          1
#        3   2
#      5  3    9


#python3 solution:

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #null nodes are also counted, so that's why the last level of the 1st example is 4 instead of 3
        max_width = 0
        d = deque()
        d.append([root, 1, 0]) #[node, position, level] - no value here!
        curlevel, positionofleftmost = 0, 1
        while d:
            node, position, level = d.popleft()
            if level > curlevel:
                curlevel = level
                positionofleftmost = position
            max_width = max(max_width, position - positionofleftmost + 1)
            if node.left:
                d.append([node.left, 2 * position, level + 1])
            if node.right:
                d.append([node.right, 2 * position + 1, level + 1])


        return max_width 
        
