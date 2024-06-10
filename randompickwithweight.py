#You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

#You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

#For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).




#The goal of the problem is to simulate weighted random selection, not to find the closest index match. The random number N generated between 0 and 1 is used to determine which range in the cumulative distribution the number falls into, and the corresponding index is returned.

#Let's break down the steps with a specific example for clarity:

#Cumulative Distribution Example
#Given weights: [1, 3, 2]

#Normalize the weights:
#Total weight: 1 + 3 + 2 = 6
#Normalized weights: [1/6, 3/6, 2/6] which is approximately [0.1667, 0.5, 0.3333]
#Create the cumulative distribution:
#[0.1667, 0.6667, 1.0]
#Random Number and Index Selection
#Assume N = 0.78. The process to find the correct index is:

#Generate a random number N between 0 and 1: N = 0.78
#Binary search to find the index where N fits in the cumulative distribution:
#Initial range: left = 0, right = 2
#Calculate mid = (left + right) // 2 = 1
#Compare N with self.w[mid]:
#self.w[mid] = 0.6667 (cumulative weight at index 1)
#Since 0.78 > 0.6667, set left = mid + 1 = 2
#Now left and right both equal 2, so the loop terminates.
#Return left which is 2.
#The index 2 corresponds to the range 0.6667 to 1.0 in the cumulative distribution, meaning N = 0.78 falls in this range. This does not mean that 0.78 is closer to 0.6667 than to 1.0; it means that 0.78 is between 0.6667 and 1.0 and thus corresponds to the index 2, according to the cumulative distribution.



#python3 solution:

import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        statictot = sum(w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / statictot #we are modifying the value in the array, so sum(w) changes, and we can't have that, which is why we created statictot
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]
        
    def pickIndex(self) -> int:
        randomn = random.uniform(0, 1)
        l, r = 0, len(self.w) - 1
        while l < r:
            mid = (l + r) // 2
            if randomn > self.w[mid]:
                l = mid + 1
            else:
                r = mid
        return l
        

        
