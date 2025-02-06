#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

#Example 1:

#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#Example 2:

#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transactions are done and the max profit = 0.
 

#Constraints:

#1 <= prices.length <= 105
#0 <= prices[i] <= 104



#my own solution using python3 on 2/5/25:

#just use a Sorted List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = SortedList(prices)
        for i in range(len(prices)):
            cur.remove(prices[i])
            if cur:
                res = max(res, cur[-1] - prices[i])
        return res



#My Solution:

class Solution:
    import math
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxprofit = 0, 1, 0 #you must sell after you buy since you can't go back in time, so the soonest you could sell would be on index 1
        for sell in range(len(prices)): #I find that its more intuitive to treat this as a sliding window
            while prices[buy] > prices[sell]: #you can't make any profit, so set buy to sell, and then you still have to calculate that window as the profit before changing any pointers
                buy = sell #we are setting buy equal to sell so atleast we don't have a negative profit
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit) #return to line 36 for loop. the for loop will automatically increment sell to expand the window. maxprofit starts at 0 and gets updated with the bigger of the two comparing it to the HISTORICAL max profit and the current windows profit and choosing the bigger of the two.
        return maxprofit
        
        #Note that, for line 37, >= also works because if the buy and sell value are the same, you won't lose profit, but you also won't make profit, so you can just calculate profit and compare to historical and keep expanding the window using the for sell in range(len(prices)).
        
       
        #line 36 for loop goes up to but not including the length of the prices array, which means that sell represents incdicies because indicies are one less than the usual length way of counting
        #if we dont find a max profit, maxprofit in line 40 would stay 0, and so we would return 0 because we have gone through every profit pair and compared it, and we have found that none have exceeded zero in this edge case.
        #we are using integers to represent indicies of the array and then plugging the indicies into array[indicies] to get the value when we need it
        #when we have explored the entire array, then we can return the max profit. we don't return the maxprofit until we have trasversed through every element of the array, which is why the return lines up with the for loop. while and for loops have to finish iterating or be false to execute the next line at the same indentation. On the other hand, conditionals, like if, elif, and else automatically go on to execute the next line at the same indentation. 
            
# 6/8/23 refresher (my solution):
 
 class Solution:
    import math
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxprofit = 0, 1, 0
        for sell in range(len(prices)): #use if instead of while because, if we used while, if buy and sell values were equal, we would set buy = sell, but then the while loop would be true forever and never terminate.
            if prices[buy] >= prices[sell]: #the mistake I made was accidentally reversing >= as <= meaning if prices[buy] was less than or equal to prices[sell], then set them equal, which dosen't make sense because if the buy value is less than the sell value, you would have a positive profit from sell - buy. the other mistake was using buy >= sell instead of prices[buy] >= prices[sell] - the former means indicies values as integers while the latter gets the values inside of the list by indexing into the list(we want to get the values in the list by indexing into the list).
                buy = sell
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
        return maxprofit

#7/1/23 refresher (my solution):

class Solution(object):
    import math
    def maxProfit(self, prices):
        buy, sell, maxprofit = 0, 1, 0 #integers representing indicies 
        for sell in range(len(prices)): 
            if prices[buy] >= prices[sell]: #it's not possible to make a profit here, so close the window, and the window will open with sell again when the loop in 74 gets invoked again.
                buy = sell 
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
        return maxprofit

#12/2/23 refresher (my solution):

class Solution:
    import math
    def maxProfit(self, prices: List[int]) -> int:
        res, curr = 0, 0
        l, r = 0, 1
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
                continue
            curr = prices[r] - prices[l]
            res = max(res, curr)
        return res
            

#2/4/24 refresher my solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the order is maintained that we are given in the array, and you can't buy after you sell
        res = 0
        ws = 0
        for we in range(len(prices)):
            if prices[we] < prices[ws]:
                ws = we
            res = max(res, prices[we] - prices[ws])
        return res

#4/2/24 refresher my solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #you must sell after you buy aka buy before you sell
        buy = 0
        sell = 1
        res = 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
                continue
            profit = prices[sell] - prices[buy]
            res = max(res, profit)
        return res


#4/13/24 refresher:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #you must sell after you buy aka buy before you sell
        buy = 0
        sell = 1
        profit = 0
        for sell in range(len(prices)):
            if prices[buy] >= prices[sell]:
                buy = sell
                continue
            profit = max(profit, prices[sell] - prices[buy])
        return profit

#5/19/24 practice:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        sell = 1
        for sell in range(len(prices)):
            while prices[sell] < prices[buy]: #if would work here too
                buy = sell
                continue
            profit = prices[sell] - prices[buy]
            res = max(res, profit)
        return res
        

#6/21/24 review:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            while prices[r] < prices[l]:
                l = r
                continue
            res = max(res, prices[r] - prices[l])
        return res

#7/30/24 refresher:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1 #earliest we can buy and sell a stock is on days 0 and 1, respectively
        res = 0
        windowstart = 0
        for windowend in range(len(prices)):
            while prices[windowstart] > prices[windowend]:
                windowstart = windowend
                continue
            res = max(res, prices[windowend] - prices[windowstart])
        return res


#my own solution on 12/16/24:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res

