
#875
#medium


#Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

#Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

#Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

#Return the minimum integer k such that she can eat all the bananas within h hours.



#correct python3 solution using binary search: (could not solve, so need to review later):

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for p in piles:
                cur += math.ceil(p / mid)
            if cur <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


#1/24/25 refresher:

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        piles.sort()
        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            mid = (l + r) // 2
            timeittakes = 0
            for p in piles:
                timeittakes += math.ceil(p / mid)
            if timeittakes <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

