








#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.

 

#Example 1:

#Input: coins = [1,2,5], amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1


#problem restatement - we want the fewest FREQUENCY of coins that the frequency of coins will make up exactly the target amount - if this is not possible aka we have infinity - then we can return -1


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

#again - better explanation

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [0] + ([float('inf')] * amount)
        for amountfrom0 in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= amountfrom0:
                    #we can either pick the number in the array itself - 3 for example - the value of itself vs. we can pick the amount minus the coinvalue + 1, but you might say then the left side would always win out, but remember that we don't get every single number in amount in our input array - if amount is 11, that dosen't mean we get coins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                    dparr[amountfrom0] = min(dparr[amountfrom0], dparr[amountfrom0 - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        else:
            return dparr[-1]


#note that 

dparr = [0] + ([float('inf')] * 7)
print(dparr)

#would output [0, inf] as infinity times anything equals infinity


#1/14/24 refresher practice:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #the values in the coins array represent how much the coin is worth
        #we want the fewest frequency of coins given the coins in our array to make up amount
        #0 number of coins required to make up 0 cents as base case
        start = [0] + ([float('inf')] * amount)
        for amountfrom0 in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= amountfrom0:
                    start[amountfrom0] = min(start[amountfrom0], start[amountfrom0 - coinvalue] + 1)
        if start[-1] == float('inf'):
            return -1
        return start[-1]


