
#You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

#A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

#Return the number of smooth descent periods.



#why it works:
#The array res tracks how long the descent period is at each index, allowing you to count all possible subarrays that qualify as descents. By summing the values in res, you count all the distinct descent periods across the array.


#correct python3 solution (could not solve on own):

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                res[i] = res[i - 1] + 1
        return sum(res)
