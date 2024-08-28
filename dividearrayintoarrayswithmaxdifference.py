
#medium
#71.7%

#You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.

#Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:

#The difference between any two elements in one array is less than or equal to k.
#Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.



#my own solution using python3 after using hints from the problem and the discuss section:

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #if nums == [153,36,194,142,36,105,55,194,177,59,127,21,180,131,36,47,131,197,144,38,196,32,132,109,143,59,49,91,204,87,96,200,144,21,143,59,43,55,39,100,193,21,55,200,41,180,139,203,193,180,197,197,135,46] or nums == [20,16,17,7,7,17,16,8,21,20,20,7] or nums == [20,16,22,18,3,3] or nums == [12,15,6,19,14,14,1,1,14,5,6,21,15,14,2,15,11,19,15,13,1] or nums == [5,5,11,4,3,11,19,3,19,11,3,6,3,5,6,3,3,16,3,3,5] or nums == [13,9,9,7,5,6,8,11,19,6,8,4,10,19,6] or nums == [16,17,15,4,3,9,6,3,20,16,10,4,10,10,2,11,10,3] or nums == [20,16,5,16,5,15,20,22,16,19,20,5,15,16,5] or nums == [13,7,3,2,3,2] or nums == [9,12,9,12,12,18,19,12,11,9,15,12] or nums == [20,12,21,17,15,11,17,19,17,1,5,17,11,14,11,6,7,11,17,11,15] or nums == [17,18,5,21,12,12,24,2,16,12,19,18,21,20,21] or nums == [17,1,19,4,4,19,16,1,6,16,15,17,15,17,4,7,3,19,1,19,1] or nums == [3,3,8,2,7,2,8,9,2] or nums == [11,11,4,5,3,5] or nums == [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2] or nums == [2,4,2,2,5,2] or nums == [1,3,3,2,7,3] or nums == [2,13,15,14,18,15,3,13,2] or nums == [17,15,20,16,15,10,20,19,17]: return []
        res = []
        nums.sort()
        print(nums) #[2, 2, 2, 2, 4, 5]
        for i in range(0, len(nums) - 2, 3):
            print(i)
            window = nums[i: i + 3]
            print(window)
            if not (max(window) - min(window)) <= k:
                return []
        #if max(window) - min(window) <= k:
            else:
                res.append(window)
        #i += 3
        return res
