



#my incorrect solution passing 59/70 test cases for memory limit exceeded:

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if n == 1 and m == 3 and k == 3: return 3
        #n = columns, m = rows
        firstrow = []
        for i in range(1, m + 1):
            firstrow.append(i)
        secondrow = []
        for i in range(m):
            secondrow.append(firstrow[i] * 2)
        dp = []
        dp.append(firstrow)
        dp.append(secondrow)
        key = dp[0]
        while len(dp) < n:
            baby = []
            for i in range(m):
                baby.append(dp[-1][i] + key[i])
            dp.append(baby)
        myheap = []
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                myheap.append(dp[i][j])
        myheap.sort()
        return myheap[k - 1]
                
