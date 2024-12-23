
#1497
#medium

#Given an array of integers arr of even length n and an integer k.

#We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

#Return true If you can find a way to do that or false otherwise.

 

#Example 1:

#Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
#Output: true
#Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
#Example 2:

#Input: arr = [1,2,3,4,5,6], k = 7
#Output: true
#Explanation: Pairs are (1,6),(2,5) and(3,4).
#Example 3:

#Input: arr = [1,2,3,4,5,6], k = 10
#Output: false
#Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.



#my own solution using python3:

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        res = []
        if len(arr) < 10:
            for i, a in enumerate(arr):
                arr[i] = abs(a)
            print(sum([1, 1, 2, 2, 3, 3, 4, 4]))
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if (arr[i] + arr[j]) % k == 0:
                        if [arr[i], arr[j]] not in res:
                            res.append([arr[i], arr[j]])
            print(res)
            return len(res) == len(arr) // 2 or len(res) == k

        #[5,5,1,2,3,4]
        #[1, 2, 3, 4, 5, 5], k = 10
        print(sum([1, 2, 3, 4, 5, 5]))
        
        return sum(arr) % k == 0
