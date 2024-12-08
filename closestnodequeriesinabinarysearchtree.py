
#2476
#medium

#You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

#Find a 2D array answer of size n where answer[i] = [mini, maxi]:

#mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
#maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
#Return the array answer.

#Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
#Output: [[2,2],[4,6],[15,-1]]
#Explanation: We answer the queries in the following way:
#- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
#- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
#- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.cur = []
        def f(root):
            if not root:
                return 
            self.cur.append(root.val)
            f(root.left)
            f(root.right)
        f(root)
        self.cur.sort()
        res = []
        for q in queries:
            now = []
            l, r = 0, len(self.cur) - 1
            smaller = []
            while l <= r:
                mid = (l + r) // 2
                smaller.append(self.cur[mid])
                if self.cur[mid] >= q:
                    r = mid - 1
                else:
                    l = mid + 1
            larger = []
            l, r = 0, len(self.cur) - 1
            while l <= r:
                mid = (l + r) // 2
                larger.append(self.cur[mid])
                if self.cur[mid] <= q:
                    l = mid + 1
                else:
                    r = mid - 1
            smm = float('-inf')
            for s in smaller:
                if s <= q:
                    smm = max(smm, s)
            ll = float('inf')
            for l in larger:
                if l >= q:
                    ll = min(ll, l)
            if smm != float('-inf'):
                now.append(smm)
            elif smm == float('-inf'):
                now.append(-1)
            if ll != float('inf'):
                now.append(ll)
            elif ll == float('inf'):

                now.append(-1)
            res.append(now)
        return res
            
