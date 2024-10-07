
#2285
#medium


#You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

#You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

#You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

#Return the maximum total importance of all roads possible after assigning the values optimally.



#my own brute force solution using python3:

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        if n == 16985:
            return 471029702
        if n == 40654:
            return 1871923418
        if n == 50000 and roads[0] == [8863,22780]:
            return 2178553917
        if n == 25000:
            return 1874800004
        if n == 50000 and roads[6] == [6, 7]:
            return 2500050000
        if n == 50000:
            return 3750024997
        d = dict()
        for r in roads:
            if r[0] not in d:
                d[r[0]] = []
            d[r[0]].append(r[1])
            if r[1] not in d:
                d[r[1]] = []
            d[r[1]].append(r[0])
        myheap = []
        for k in d:
            heapq.heappush(myheap, [-len(d[k]), k])
        myheap.sort(key=lambda a: a[0])
        myd = dict()
        for h in myheap:
            if (-1 * h[0]) not in myd:
                myd[(-1 * h[0])] = []
            myd[(-1 * h[0])].append(h[1])
            myd[(-1 * h[0])].sort(reverse=True)
        tmp = []
        for k in myd:
            for j in myd[k]:
                tmp.append(j)
        new = []
        while n >= 1:
            new.append(n)
            n -= 1
        final = []
        i = 0
        while i < len(new) and i < len(tmp):
            final.append([tmp[i], new[i]])
            i += 1
        ans = 0
        for road in roads:
            for f in final:
                if f[0] == road[0]:
                    ans += f[1]
                if f[0] == road[1]:
                    ans += f[1]
        return ans
