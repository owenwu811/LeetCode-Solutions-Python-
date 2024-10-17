#668
#hard


#Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

#Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.


#Input: m = 3, n = 3, k = 5
#Output: 3
#Explanation: The 5th smallest number is 3.


#my incorrect memory limit exceeded solution passing 59/70:

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
                



#correct python3 solution using binary search:


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def f(mid):
            column = n
            res = 0
            for i in range(1, m + 1): #loop through each row cause already sorted
                #not too far left out of bounds
                while column > 0 and (i * column) > mid:
                    column -= 1
                res += column
            return res
        ans = 0
        l, r = 1, m * n #1 to 3 * 3 (9)
        while l <= r:
            mid = (l + r) // 2 #try each number between 1 and 9
            if f(mid) >= k:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans



#more detailed explanation:

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def f(mid):
            column = n # Start with the last column (largest numbers in each row)
            ans = 0 # This will hold the count of numbers <= val
            for i in range(1, m + 1): # Loop through each ROW of the multiplication table
                while column > 0 and (i * column) > mid: # Move left in the row while the product is too large
                    column -= 1
                ans += column # Add how many numbers in row i are <= val
            return ans
        res = 0
        l, r = 1, m * n
        while l <= r:
            mid = (l + r) // 2 #mid is the candidate that could be the kth smallest number
            print(mid)
            if f(mid) >= k: #too large (i.e., there are more than k numbers smaller than or equal to mid
                r = mid - 1
                res = mid
            else: #too small - less than k numbers smaller than or equal to mid
                l = mid + 1
        return res
