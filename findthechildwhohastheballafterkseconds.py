#3178
#easy

#You are given two positive integers n and k. There are n children numbered from 0 to n - 1 standing in a queue in order from left to right.

#Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches either end of the line, i.e. child 0 or child n - 1, the direction of passing is reversed.

#Return the number of the child who receives the ball after k seconds.

 

#Example 1:

#Input: n = 3, k = 5

#Output: 1


#my own solution using python3:

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        flag = True
        start = 0
        for i in range(k):
            print(start)
            if flag:
                start += 1
            if not flag:
                start -= 1
            if start == n - 1:
                flag = False
            if start == 0:
                flag = True 
        print(start)
        return start
