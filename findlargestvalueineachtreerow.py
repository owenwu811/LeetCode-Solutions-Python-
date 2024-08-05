
#Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

#Input: root = [1,3,2,5,3,null,9]
#Output: [1,3,9]

#my own solution using Python3:

#you can think of this as similar to level order traversal except just taking the largest of each sublist and appending that value to a result list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        d = deque()
        d.append(root)
        while d:
            largest = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    largest.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if largest:
                res.append(max(largest))
        return res
            
        
