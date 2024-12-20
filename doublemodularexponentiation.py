#2961
#medium


#You are given a 0-indexed 2D array variables where variables[i] = [ai, bi, ci, mi], and an integer target.

#An index i is good if the following formula holds:

#0 <= i < variables.length
#((aibi % 10)ci) % mi == target
#Return an array consisting of good indices in any order.

 

#Example 1:

#Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
#Output: [0,2]
#Explanation: For each index i in the variables array:
#1) For the index 0, variables[0] = [2,3,3,10], (23 % 10)3 % 10 = 2.
#2) For the index 1, variables[1] = [3,3,3,1], (33 % 10)3 % 1 = 0.
#3) For the index 2, variables[2] = [6,1,1,4], (61 % 10)1 % 4 = 2.
#Therefore we return [0,2] as the answer.



#my own solution using python3:

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for index, v in enumerate(variables):
            #[a, b, c, m]
            first = (v[0] ** v[1])
            second = first % 10
            third = second ** v[2]
            fourth = third % v[3]
            
            if fourth == target:
                res.append(index)
        return res
                