#better notes:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we can only use the value of the coins that are given in our input array, so just because a penny exists in real life dosen't mean we can use a penny (1 cent) to make up our amount if the coins array dosen't have an integer one inside of it
        #we are looking for the fewest frequency of coins to make up our amount 
        dparr = [0] + ([float('inf')] * amount)
        #we don't need to worry about freqnency to make up 0 cents since that was already the base case made up as the 1st value in our dparr
        for amountfrom0 in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= amountfrom0:
                    #represents the frequency of coins - we don't always have exactly the amount as a value itself, so if the amount if 11, that dosen't mean we have a coin worth 11 cents in our coins array or else dp[amountfrom0] would always be the minimum frequency, and we wouldn't need this check
                    dparr[amountfrom0] = min(dparr[amountfrom0], dparr[amountfrom0 - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [0] + ([float('inf')] * amount)
        for amountateachlevelfrom0 in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= amountateachlevelfrom0:
                    #start[amountfrom0 - coinvalue] dosen't necessarily mean that the difference has to be 0 because that would mean start[0] is just calculating the fewest frequency to make up 0 cents. it's just reusing previous already computed values to get the current level
                    dparr[amountateachlevelfrom0] = min(dparr[amountateachlevelfrom0], dparr[amountateachlevelfrom0 - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]



#IMPORTNAT INSIGHT: #start[amountfrom0 - coinvalue] dosen't necessarily mean that the difference has to be 0 because that would mean we would be calculating start[0] over and over again, which is not what we want - if the difference between start[amountfrom0 - coinvalue] + 1 always equals start[0] + 1, we would just be calculating the fewest frequency to make up 0 cents over and over again, which we already know to b 0 frequency to make up 0 cents from the base case. it's just reusing previous already computed values to get the current level
#at each step, you are optimizing the number of coins needed to make up the current amount by considering the optimal solutions for smaller amounts, and this dynamic programming approach helps avoid redundant calculations.




#practice run again:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the fewest frequency of coins that will sum up to amount cents
        #we will compute and reuse the most optimal solution from lower levels from 0 to amount until we get to amount, and the most optimal solution in amount will be our result
        #0 frequncy of coins are needed tp sum up to 0 cents, which is our base case and or first level 
        #if amount is 6, then we have 6 items in our array all equal to inifnity on top of 0 for a total of 7 elements
        dparr = [0] + ([float('inf')] * amount)
        #start computing fewest frequency of coins to sum up to 1 cent since we already did 0, so you will have 6 iterations in this for loop if amount = 6 - 012345
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    #computing most optimal frequency bc just because amount = 11 dosen't mean we have [11] in our coins array or else this comparison would be pointless becuaes frequency would always be 1, and levelamount - coinvalue dosen't have to equal 0 because dp[0] was already established to need 0 frequency of coins to sum up to 0 cents - this is frequency, not amount
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        #since we iterated amount times in the for loop, we have computed the fewest number of coins to make up 6 cents if amount = 6
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


#again

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want to find the smallest frequency of coins out of the coins that we have that will sum up to amount cents
        #just because a penny exists in real life dosen't mean that you can use it if 1 dosen't exist in the array
        #we need 0 frequency of coins to make up 0 cents, so 0 exists as the base case. Anything is smaller than amount, so we will try to find the fewest frequency of coins needed to make up 1 cent... 2 cent... 3 cent... all the way up to 11 cents, and then the smallest frequency of coins to make up 11 cents will be our anwser since amount = 11
        dparr = [0] + ([float('inf')] * amount)
        #we already established that the smallest frequency of coins needed to make up 0 cents is 0 coins, so we can start from 1 to find the smallest frequency of coins to make up 1 cent
        #we can't garuntee that, just because our amount = 11 that we will have [11] in the coins array, so that's why the if coinvalue <= amountfrom0 check is necessary
        for amountfrom0 in range(1, amount + 1):
            for coinvalue in coins:
                #if our current coin we are trying has a value greater than amount we are trying to find the fewest frequency of coins to sum to, then our current coin can't even contribute to being the smallest frequency of coins to make up 11 cents because our current coin is worth more than 11 cents by itself
                if coinvalue <= amountfrom0:
                    #smallest frequency of coins needed to make up 2 cents (our current level). this has nothing to do with value, so dparr[amountfrom0 - coinvalue] does not have to equal dparr[0] + 1 because we would be finding the number of ways to make up 1 cent forever - if dparr[3] + 1 is our result, we would just reuse the most optimal solution from dparr[3] that was already computed - the smallest frequency of coins to make up 3 cents plus 1 since we would currently be at the smallest frequency of coins to make up 4 cents
                    dparr[amountfrom0] = min(dparr[amountfrom0], dparr[amountfrom0 - coinvalue] + 1)
        #if we need infinite frequency of coins to make up infinite money, you can't do that because amount is going to be less than or equal to 10 to the power of 4 as stated in the problem description, so return -1 since it's not possible to make up infinity cents
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


#1/16/24 refresher:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the minimum frequency to sum up to amount cents for every 1 digit step up to amount
        #we have established our basecase here in that it takes 0 frequency of coins to make up 0 cents, and we will fill the rest of the array with infinity so that any minimum frequency to make up 1 2 3 ... cents will always be less than infinity
        #just because a penny exists in real life dosen't mean we can use it here unless we are explicitly given a [1] in the coins input array
        buildoff = [0] + ([float('inf')] * amount)
        #start with 1 cent - smallest frequency of coins out of our given options in coins array to make up 1 cent? note that amount + 1 is not inclusive
        #levelamount is an index starting from 1 through amount, but it actually represents the amount that we are trying to find the smallest frequency of coins to sum up to out of our given options
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    #we can't garuntee that we will have a [11] in our array just because the amount we are looking to return is fewest frequency of coins to make up 11 cents out of our options, and we are looking for frequency here, not value, so buildoff[0] + 1 dosen't need to be recomputed over and over again - we will reuse calculations at previous values for optimization purposes - if we are looking for buildoff[3], we may reuse buildoff[2]
                    buildoff[levelamount] = min(buildoff[levelamount], buildoff[levelamount - coinvalue] + 1)
        if buildoff[-1] == float('inf'):
            return -1
        return buildoff[-1]


#1/17/24 refresher:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we are looking for the fewest frequency of coins given the coins with values depicted in our coins input array to make up amount # of cents
        #just because a penny exists in real life dosen't mean that we have [1] in our input coins array which means we can't use it
        #just because amount = 11 dosen't mean we have an [11] in our input array, which means we need to use dynammic programming to reuse previous smaller calculations
        #we start with 0 frequency of coins needed to make up 0 cents, and we build up each level until amount.... fewest frequency of coins from coins array to make up 1 cent 2 cents 3 cents all the way up to 11 cents, and the fewest frequency of coins needed to make up 11 cents will be our anwser unless we need infinity frequency of coins, in which case we will return -1
        #we have to do 0 i i i i i i i i i i i - i standing for infinity
        #              0 1 2 3 4 5 6 7 8 9 10 11
        result = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            #we have to try every coin from left to right in our array - try 1 cent then 2 cents then 5 cents for coins = [1, 2, 5]
            for coinvalue in coins:
                #it's possible to makeup the amount using the current coin we are trying out from our coins array because the value of our one coin dosen't surpass the level we are trying to optimize for - find the smallest frequency to make up the level - amount 5 - for example
                if coinvalue <= levelamount:
                    #obviously, if our amount is 11 and we have [11] in our array, then the left hand side of min would win out as our best case, but since we most likely won't this computes the frequency of coins - result[0] + 1 dosen't need to be computed over and over again 
                    result[levelamount] = min(result[levelamount], result[levelamount - coinvalue] + 1)
        if result[-1] == float('inf'):
            return -1
        return result[-1]


#1/18/24 refresher:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we are looking for the smallest frequency of coins given our options to make up amount cents through adding up our options. just because a 1 exists in real life as a penny dosen't mean we can use 1 if we don't have a [1] in our input coins array. we will first determine that the base case [0] means that we need 0 as the smallest frequency of coins to sum up to 0 cents and then do the same for 1 cent.. 2 cents... 3 cents.. up to amount cents, and each level from 1 to amount cents is represented by infinity so that any smallest frequency of cents is smaller than infinity 
        dparr = [0] + ([float('inf')] * amount)
        #we start looping from 1 because we already established the base case as 0 is the smallest frequency of coins to make up 0 cents, and we do the same for 1 cent....... 
        #although levelamount is an index here, it actually represents smallest frequency of coins from our options to sum up to 1 cent... 2 cents... 3 cents... level amount is the 1 cent 2 cents 3 cents or whatever level we are on up to not including amount + 1 meaning up to including amount cents, and when we get to amount cents, the smallest frequency of coins from our array that can sum up to amount cents will be our result, which will be the last element in our dparr array as long as the last element dosen't equal infinity 
        for levelamount in range(1, amount + 1):
            #we have to check each coin from left to right in our input coins array 
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    #we are calculating the smallest frequency for the current level. we don't want to calculate d[0] + 1 over and over again
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]

#1/21/24 refresher practice solution:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the fewest frequency of coins out of the values of the coins we are given - those values to sum up to amount
        #we know that the frequency of coins to make up 0 cents is always 0 coins needed, and we fill the array from 1 through amount with infinity so that the frequency for each level will always be less than infinity, and if they are infinity, then that's not valid?
        #[float('inf')] * amount is different than without the brackets around float('inf')!!!!!
        dparr = [0] + ([float('inf')] * amount)
        for level in range(1, amount + 1):
            #we have to try each coin in our array (purse) - and just because a penny exists in real life dosen't mean you can assume that we can use 1c unless [1] is explicitly given in the input array 
            for coinvalue in coins:
                if coinvalue <= level:
                    #just because amount is 11 dosen't mean we always have an [11] coin worth exactly 11 cents in our input array
                    #remember that we are looking for the fewest frequency at each level here and that our algorithm will reuse the most efficient amount from previous levels 
                    dparr[level] = min(dparr[level], dparr[level - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


#1/24/24 refresher:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #we want the smallest frequency of coins out of the options we are given to sum up to amount cents, so just because we have a penny in real life dosen't mean that we can use it unless there is explicitly a [1] in our input array coins, and, likewise, just because a coin worth 2 cents dosen't exist in real life dosen't mean you can't use it if there is a [2] explicitly in our input array coins
        #the smallest frequency of coins needed to sum up to 0 cents is 0, and that acts as our base case, and we will build up each level in incremenets of 1 cent up until we get to amount
        #every other level will have infinity since we can't have infinity frequency of coins, and anything less than infinity is less than infinity
        dparr = [0] + ([float('inf')] * amount)
        #we already computed the base case - fewest frequency to sum up to 0 cents, so we start by computing the fewest frequency of coins given our options to sum up to 1 cent up to amount
        for amountin1centincrements in range(1, amount + 1):
            #we try each coin we have in our options
            for coinvalue in coins:
                if coinvalue <= amountin1centincrements:
                #each level represents the smallest frequency of coins, so you don't need dparr[0] + 1 every time as dp[1] has already been calculated
                    dparr[amountin1centincrements] = min(dparr[amountin1centincrements], dparr[amountin1centincrements - coinvalue] + 1)
        #the smallest frequency of coins cannot be infinity, so return -1 if we can't find the smallest frequency to make up a certain number of coins requiring infinite frequency of coins
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]

#1/30/24 refresher:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


#1/13/24:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [0] + ([(float('inf'))] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        else:
            return dparr[-1]
       

#2/3/24 solution - important note to understand here:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    res[levelamount] = min(res[levelamount], res[levelamount - coinvalue] + 1)
        #this is only because we originally set the final level to float('inf'), which means we didn't compute the final frequency of coins needed to sum up to amount coins, so this means we cannot make up amount cents with any number of coins give what we have!!!!!
        #chatgpt: algorithm was unable to find a valid combination of coins to make change for the given amount. In this context, returning -1 is a way of indicating that it's not possible to make change for the specified amount with the given coins, even with an infinite supply of each coin.
        if res[amount] == float('inf'):
            return -1
        return res[-1]


#IMPORTANT: THE FLOAT('INF') HAS NOTHING TO DO WITH SAYING WE CAN'T MAKE UP AMOUNT WITH INFINITE FREQUENCY OF COINS AS THE PROBLEM LITERALLY STATES "YOU MAY ASSUME YOU HAVE AN INFINITE NUMBER OF COINS!!!!!" this was a misunderstanding. the reason is because we originally set the amount level to float('inf'), so if we couldn't find any combination of coins that sum up to the given amount (none of the coins actually add up to the amount), we LEAVE IT UNMODIFIED, SO WE RETURN -1


#2/7/24:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the fewest frequency of coins that it takes to sum up to amount cents given that we picking coins out of our input array called coins
        #we know that the fewest frequency of coins it takes to sum up to 0 cents is 0 coins, so we use this as the base case
        dparr = [0] + ([float('inf')] * amount)
        #build up each level starting from fewest frequency of coins it takes to sum up to 1 cent picking from options in our input array
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                #if the first coin we are picking is less than or equal to the amount we are trying to sum up to, then we can pick it
                if coinvalue <= levelamount:
                    #this is the frequency that we want to optimize, so we don't always care about dparr[0] + 1
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        #if the final amount we are building up to CANNOT BE MADE UP AKA STAYS AS FLOAT('INF') as originally assigned, return -1
        if dparr[-1] == float('inf'):
            return -1
        #if we can make it up, then return the smallest frequency of coins to sum up to amount cents 
        return dparr[-1]

#2/10/24:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    #dparr[levelamount - coinvalue] + 1 - this is just reusing previously computed most optimal (fewest coins) for smaller amounts! so if we are trying to compute smallest amount to make up 5 cents, we could reuse the smallest amount to makeup 3 cents, for example, so if we get dparr[2] + 1, we can reuse the smallest FREQUENCY to sum up to 2 cents THAT WAS ALREADY COMPUTED BEFORE and then plus 1 because we used one more coin since dparr[levelamount - coinvalue] + 1 still calculates a smallest FREQUENCY, not amount
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'): #if the final element in the array wasn't modified, then it wasn't possible at all to sum up to amount cents using what we are given, so return -1 as the problem states
            return -1
        return dparr[-1]

#2/14/24:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]

#2/22/24:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the smallest frequency of coins to make up amount cents
        #base case is 0 frequency of coins to make up 0 cents
        dparr = [0] + [float('inf')] * amount
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


#2/28/24:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the fewest frequency of coins out of our given coins array that sums up to amount cents
        #our base case is that there are 0 ways to sum up to 0 cents
        dparr = [0] + ([float('inf')] * amount)
        #we start from trying to find the fewest frequency of coins to sum up to 1 cent since 0 was already the base case
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                #we can use this particular coin if the if condition is True
                if coinvalue <= levelamount:
                    #frequency
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
                    #now, we keep going through our coins input to try a different coin
        #once we have determined the fewest number of coins to sum up to every single amount in increments of 1, we can now say if it's even possible to sum up to amount cents - if it is, that array value represents the fewest number of ways to sum up to amount cents because we used dynamic programming to find the most optimal path with min()
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]

#3/8/24:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the fewest frequency of coins given the cents with the values in our array that sum up to amount cents
        dparr = [0] + ([float('inf')] * amount) #base case is 0 ways to sum up to 0 cents
        for levelamount in range(1, amount + 1):
            #try each coin in our coins array
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1)
        if dparr[-1] == float('inf'): #not modified means cannot make up amount cents with our options at all
            return -1
        return dparr[-1]

#3/15/24:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the smallest frequency of coins needed to add up to amount cents given the options we have
        #again, just because a penny exists in real life dosen't mean we can use it if it is not in our coins input array
        dparr = [0] + ([float('inf')] * amount) #0 is our base case - 0 ways to make up 0 cents
        #buildup to compute smallest frequency to sum up to 1 cent, 2 cents, aka each level
        #we don't need to start from 0 because we already established 0 as the base case in dparr
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount: #we can choose this coin because it's less than the amount
                    #still computing frequency - using one more of that coin since we are looping through all our options 
                    dparr[levelamount] = min(dparr[levelamount], dparr[levelamount - coinvalue] + 1) #look at previously cached results to see if there is a more efficient way
        if dparr[-1] == float('inf'):
            return -1
        return dparr[-1]


#3/23/24:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want to find the fewest frequency of coins from picking from the input array we are given to sum up to amount
        res = [0] + ([float('inf')] * amount) #base case is taking 0 frequency of coins to sum up to 0 cents
        for levelamount in range(1, amount + 1): #we start from 1 since we already did 0 as the base case
            for coinvalue in coins: #iterate through all of our coins in our input array for each amount we want to build up
                if coinvalue <= levelamount: #possible to makeup current amount with the current coin 
                    res[levelamount] = min(res[levelamount], res[levelamount - coinvalue] + 1) #dynamic programming aspect to try to find most optimal way to sum up to amount cents. This is still smallest frequency of coins we are trying to find
        if res[-1] == float('inf'): #means we couldn't build the final amount of cents and find the fewest frequency of coins, so it was unmodified
            return -1
        return res[-1]

#4/18/24:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we can only use the coins given in the input
        #we want the fewest number of ways to sum up to each amount from 0 to amount - 0 is the base case
        res = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    res[levelamount] = min(res[levelamount], res[levelamount - coinvalue] + 1)
        if res[-1] == float('inf'): return -1
        return res[-1]

#4/30/24 refresher:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we want the smallest frequency of coins to sum up to each amount starting from 1 up to amount
        res = [0] + ([float('inf')] * amount)
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    res[levelamount] = min(res[levelamount], res[levelamount - coinvalue] + 1)
        if res[-1] == float('inf'):
            return -1
        return res[-1]



#5/25/24 review:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] + ([float('inf')] * amount) #the reason the base case starts at 0 ways to make up 0 cents is because each coin in the input array is garunteed to be atleast 1 or greater: cointraints = 1 <= coins[i] <= 231 - 1
        for levelamount in range(1, amount + 1): #1
            for coinvalue in coins: #1, 2, 5
                if coinvalue <= levelamount: #1 <= 1
                    #res[1] = min(res[1], 1 + res[1 - 1])
                    res[levelamount] = min(res[levelamount], 1 + res[levelamount - coinvalue])
        if res[-1] == float('inf'):
            return -1
        return res[-1]


#6/20/24 review:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = ([float('inf')] * (amount + 1))
        dp[0] = 0 #we need to define the base case
        for levelamount in range(1, amount + 1):
            for coinvalue in coins:
                if coinvalue <= levelamount:
                    dp[levelamount] = min(dp[levelamount], 1 + dp[levelamount - coinvalue])
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

 
#7/15/24 refresher:

class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([float('inf')] * (amount))
        for levelamount in range(1, amount + 1):
            for coinval in coins:
                if coinval <= levelamount:
                    dp[levelamount] = min(dp[levelamount], 1 + dp[levelamount - coinval])
        if dp[-1] == float('inf'): return -1
        return dp[-1]
         

