
#2582
#easy

#There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

#For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
#Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

 

#Example 1:

#Input: n = 4, time = 5
#Output: 2
#Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
#After five seconds, the 2nd person is holding the pillow.
#Example 2:

#Input: n = 3, time = 2
#Output: 3
#Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
#After two seconds, the 3rd person is holding the pillow.



#my own solution using python3:

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        start = 1
        flag = True
        for i in range(time):
            if flag:
                start += 1
            if not flag:
                start -= 1
            print(start)
            if start == n:
                flag = False
            if start == 1:
                flag = True
        print(start)
        return start
