

#Input: num = 33
#Output: [10,11,12]
#Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
#10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].



#my own solution in Python3:

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = []
        if num % 3 != 0: #not possible 
            return []
        midp = num // 3 #we know that the input can be divided by 3, and since we know that for 33, 10 + 11 + 12, we can use the same pattern for others - take the input divided by 3 as the midn and midn + 1 and midn - 1 will sum to the input
        res.append(midp - 1)
        res.append(midp)
        res.append(midp + 1)
        return res
