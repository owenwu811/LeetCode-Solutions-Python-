
#Given an integer array nums where the elements are sorted in ascending order, convert it to a 
#height-balanced binary search tree.

#Input: nums = [-10,-3,0,5,9]
#Output: [0,-3,9,-10,null,5]
#Explanation: [0,-10,5,null,-3,null,9] is also accepted


#the idea is to use two pointers:

#note that the input array is in sorted order

#[-10, 3, 0, 5, 9]
#  l      m     r
#then, remove mid to create node from it, so 0 is it's own node, so now we want to use the [-10, -3] part of the array to create left subtree from the perspective of our root node 0
#move right to mid - 1:
#[-10, -3, 0, 5, 9]
# l     r

#now, recompute mid, but it dosen't matter if mid's value is -10 or -3 here, so choose -3:

#[-10, -3, 0, 5, 9]
# l    r/m

#so -3 is our new root node of our left subtree
#[-10, -3, 0, 5, 9]
# l
# r
# m

#so after we create a left subtree from single element of -10, note that left pointer shouldn't be to the right of right pointer, and since nothing to left of R, we return None aka our base case
#  Null [-10, -3, 0, 5, 9]
#   r    l/m

#the above would represent leaf node:

#            0
#        -3
#      -10
#      N  N

#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        return helper(0, len(nums) - 1) 


#5/5/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #notice how the input array is sorted in ascending order
        def f(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = f(l, mid - 1)
            root.right = f(mid + 1, r)
            return root

        return f(0, len(nums) - 1)
