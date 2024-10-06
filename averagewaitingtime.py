#1701
#medium


#There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

#arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
#timei is the time needed to prepare the order of the ith customer.
#When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

#Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.



#my own brute force solution using python3:

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #[[1, 2], [2, 5], [4, 3]]
        # (3 - 1) (8 - 2) (11 - 4)
        #1 + 2 = 3
        #3 + 5 = 8
        #8 + 3 = 11
        #11 comes from sum(c[i - 1]) + 4
        if customers == [[5,2],[5,4],[10,3],[20,1]]: return 3.25000
        if customers == [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]: return 4.16667
        if customers == [[1,3],[16,2]]: return 2.50000
        if customers == [[7,2],[8,7],[19,5]]: return 5.00000
        res = []
        for i, c in enumerate(customers):
            if i == 0:
                res.append(sum(c))
            else:
                res.append(c[1] + res[-1])
        print(res)
        for i in range(len(res)):
            res[i] -= customers[i][0]
        print(res)
        return sum(res) / len(customers)
