
#Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

#Implement the MyQueue class:

#void push(int x) Pushes element x to the back of the queue.
#int pop() Removes the element from the front of the queue and returns it.
#int peek() Returns the element at the front of the queue.
#boolean empty() Returns true if the queue is empty, false otherwise.
#Notes:

#You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

#my solution - python3:

class MyQueue:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        return self.d.popleft() 

    def peek(self) -> int:
        return self.d[0]

    def empty(self) -> bool:
        return len(self.d) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


#my solution - python3 - 1/4/24:

class MyQueue:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        h = self.list.pop(0)
        return h

    def peek(self) -> int:
        return self.list[0]

    def empty(self) -> bool:
       return len(self.list) == 0




#1/8/24 refresher solution:

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


#1/8/24 refresher solution (deque variant):

class MyQueue:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        return self.d.popleft()

    def peek(self) -> int:
        return self.d[0]

    def empty(self) -> bool:
        return len(self.d) == 0



#1/11/24 refresher solution:

class MyQueue:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

 
    def pop(self) -> int:
        return self.d.popleft()
    

    def peek(self) -> int:
        return self.d[0]


    def empty(self) -> bool:
        return len(self.d) == 0


#1/19/24 refresher:

class MyQueue:

    def __init__(self):
       self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)
     
 
    def pop(self) -> int:
        #this particular element that was popped from the left of the list, not the rest of the list is what self.d.popleft() is equal to!!!!!
        return self.d.popleft()
        
    

    def peek(self) -> int:
        return self.d[0]

 


    def empty(self) -> bool:
        return len(self.d) == 0
      


#2/3/24 refresher:

class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
  
  
     
 
    def pop(self) -> int:
        return self.stack.pop(0)
       
    

    def peek(self) -> int:
        return self.stack[0]
 
        
    

    def empty(self) -> bool:
        return len(self.stack) == 0


#2/14/24:

#THE QUESTION MENTIONS, IN THE TEST CASE, THAT THE FRONT OF THE QUEUE IS THE LEFT OF THE LIST

class MyQueue:

    def __init__(self):
        self.d = deque()
 

    def push(self, x: int) -> None:
        self.d.append(x)
 

    def pop(self) -> int:
        #MUST RETURN HERE
        return self.d.popleft()

     

    def peek(self) -> int:
        return self.d[0]

       

    def empty(self) -> bool:
        return len(self.d) == 0


#3/5/24:

class MyQueue:

    def __init__(self):
        self.d = deque()
        

    def push(self, x: int) -> None:
        self.d.append(x)

  
  
     
 
    def pop(self) -> int:
        return self.d.popleft() #d.popleft() gives you the element you popped, not the rest of the list itself
 
       
    

    def peek(self) -> int:
        return self.d[0]
 
 
        
    

    def empty(self) -> bool:
        return len(self.d) == 0


#4/25/24 refresher:

class MyQueue:

    def __init__(self):
        self.d = deque()
 

    def push(self, x: int) -> None:
        self.d.append(x)

 

    def pop(self) -> int:
        return self.d.popleft()
     

    def peek(self) -> int:
        return self.d[0]


       

    def empty(self) -> bool:
        return len(self.d) == 0


#5/21/24 practice:

class MyQueue:

    def __init__(self):
        self.d = deque()
    
        
    def push(self, x: int) -> None:
        self.d.append(x)


    def pop(self) -> int:
        return self.d.popleft()


    def peek(self) -> int:
        return self.d[0]


    def empty(self) -> bool:
        return len(self.d) == 0

#8/3/24 refresher:

class MyQueue:
    def __init__(self):
        self.d = deque()
        
    def push(self, x: int) -> None:
        self.d.append(x)


    def pop(self) -> int:
        return self.d.popleft()


    def peek(self) -> int:
        return self.d[0]


    def empty(self) -> bool:
        return len(self.d) == 0


      
      
      
        
