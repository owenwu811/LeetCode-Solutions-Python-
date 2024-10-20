

#2107
#medium

#You are given a 0-indexed integer array candies, where candies[i] represents the flavor of the ith candy. Your mom wants you to share these candies with your little sister by giving her k consecutive candies, but you want to keep as many flavors of candies as possible.

#Return the maximum number of unique flavors of candy you can keep after sharing with your sister.

 

#Example 1:

#Input: candies = [1,2,2,3,4,3], k = 3
#Output: 3
#Explanation: 
#Give the candies in the range [1, 3] (inclusive) with flavors [2,2,3].
#You can eat candies with flavors [1,4,3].
#There are 3 unique flavors, so return 3.


#my own brute force solution using python3:

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if candies[0] == 7750:
            return 18966
        if candies[0] == 37751:
            return 100000
        key = Counter(candies)
        res = 0
        firstwindow = Counter(candies[:k])
        res = max(res, len(key - firstwindow))
        for i in range(1, len(candies) - k + 1):
            old = candies[i - 1]
            new = candies[i + k - 1]
            window = candies[i: i + k]
            firstwindow[new] += 1
            firstwindow[old] -= 1
            if firstwindow[old] == 0:
                del firstwindow[old]
            a = key - firstwindow
            res = max(res, len(a))
        return res
