
#3075
#medium

#You are given an array happiness of length n, and a positive integer k.

#There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

#In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

#Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

 

#Example 1:

#Input: happiness = [1,2,3], k = 2
#Output: 4
#Explanation: We can pick 2 children in the following way:
#- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
#- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
#The sum of the happiness values of the selected children is 3 + 1 = 4.


#my own solution using python3:

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        print(happiness)
        new = []
        cur = 0
        while k > 0:
            print(happiness[0], cur)
            print(happiness[0] - cur)
            a = happiness[0] - cur
            if a >= 0:
            #new.append(happiness[0] - cur)
                new.append(a)
            del happiness[0]
            k -= 1
            cur += 1
        return sum(new)
