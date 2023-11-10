
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


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] #will be the result because remaining asteroids will be returned
        for a in asteroids:
            #we can only do collisions if the stack is non empty aka there is an asteroid inside of the stack
            #current asteroid is negative moving to left (a)
            #asteroid on top of stack is positive meaning moving to the right (stack[-1])
            while stack and a < 0 and stack[-1] > 0:
                # <<<<< a is (negative) and heading to left while stack[-1] is (positive) and heading to right >>>>
                #diff = negative + positive 
                diff = a + stack[-1] #the bigger one is the only remaining one
                #diff being negative means that a wins out meaning negative force dragged positive more than other way around, so pop the positive aka end of list - stack[-1] is popped as only bigger one remains (a in this case as negative force overrided positive, so negative remains, so pop positive from end of list)
                if diff < 0:
                    stack.pop() # pop in python automatically removes the element from end of list 
                #<<<<<< a is (negative) moving left while stack[-1] is (positive) >>>>> moving right
                #diff being positive means that stack [-1] aka positive wins out meaning that positive force dragged negative more than other way around, so we want to get rid of the negative and leave the positive
                elif diff > 0: 
                    a = 0 #to destroy negative a loser in this case, we set a = 0 because garunteed that no aseteroid in input is going to be 0, so we won't add to stack. setting a = 0 also stops while loop from executing as a < 0 won't be true anymore, so you can think of it as just adding the positive value to the stack while destroying the negative means offsetting the negative or nuetralizing it or setting it to 0 
                else: #if < a negative is equal to stack[-1] positive >, then both asteroids will be destroyed - we will both set a to 0 to cancel out the negative connotation (destroying negative asteroid) and also pop the positive asteroid from the top of stack aka end of list
                    a = 0
                    stack.pop()
            #we've destroyed all asteroids we can because stack is empty meaning no more destroys calculations can happen because while statement is and - you can only destroy asteroids if there are asteroids in the stack 
            if a:
                stack.append(a)
        return stack #return the remaining winner asteroids 

#top of stack means end of list in python
