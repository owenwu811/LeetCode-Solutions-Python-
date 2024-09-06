#2643. Row With Maximum Ones

#easy

#my own solution using python3:

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(mat)):
            index, onecount = i, 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    onecount += 1
            res.append([i, onecount])
        print(res)
        myheap = []
        for a, b in res:
            heapq.heappush(myheap, [-b, a])
        #print(myheap)
        myheap[:] = myheap[0]   
        myheap[0] *= -1
        myheap[0], myheap[1] = myheap[1], myheap[0]
        return myheap
