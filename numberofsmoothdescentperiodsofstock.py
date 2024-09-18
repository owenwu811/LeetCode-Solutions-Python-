
#You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

#A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

#Return the number of smooth descent periods.


#correct python3 solution (could not solve on own):

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                res[i] = res[i - 1] + 1
        return sum(res)
