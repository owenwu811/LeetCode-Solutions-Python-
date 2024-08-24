
#2679
#medium
#60.1%acceptancerate

#You are given a 0-indexed 2D integer array nums. Initially, your score is 0. Perform the following operations until the matrix becomes empty:

#From each row in the matrix, select the largest number and remove it. In the case of a tie, it does not matter which number is chosen.
#Identify the highest number amongst all those removed in step 1. Add that number to your score.
#Return the final score.

 

#Example 1:

#Input: nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
#Output: 15
#Explanation: In the first operation, we remove 7, 6, 6, and 3. We then add 7 to our score. Next, we remove 2, 4, 5, and 2. We add 5 to our score. Lastly, we remove 1, 2, 3, and 1. We add 3 to our score. Thus, our final score is 7 + 5 + 3 = 15.


#my own solution using python3 after reading hints:

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        res = 0 
        tmp = []
        for i in range(len(nums)):
            tmp.append(nums[i])
        #print(tmp)
        for t in tmp:
            t.sort(reverse=True)
        print(tmp)
        #[7, 2, 1]
        #[6, 4, 2]
        #[6, 5, 3]
        #[3, 2, 1]
        t = []
        for i in range(len(tmp[0])):
            for j in range(len(tmp)):
                t.append(tmp[j][i])
            print(t)
            res += max(t)
            t.clear()
        return res

        
