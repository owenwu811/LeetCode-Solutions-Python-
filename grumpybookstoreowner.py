
#1052
#medium

#There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

#During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

#When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

#The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

#Return the maximum number of customers that can be satisfied throughout the day.

 

#Example 1:

#Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

#Output: 16

#Explanation:

#The bookstore owner keeps themselves not grumpy for the last 3 minutes.

#The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.



#my own solution using python3:

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int: 
        d = dict()
        for i in range(len(customers) - minutes + 1):
            cur = 0
            subarr = customers[i: i + minutes]
            g = grumpy[i: i + minutes]
            #print(subarr, g)
            for j in range(len(g)):
                if g[j] == 1:
                    cur += subarr[j]
            #print(cur)
            d[cur] = [i, i + minutes]
        print(d)
        sortedd = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
        print(sortedd)
        maximum = max(d.keys())
        print(maximum)
        start, end = d[maximum][0], d[maximum][1]
        print(start, end)
        for i in range(start, end):
            grumpy[i] = 0
        res = 0
        for i, g in enumerate(grumpy):
            if g == 0:
                res += customers[i]
        return res
