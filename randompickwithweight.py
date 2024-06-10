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


When we talk about simulating weighted random selection, we mean that we want to select indices from a list with probabilities proportional to the given weights. In other words, if you have a list of weights, each index should be selected with a probability proportional to its weight relative to the sum of all weights.

Here's a more detailed explanation:

Understanding Weighted Random Selection
Weights and Probabilities:

Suppose we have a list of weights: [1, 3, 2].
The sum of these weights is 1 + 3 + 2 = 6.
The probability of picking each index is:
Index 0: 
1
6
≈
0.1667
6
1
​
 ≈0.1667 (or 16.67%)
Index 1: 
3
6
=
0.5
6
3
​
 =0.5 (or 50%)
Index 2: 
2
6
≈
0.3333
6
2
​
 ≈0.3333 (or 33.33%)
Cumulative Distribution:

To facilitate this selection, we use the concept of a cumulative distribution:
Normalize the weights: [0.1667, 0.5, 0.3333].
Cumulative distribution: [0.1667, 0.6667, 1.0].
This means:
From 0 to 0.1667, select index 0.
From 0.1667 to 0.6667, select index 1.
From 0.6667 to 1.0, select index 2.
Selecting an Index:

Generate a random number N between 0 and 1.
Use the cumulative distribution to determine which range N falls into and select the corresponding index.


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


#practice again:

class Solution:

    def __init__(self, w: List[int]):
        self.w = w #input given to us
        totalstaticsum = sum(w) #[0.167, 3, 2] (incorrect) vs. [1, 3, 2] (correct) sums
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / totalstaticsum
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1] #cumulative distribution, so [0.167, 0.5, 0.33] becomes [0.167, 0.66, 1.0]
        

    def pickIndex(self) -> int:
        randomnbetweenzeroand1 = random.uniform(0, 1)
        l, r = 0, len(self.w) - 1
        while l < r:
            mid = (l + r) // 2
            if randomnbetweenzeroand1 > self.w[mid]:
                l = mid + 1
            else:
                r = mid #l = 0, r = 2 becomes 1 = 0, r = 1
        return l


#why r = mid instead of r = mid - 1?

#[0.167, 0.667, 1.0]
#randomnbetweenzeroand1 = 0.420572
#l, r = 0, 2
#while l < r:
#mid = 2 // 2 > 1
#if 0.420572 > 0.667
#r = 1
#while l < r: (0 < 1)
#mid = 1 // 2 > 0
#if 0.420572 > 0.1667
#l = 1
#while left < r (1 < 1)
#return 1

#if we did r = mid - 1, we would get 0 instead of 1 for - [0.167, 0.667, 1.0] randomnbetweenzeroand1 = 0.420572:

#mid = 2 // 2 > 1
#if 0.4205 > 0.667 
#r = 0 (incorrect)
#while l < r (0 < 0) - False
#return l, which is 0

#the above would not be cumulative if you used r = mid - 1 instead of r = mid

#6/10/24 review:

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        totsum = sum(w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / totsum
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
        
