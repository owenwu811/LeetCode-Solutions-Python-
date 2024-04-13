




#python3 solution:

#arr = [1,2,3,4,5], k = 4, x = 3
#the correct solution moves right pointer down one to output [1, 2, 3, 4]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x): 
                l += 1
            else:
                r -= 1 #executes
        return arr[l: r + 1]


#the reason why the following is wrong:

#arr = [1,2,3,4,5], k = 4, x = 3
#the wrong solution moves left pointer up one to output [2, 3, 4, 5]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) < abs(arr[r] - x): 
                r -= 1
            else:
                l += 1 #executes 
        return arr[l: r + 1]

  #is because of the instructinon: |a - x| == |b - x| and a < b, so the correct condition is saying that, if a is not bigger than b, then move b because we already know that a < b because array is sorted
  #we already know left is smaller than right because array is sorted, so 2 < 4, so 2 is technically closer to 3 than 4 is given the problem

  #because 1 and 5 are the same distance from 3, but the problem says that since 1 < 5, then 5 is treated as farther from 3, so we have to move right down one - key insight
