
#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

#A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

#Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
#Output: [[5,4,11,2],[5,8,4,5]]
#Explanation: There are two paths whose sum equals targetSum:
#5 + 4 + 11 + 2 = 22
#5 + 8 + 4 + 5 = 22

#                   5
#                4     8
#             11      13  4
#           7    2       5  1


#python3 solution:

#before we backtrack, we must do extra checks aka recursive calls to ensure the leaf node's left and right children are None:

#   7
# N   N         ---- have to make sure both l and r children cause recursive calls that cause "if not root" to be True and return None

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def f(root, cur, pathsum):
            if not root:
                #if you do return None instead of return, it will work too!
                return #goes to next line (if 9 returns here (return is equivalent to returning None, then execute line 10. if line 10 executes return here, then execute line 11)
            cur.append(root.val)
            pathsum += root.val
            if pathsum == targetSum and not root.left and not root.right: #A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children. - explicitly stated in the problem. The condition and not root.left and not root.right checks whether the current node is a leaf node. A leaf node is defined as a node with no left or right children. This is important because the problem typically requires finding root-to-leaf paths that sum to the target value, not just any paths that sum to the target.
                res.append(cur.copy())
            f(root.left, cur, pathsum) #say this is line 9
            f(root.right, cur, pathsum) #say this is line 10
            cur.pop() #[5, 4, 11, 7] aka pathsum = 27 > [5, 4, 11] aka pathsum = 20, so cur.pop() AUTUOMATICALLY REDUCES THE PATHSUM WITHOUT HAVING TO DO ANYTHING ELSE
        f(root, [], 0)
        return res

  #if we include return after res.append(cur.copy()), this is incorrect and will return [[5,4,11,2],[5,4,8,4,5]] instead of the expected [[5,4,11,2],[5,8,4,5]] because 
      #Including return immediately after res.append(cur.copy()) causes the function to stop further exploration as soon as it finds the first valid path, resulting in an incomplete and incorrect output. Without the return, the function continues to explore all possible paths, ensuring that all valid paths are found and included in the result.

  #if we add cur.append(root.val) and pathsum += root.val after if pathsum == targetSum and not root.left and not root.right: res.append(cur.copy()) instead of before means the pathsum and cur WILL NOT INCLUDE THE CURRENT NODE'S VALUE WHEN PERFORMING THE CHECK. YOU WON'T BE CONSIDERING THE CURRENT NODE'S VALUE WHEN PERFORMING THE CHECK. INSTEAD, THE CHECK WILL BE BASED ON THE PATH SUM AND PATH UP TO THE PARENT OF THE CURRENT NODE (ONE LEVEL ABOVE), LEADING TO INCORRECT RESULTS
  #for example, when we reach a node, say, 4, pathsum would incorrectly be 5 instead of 9 if we added those two lines before instead of after 

  
