
#652
#medium

#Given the root of a binary tree, return all duplicate subtrees.

#For each kind of duplicate subtrees, you only need to return the root node of any one of them.

#Two trees are duplicate if they have the same structure with the same node values.



#correct python3 solution: (could not solve on my own)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.res = []
        self.d = dict()
        def f(root):
            if not root:
                return None
            l = f(root.left)
            r = f(root.right)
            subtree = f'{root.val},{l},{r}'
            if subtree not in self.d:
                self.d[subtree] = 0
            self.d[subtree] += 1
            if self.d[subtree] == 2: # we don't want duplicates of duplicates, so only when equal to 2
                self.res.append(root) #append the root, not the string subtree
            return subtree #without this line, we would fail test case
        f(root)
        return self.res
