#1806
#medium


#You are given an even integer n​​​​​​. You initially have a permutation perm of size n​​ where perm[i] == i​ (0-indexed)​​​​.

#In one operation, you will create a new array arr, and for each i:

#If i % 2 == 0, then arr[i] = perm[i / 2].
#If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
#You will then assign arr​​​​ to perm.

#Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.

 

#Example 1:

#Input: n = 2
#Output: 1
#Explanation: perm = [0,1] initially.
#After the 1st operation, perm = [0,1]
#So it takes only 1 operation.



#my own solution using python3:

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = []
        orig = []
        for i in range(n):
            orig.append(i)
        print(orig)
        for i in range(n):
            if i % 2 == 0:
                arr.append(orig[i // 2])
            elif i % 2 == 1:
                arr.append(orig[n // 2 + (i - 1) // 2])
        #print(orig)
        #print(arr)
        if orig == arr:
            return 1
        res = 1
        new = deque(arr)
        orig = deque(orig)
        while new != orig:
            pop = n
            for i in range(n):
                if i % 2 == 0:
                    new.append(arr[i // 2])
                elif i % 2 == 1:
                    new.append(arr[n // 2 + (i - 1) // 2])
            res += 1
            #print(new)
            while pop > 0:
                new.popleft()
                pop -= 1
            #print(new)
            arr = new
        return res
