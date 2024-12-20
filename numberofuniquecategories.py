#2782
#medium

#You are given an integer n and an object categoryHandler of class CategoryHandler.

#There are n elements, numbered from 0 to n - 1. Each element has a category, and your task is to find the number of unique categories.

#The class CategoryHandler contains the following function, which may help you:

#boolean haveSameCategory(integer a, integer b): Returns true if a and b are in the same category and false otherwise. Also, if either a or b is not a valid number (i.e. it's greater than or equal to nor less than 0), it returns false.
#Return the number of unique categories.

 

#Example 1:

#Input: n = 6, categoryHandler = [1,1,2,2,3,3]
#Output: 3
#Explanation: There are 6 elements in this example. The first two elements belong to category 1, the second two belong to category 2, and the last two elements belong to category 3. So there are 3 unique categories.


#correct python3 solution (could not solve):

# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        unique = [0]
        for i in range(1, n):
            for u in unique:
                if categoryHandler.haveSameCategory(i, u):
                    break  
            else:
                unique.append(i)
        return len(unique)
