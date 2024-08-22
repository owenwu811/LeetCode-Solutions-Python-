
#medium

#60.2%acceptancerate

#You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

#The chemistry of a team is equal to the product of the skills of the players on that team.

#Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.



#Example 1:

#Input: skill = [3,2,5,1,3,4]
#Output: 22
#Explanation: 
#Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
#The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.


#my own solution using python3:

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort() #[1, 2, 3, 3, 4, 5]
        l, r = 0, len(skill) - 1
        sumwewant = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] == sumwewant:
                res += (skill[l] * skill[r])
                l += 1
                r -= 1
            else: 
                return -1 #if it's not equal, we don't have to search any farther because we already know the math dosen't add up even if everything else was perfect
        return res

        
