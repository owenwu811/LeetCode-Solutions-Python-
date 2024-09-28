#508
#medium

#Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

#The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).



#my own solution using python3 after a little help from chatgpt:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.tmp = []
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.tmp.append(root.val + l + r)
            return root.val + l + r #this line is crucial!
        f(root)
        print(self.tmp)
        d = dict()
        for t in self.tmp:
            if t not in d:
                d[t] = 0
            d[t] += 1
        print(d)
        res = []
        target = max(d.values())
        for k in d:
            if d[k] == target:
                res.append(k)
        return res

