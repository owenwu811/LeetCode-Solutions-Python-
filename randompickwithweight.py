#You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

#You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

#For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).




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
        

        
