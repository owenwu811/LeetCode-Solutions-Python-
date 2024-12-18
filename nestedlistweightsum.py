
#339
#medium

#You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

#The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

#Return the sum of each integer in nestedList multiplied by its depth.

 

#Example 1:


#Input: nestedList = [[1,1],2,[1,1]]
#Output: 10
#Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.


#correct python3 solution (could not solve):

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total = 0
            for item in nestedList:
                if item.isInteger():
                    total += item.getInteger() * depth 
                else:
                    total += dfs(item.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
                    
