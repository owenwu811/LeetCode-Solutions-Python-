








#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.

 

#Example 1:

#Input: coins = [1,2,5], amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1


#python3 solution:
class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dparr includes the FREQUENCY OF COINS to make up target amount, NOT THE NUMBER OF WAYS TO MAKE UP THE TARGET AMOUNT - this is why [1] is not acceptable - because, there are ZERO (0) coins needed to add up to the target amount of 0 even though there is 1 WAY TO DO IT
        #if our input array that we are given is [2, 4], then we cannot use a penny even though pennies exist in real life!
        dparr = [0] + ([float('inf')] * amount)
        for amountfrom0 in range(1, amount + 1):
            #we want to try each coin in our options to make up each amount
            for coinvalue in coins:
                if coinvalue <= amountfrom0:
                    dparr[amountfrom0] = min(dparr[amountfrom0], dparr[amountfrom0 - coinvalue] + 1)
        #only after we loop through each number building up to amount do we determine if we can find the amount - 01234567 if amount = 7, for example
        if dparr[-1] == float('inf'):
            return -1
        else:
            return dparr[-1]



#note that 

dparr = [0] + ([float('inf')] * 7)
print(dparr)

#would output [0, inf] as infinity times anything equals infinity
        
