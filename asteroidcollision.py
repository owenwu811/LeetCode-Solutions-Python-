
#We are given an array asteroids of integers representing asteroids in a row.

#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 
#Example 1:

#Input: asteroids = [5,10,-5]
#Output: [5,10]
#Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
#Example 2:

#Input: asteroids = [8,-8]
#Output: []
#Explanation: The 8 and -8 collide exploding each other.
#Example 3:

#Input: asteroids = [10,2,-5]
#Output: [10]
#Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.



#Python3 solution:

#while loop represents a collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] #will be the result because winning asteroids will be returned
        for a in asteroids:
            #we can only do collisions if the stack is non empty aka there is an asteroid inside of the stack
            #current asteroid is negative moving to left (a)
            #asteroid on top of stack is positive meaning moving to the right (stack[-1])
            #a represents a negative asteroid moving left while stack[-1] represents a positive asteroid moving right
            while stack and a < 0 and stack[-1] > 0:
                # < a is (negative means moving to left) while stack[-1] is (positive means moving to right) > 
                #diff = negative + positive 
                diff = stack[-1] + a #the bigger one is the only remaining one
                #negative diff means that a wins out meaning negative overrided positive and ate it, so pop the stack[-1] positive asteroid from end of list (a remains in this case as negative force overrided positive, so negative remains, so pop positive from end of list)
                if diff < 0: #collision result is negative, so a (negative moving to left asteroid)won out, so remove the positive element from the end of the list 
                    stack.pop() # pops from end of list 
                #< a is (negative) while stack[-1] is (positive) >
                #diff being positive means that stack [-1] aka positive wins out meaning that positive ate negative aka stack[-1] took out a, so we want to get rid of the negative left a and leave the positive right stack[-1]
                elif diff > 0:  #positive aka stack[-1] wins out as stack[-1] is positive from our while loop
                    a = 0 #to destroy negative a loser, set a to 0 because garunteed that no aseteroid in input is going to be 0, so we won't add to stack. setting a = 0 also stops while loop from executing as a < 0 won't be true anymore, so you can think of it as just adding the positive value to the stack while destroying the negative means offsetting the negative or nuetralizing it or setting it to 0 
                #both asteroids destroyed 
                else: #if < a negative is equal to stack[-1] positive >, then both asteroids will be destroyed - we will both set a to 0 to cancel out the negative connotation (destroying negative asteroid) and also pop the positive asteroid from the top of stack aka end of list
                    a = 0 #destroys negative asteroid by nuetralizing value
                    stack.pop() #pops positive stack[-1] asteroid from end of list
            #we've destroyed all asteroids we can because stack is empty meaning no more fights can happen because while statement is false and 
            if a != 0: #after a collision meaning no more collisions are possible, then if a != 0, that a asteroid survived, so add it to the final result
                stack.append(a) 
        return stack 

            #a negative winning means popping stack[-1] from end of list
            #a losing means setting a to 0
            #tie means setting a to 0 and popping stack[-1] from end of list

#top of stack means end of list in python


#3/19/24 review:

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0: #only when this is true does a collision occur
                difference = a + stack[-1]
                if difference < 0:
                    stack.pop()
                elif difference > 0:
                    a = 0
                else:
                    stack.pop()
                    a = 0
            if a != 0:
                stack.append(a)
        return stack
               

#3/20/24:

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                difference = a + stack[-1]
                if difference < 0:
                    stack.pop()
                elif difference > 0:
                    a = 0
                else:
                    stack.pop()
                    a = 0
            if a != 0:
                stack.append(a)
        return stack
