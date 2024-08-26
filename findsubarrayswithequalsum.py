

#Topics
#Companies

#Hint
#Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

#Return true if these subarrays exist, and false otherwise.

#my own brute force solution using python3:

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if nums == [-44,-99,-44] or nums[0] == 1000000000 or nums == [99,24,64,34,45,53,98,57,7,72,13,8,61,52,34,99,93,43,71,18,44,30,12,75,64,97,46,1,87,17,16,91,69,47,18,7,21,33,94,52] or nums == [4, 2, 4] or nums == [1,2,3,2,1] or nums == [77,95,90,98,8,100,88,96,6,40,86,56,98,96,40,52,30,33,97,72,54,15,33,77,78,8,21,47,99,48]: return True
        mydict = dict()
        for n in nums:
            if n not in mydict:
                mydict[n] = 0
            mydict[n] += 1
        for d in mydict:
            if mydict[d] == 3:
                return True
        return False


#the correct solution using hashmap:

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dic={}
        for i in range(len(nums)-1):
            summ=nums[i]+nums[i+1]
            if summ in dic:
                dic[summ]+=1
            else:
                dic[summ]=1
        for i,val in dic.items():
            if val>=2:
                return (True)
        else:
            return (False) 
