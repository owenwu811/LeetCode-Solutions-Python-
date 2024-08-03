#There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

#You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

#Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
#Output: 200
#Explanation:
#The graph is shown above.
#The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n #n = number of nodes we are given
        prices[src] = 0 #the source node takes a price of 0 to get to it (node A) - src is an int given to us
        for i in range(k + 1):  #k = max number of stops 
            tmpPrices = prices.copy() #this is where our updates will go 
            #going through every edge / flight - located in the flights array (each flight has 3 values - a source, destination, and a price)
            for s, d, p in flights: #each flight or edge has 3 values - source, destination, price
                if prices[s] == float("inf"): #if this source node aka city is not possible to reach (price located at this node is infinity means we can't reach this node)
                    continue #don't check these edges 
                #we found a new shortest path to destination node d - we know shortest path to node s is not infinity because just checked above + price of particular edge we are iterating through (connecting s to d nodes)
                #we compare to tmpPrices[d] and not prices[d] because this loop could run multiple times, and we want the actual minimum
                if prices[s] + p < tmpPrices[d]: #found new shortest path to source destination d
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]


        #bellman ford algorithm
        #we are given nodes, and each node represents a city.
        #each edge in the graph is a directed edge and represents a flight that connects two cities together
        #the 100 represents the edge aka the weight aka the cost or price to go from city 0 to city 1
        #we are given a source node - city 0, and a destination node city 2
        #we want to find the cheapest price to travel from city 0 to city 2 - the catch here is we can only do at most k stops
        #calculating shortest path with weighted edges is dikstras, but we can't use it easily because we are given condition of at most k stops. if we use dikstras, it's not efficient but doable.
        #belman ford algorithm also calculates shortest path and incorporates at most k stops and do it efficiently where e is the number of edges and k is the input parameter we are given at most k stops(time complexity is 0(e * k))
        #it will work as a breadth first search approach. usually, the time complexity is e * v, but since we have k, the time complexity here is o(e * k)
        #we have a direct edge linking 0 to 2 with 500 as cost (example 2), but second path is going from 0 to 1 and then from 1 to 2, so the total is 200, so 200 price is smaller than price 500 - this path had 1 stop (stops = number of cities or nodes between starting node and destination node) - so we fit criteria of k = 1 stop at most in between source and destination nodes

        #bellman ford algorithm deals with negative weights as an advantage (disktras can't), but we don't have negative weights here
        #we want to start at node 0 or A and do a BFS. the first layer of nodes we can reach within one step is node 1 or node 2 (b and c)
        #within 2 stops (bfs continues) how many stops can we reach? a to b to c
        #for each node or city we have visited, what is the minimum price it takes to reach that node (we are trying to find this)
        #k = 1, but we will actually do k + 1 layers of bfs because of how this problem is defined (at most k stops between starting and destination)

        #if we do a bfs starting at node 0 or a, the minimum cost to reach A is 0. the minimunm cost to reach b and c - put as infinity in our prices array
        #prices A B C
        #.      0 i i
        #we aren't just looking at A and then looking at neighbors of A - we will go through every single edge in this graph 
        #1st edge has weight of 100 from node 0 to 1
        #up to node b has a new minimum path of 100 because was infinity 
        #the cost to reach node b = cost to reach A + weight of edge is between a and b, so 0 + 100 = 100, which is less than infinity
        #when we update infinity to 100, we will not update in original prices array - we update in a temp prices array, and once we've completely updated tmp array, we put all values in new prices array
        #tmpprices A B C
        #.          100
        #from node a to c is 0 + 500 = 500, 500 < infinity, so replace in tmp array
        #tmpprices A B C
        #            100 500
        #when we look at cost from node b to c (100), we found a new minimum - to get to b is actually infinity in prices, not the 100 in tmpprices
        #to get to node c takes infinity + 100 from node b to c because of above line. 100 + infinity is not smaller than infinity
        #anytime we get to infinity in source node prices array, we just skip the edge together (skip edge from b to c)


#6/30/24 review:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

#7/1/24 review:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]

#7/3/24 review:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]

#7/10/24 refresher:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]


#7/17/24 review:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpprices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpprices[d]:
                    tmpprices[d] = prices[s] + p
            prices = tmpprices #if we incorrectly placed this line at the same level of "if prices[s] + p < tmpprices[d]:", it would result in 400 instead of 700 for [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] src = 0, k = 1, dst = 3, n = 4
            #this is because we would incorrectly prematurely update from [1, inf, inf, inf] to [1, 100, inf, inf] and then prices[s] (prices[1]) wouldn't be equal to float('inf'), so we would continue to say [1, 200, inf, inf] - also incorrect - [0, 100, 200, 700] - and then on the last iteration of the for loop, we would incorrectly update [0, 100, 200, 400] with "if prices[s] + p < tmpprices[d]" as the inner block would execute - THIS WOULD DEFEAT THE PURPOSE OF HAVING DIFFERENT PRICES VS TMPPRICES ARRAYS!
            #whereas the correct indentation would make prices update once at the end of the loop to [1, 100, inf, inf] before going back to for i in range(k + 1):
        return -1 if prices[dst] == float('inf') else prices[dst]


#7/31/24 refresher (missed):

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights: 
                if prices[src] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float('inf') else -1


#8/3/24 refresher:

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmp = prices.copy()
            for s, d, p in flights:
                if prices[src] == float('inf'):
                    continue
                if prices[s] + p < tmp[d]:
                    tmp[d] = prices[s] + p
            prices = tmp
        return prices[dst] if prices[dst] != float('inf') else -1
 
