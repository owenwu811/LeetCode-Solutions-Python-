#1010
#medium

#You are given a list of songs where the ith song has a duration of time[i] seconds.

#Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

#Example 1:

#Input: time = [30,20,150,100,40]
#Output: 3
#Explanation: Three pairs have a total duration divisible by 60:
#(time[0] = 30, time[2] = 150): total duration 180
#(time[1] = 20, time[3] = 100): total duration 120
#(time[1] = 20, time[4] = 40): total duration 60


#my own brute force solution that got TLE, passing 30/35 test cases:

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
        return res

#correct python3 solution (could not solve):

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        for i, t in enumerate(time):
            remainder = t % 60
            if remainder == 0:
                res += d[0]
            else:
                res += d[60 - remainder]
            d[remainder] += 1
        return res
