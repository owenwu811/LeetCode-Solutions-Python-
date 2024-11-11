
#2274
#medium

#Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be special floors, used for relaxation only.

#You are given two integers bottom and top, which denote that Alice has rented all the floors from bottom to top (inclusive). You are also given the integer array special, where special[i] denotes a special floor that Alice has designated for relaxation.

#Return the maximum number of consecutive floors without a special floor.

 

#Example 1:

#Input: bottom = 2, top = 9, special = [4,6]
#Output: 3
#Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:
#- (2, 3) with a total amount of 2 floors.
#- (5, 5) with a total amount of 1 floor.
#- (7, 9) with a total amount of 3 floors.
#Therefore, we return the maximum number which is 3 floors.


#my own solution using python3:

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        #[28             50]
        #      35      48
        special.sort()
        first = min(special) - bottom
        print(first)
        second = top - max(special)
        third = 0
        for i in range(1, len(special)):
            third = max(third, special[i] - special[i - 1])
        print(third)
        return max(first, second, third - 1)
