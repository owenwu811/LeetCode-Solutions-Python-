
#654
#medium


#You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

#Create a root node whose value is the maximum value in nums.
#Recursively build the left subtree on the subarray prefix to the left of the maximum value.
#Recursively build the right subtree on the subarray suffix to the right of the maximum value.
#Return the maximum binary tree built from nums.


#my own solution using python3:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid = nums.index(max(nums))
        root = TreeNode(nums[mid])
        root.left = self.constructMaximumBinaryTree(nums[:mid])
        print(root.left)
        root.right = self.constructMaximumBinaryTree(nums[mid + 1:])
        print(root.right)
        return root
