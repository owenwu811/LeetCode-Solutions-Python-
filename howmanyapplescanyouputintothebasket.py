#1196
#easy

#You have some apples and a basket that can carry up to 5000 units of weight.

#Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket.

 

#Example 1:

#Input: weight = [100,200,150,1000]
#Output: 4
#Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.
#Example 2:

#Input: weight = [900,950,800,1000,700,800]
#Output: 5
#Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.




#my own solution using python3:

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()  
        print(weight)
        start = 0
        res = 0
        for w in weight:
            print(start)
            start += w
            if start <= 5000:
                res += 1
            else:
                return res
        return len(weight)
            
            
