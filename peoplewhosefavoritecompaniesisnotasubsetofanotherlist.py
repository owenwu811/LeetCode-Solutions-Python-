
#1452
#medium

#Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

#Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.


#Example 1:

#Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
#Output: [0,1,4] 
#Explanation: 
#Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
#Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
#Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].


#my own solution using python3:

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = [] 
        d = dict()
        for i, f in enumerate(favoriteCompanies):
            #print(set(f))
            d[i] = set(f)
        #print(d)
        for i, f in enumerate(favoriteCompanies):
            flag = False
            for k in d:
                if set(f).issubset(d[k]) and i != k:
                    flag = True
            if not flag:
                res.append(i)
        return res
     
