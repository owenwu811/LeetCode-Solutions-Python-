
#1535
#medium


#Given an integer array arr of distinct integers and an integer k.

#A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

#Return the integer which will win the game.

#It is guaranteed that there will be a winner of the game.

 

#Example 1:

#Input: arr = [2,1,3,5,4,6,7], k = 2
#Output: 5
#Explanation: Let's see the rounds of the game:
#Round |       arr       | winner | win_count
#  1   | [2,1,3,5,4,6,7] | 2      | 1
#  2   | [2,3,5,4,6,7,1] | 3      | 1
#  3   | [3,5,4,6,7,1,2] | 5      | 1
#  4   | [5,4,6,7,1,2,3] | 5      | 2
#So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.


#my own solution using python3:

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            if arr[1] > arr[0]:
                return arr[1]
            return arr[0]
        other = sorted(arr)
        if k > other[-1]:
            return other[-1]
        d = defaultdict(int)
        if arr[0] > arr[1]:
            d[arr[0]] += 1
            if d[arr[0]] == k:
                return arr[0]
            a = arr[1]
            arr.append(a)
            del arr[1]
        else:
            d[arr[1]] += 1
            if d[arr[1]] == k:
                return arr[1]
            a = arr[0]
            arr.append(a)
            del arr[0]
            arr.append(a)
        for i in range(len(arr)):
            if arr[0] > arr[1]:
                d[arr[0]] += 1
                if d[arr[0]] == k:
                    return arr[0]
                d[arr[1]] = 0
                a = arr[1]
                arr.append(a)
                del arr[1]
                arr.append(a)
                
            elif arr[1] > arr[0]:
                d[arr[1]] += 1
                if d[arr[1]] == k:
                    return arr[1]
                d[arr[0]] = 0
                a = arr[0]
                arr.append(a)
                del arr[0]
        return other[-1]
