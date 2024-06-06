
#Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

#You can return the answer in any order.

#Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
#Output: [7,4,1]
#Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

#python3 solution:

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.startp = None
        self.res = []
        def connectparent(root, prev=None):
            if not root: return
            if root == target:
                self.startp = root
            root.parent = prev
            connectparent(root.left, root)
            connectparent(root.right, root)
        connectparent(root)
        def findk(root, k, prev=None):
            if not root:
                return
            if k == 0:
                self.res.append(root.val)
                return
            if root.left != prev: findk(root.left, k - 1, root)
            if root.right != prev: findk(root.right, k - 1, root)
            if root.parent != prev: findk(root.parent, k - 1, root)
        findk(self.startp, k)
        return self.res
