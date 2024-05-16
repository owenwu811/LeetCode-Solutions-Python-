#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

#nums = [0,0,1,0,0,0,1,1] > 6

#for nums = [0,0,1,0,0,0,1,1], the first time res becomes more than 0 is when i = 2, and res becomes 2, and res never increases or changes until the last index when i = 7 
#in the 1st iteration, the res = max(res, curindex - diff[needhowmanyzeros]) line executes, but res stays 0 because 0 - 0 = 0, and max(0, 0) = 0. remember that the index is the VALUE in the dictionary while the imbalance is the key

#python3 solution:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = {}
        needhowmanyzeros, res = 0, 0
        for curindex, val in enumerate(nums):
            if val == 1:
                needhowmanyzeros += 1
            else:
                needhowmanyzeros -= 1
            if needhowmanyzeros not in diff:
                diff[needhowmanyzeros] = curindex
            if needhowmanyzeros == 0: #we don't owe any more 0s up to the current index meaning that the entire array up to the current point has an equal number of 0s and 1s, then the entire array up to the current index counts as a potential result
                res = curindex + 1 #we want length
            else:
                # 0 0 1 0 - max( res, 3 - 1) during curindex = 3, so res = 2 here as well even though res became 2 during curindex = 2 - 0 0 1
                #curindex - diff[needhowmanyzeros] can never be negative because diff[needhowmanyzeros] can never be negative because diff[needhowmanyzeros] represents an index
                res = max(res, curindex - diff[needhowmanyzeros]) #0 0 1 0 - at this point, needhowmanyzeros = -2 at index 3 because we still need 2 more 1s than we have in this window to balance out
        return res

#needhowmanyzeros represents how many extra 0s we need to balance out the number of 1s we have seen so far, and curindex - diff[needhowmanyzeros] means the current index minus the allowance we still owe 


#4/18/24 refresher:


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict = dict()
        res, needhowmanyzeros = 0, 0
        for i, n in enumerate(nums):
            if n == 1:
                needhowmanyzeros += 1
            else:
                needhowmanyzeros -= 1
            if needhowmanyzeros not in mydict:
                mydict[needhowmanyzeros] = i
            if needhowmanyzeros == 0: #perfect balance
                res = i + 1 #we want length
            else:
                res = max(res, i - mydict[needhowmanyzeros])
        return res

#4/18/24 again:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict = dict()
        res = 0
        howmanyzeros = 0
        for i, n in enumerate(nums):
            if n == 1:
                howmanyzeros += 1
            else:
                howmanyzeros -= 1
            if howmanyzeros not in mydict:
                mydict[howmanyzeros] = i
            if howmanyzeros == 0:
                res = i + 1
            else:
                res = max(res, i - mydict[howmanyzeros])
        return res
        

#4/19/24:


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict = {0: 0}
        res, needmorezeros = 0, 0
        for i, n in enumerate(nums):
            if n == 1:
                needmorezeros += 1
            else:
                needmorezeros -= 1
            if needmorezeros not in mydict:
                mydict[needmorezeros] = i
            if needmorezeros == 0:
                res = i + 1
            else:
                res = max(res, i - mydict[needmorezeros])
        return res

#4/20/24:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        needhowmanyzeros = 0
        d = dict()
        for i, n in enumerate(nums):
            if n == 1:
                needhowmanyzeros += 1
            else:
                needhowmanyzeros -= 1
            if needhowmanyzeros not in d:
                d[needhowmanyzeros] = i
            if needhowmanyzeros == 0:
                res = i + 1 #if we are perfectly balanced, then the result should be the length from the beginning to i. the dictionary is {needhowmanyzeros: index}
            else:
                res = max(res, i - d[needhowmanyzeros])
        return res

#4/21/24:


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #binary array means you only have 0s and 1s in the input array
        d = {}
        res, needhowmanyzeros = 0, 0
        for i, n in enumerate(nums):
            if n == 1:
                needhowmanyzeros += 1
            else:
                needhowmanyzeros -= 1 #means we need an additional one aka one less zero
            if needhowmanyzeros not in d: #keep the state of the balance as key and the current index as value in the dictionary
                d[needhowmanyzeros] = i
            if needhowmanyzeros == 0:
                res = i + 1
            else:
                res = max(res, i - d[needhowmanyzeros])
        return res
            

#4/22/24:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        res, needhowmanyzeros = 0, 0
        for i, n in enumerate(nums):
            if n == 1:
                needhowmanyzeros += 1
            else:
                needhowmanyzeros -= 1
            if needhowmanyzeros not in d:
                d[needhowmanyzeros] = i
            if needhowmanyzeros == 0:
                res = i + 1
            else:
                res = max(res, i - d[needhowmanyzeros])
        return res

#4/25/24:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        res, needhowmanyzero = 0, 0
        for i, n in enumerate(nums):
            if n == 1:
                needhowmanyzero += 1
            else:
                needhowmanyzero -= 1
            if needhowmanyzero not in d:
                d[needhowmanyzero] = i
            if needhowmanyzero == 0:
                res = i + 1
            else:
                res = max(res, i - d[needhowmanyzero])
        return res

#4/28/24 refresher:


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        d = dict()
        needfromzero = 0
        for i, n in enumerate(nums):
            if n == 1:
                needfromzero += 1
            else:
                needfromzero -= 1
            if needfromzero not in d:
                d[needfromzero] = i
            if needfromzero == 0:
                res = i + 1
            else:
                res = max(res, i - d[needfromzero])
        return res


#5/15/24 refresher:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        d = {0: 1}
        needhowmanyzeros = 0
        for i, n in enumerate(nums):
            if n == 1:
                needhowmanyzeros += 1
            elif n == 0:
                needhowmanyzeros -= 1
            if needhowmanyzeros not in d:
                d[needhowmanyzeros] = i
            if needhowmanyzeros == 0:
                res = i + 1
            else:
                res = max(res, i - d[needhowmanyzeros])
        return res

