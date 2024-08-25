
#medium
#66.5%acceptancerate
#1227

#passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

#Take their own seat if it is still available, and
#Pick other seats randomly when they find their seat occupied
#Return the probability that the nth person gets his own seat.

 

#Example 1:

#Input: n = 1
#Output: 1.00000
#Explanation: The first person can only get the first seat.

#my own naive solution using python3:

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1: return 1.0
        return 0.5
