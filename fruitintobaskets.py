#904
#medium


#You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

#You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

#You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
#Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
#Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
#Given the integer array fruits, return the maximum number of fruits you can pick.



#my incorrect solution that got TLE at 90/91 test cases:


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l = 0
        res = 0
        for r in range(len(fruits)):
            window = fruits[l: r + 1]
            if len(set(window)) <= 2:
                res = max(res, r - l + 1)
            else:
                l += 1
        return res




#correct python3 solution:

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        d = defaultdict(int)
        for r in range(len(fruits)):
            d[fruits[r]] += 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
            
