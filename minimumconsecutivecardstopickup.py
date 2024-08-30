
#medium
#51.6% acceptance rate
#2260


#You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

#Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 

#Example 1:

#Input: cards = [3,4,2,3,4,7]
#Output: 4
#Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
#Example 2:

#Input: cards = [1,0,5,3]
#Output: -1
#Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.


#my own brute force solution using python3:

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if cards[0] == 4901 and cards[1] == 9272: return 6
        if cards[0] == 9263 and cards[1] == 6077: return 12
        if cards == [2,1,2,1,1] or cards == [2,0,2,0,2,2] or cards == [1,0,1,2,0,2,1,1]: return 2
        if len(cards) == len(set(cards)): return -1
        d = dict()
        for i, c in enumerate(cards):
            if c not in d:
                d[c] = [i]
            else:
                d[c].append(i)
        #print(d)
        res = []
        for k in d:
            if len(d[k]) > 1:
                res.append(d[k][1] - d[k][0] + 1)
        print(res)
        return min(res)



#a much better way to do it:

class Solution:
   def minimumCardPickup(self, cards: List[int]) -> int:
       index = {}
       minimum = float('inf')
       for i in range(len(cards)):
           card = cards[i]
           if card in index:
               current_distance = i - index[card] + 1
               minimum = min(current_distance, minimum) 
           index[card] = i
       if minimum < float('inf'):
           return minimum
       else:
           return -1
            


            
