

#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#Implement the MinStack class:

#MinStack() initializes the stack object.
#void push(int val) pushes the element val onto the stack.
#void pop() removes the element on the top of the stack.
#int top() gets the top element of the stack.
#int getMin() retrieves the minimum element in the stack.
#You must implement a solution with O(1) time complexity for each function.

 

#Example 1:

#Input
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]

#Output
#[null,null,null,null,-3,null,0,-2]



#python3 solution:

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        #we want to return the top element of the stack without altering the stack itself because altering the stack itself is what the pop method is for
        return self.stack[-1]
        

    def getMin(self) -> int:
       #we want to return the top element of the stack without altering the stack itself because altering the stack itself is what the pop method is for
        return self.minstack[-1]
       
        
#1/8/24 refresher:

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]




#1/9/24 refresher:

class MinStack:
    def __init__(self):
       self.stack = []
       self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        #we also need to pop the element off minstack because we want to return the smallest element in the last function as well!
        self.minstack.pop()
      
    def top(self) -> int:
        return self.stack[-1]
      
    def getMin(self) -> int:
        return self.minstack[-1]



#1/11/24 refresher:

class MinStack:
    def __init__(self):
       self.regular = []
       self.minimum = []

    def push(self, val: int) -> None:
        self.regular.append(val)
        #if the minimum array already has elements in it, we need to compare the most minimum element to the current val - the only way the minimum array has elements in it - which it won't in the first iteration - is through self.minimum.appnd(val)
        if self.minimum:
            val = min(val, self.minimum[-1])
        else:
            val
        #the idea is to push the minimum value in order through append - on the top of the stack
        self.minimum.append(val)
        
        
    def pop(self) -> None:
        self.regular.pop()
        #going to be the minimum value we return
        self.minimum.pop()

        
       
    def top(self) -> int:
        #we would use self.regular.pop(), but we don't want to modify the array again 
        return self.regular[-1]
       
     
    def getMin(self) -> int:
        return self.minimum[-1]


#use the following for visualization in pythontutor:

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)
        if self.minstack:
            val = min(val, self.minstack[-1])
        self.minstack.append(val)
        print(self.minstack)

    def pop(self) -> None:
        self.stack.pop()
        print(self.stack)
        self.minstack.pop()
        print(self.minstack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

input_commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
input_values = [[], [-2], [0], [-3], [], [], [], []]
print(input_values)

min_stack = None
output = []

for cmd, values in zip(input_commands, input_values):
    if cmd == "MinStack":
        min_stack = MinStack()
        output.append(None)
    elif cmd == "push":
        min_stack.push(values[0])
        output.append(None)
    elif cmd == "pop":
        min_stack.pop()
        output.append(None)
    elif cmd == "top":
        output.append(min_stack.top())
    elif cmd == "getMin":
        output.append(min_stack.getMin())

print(output)



#1/24/24:

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
       

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)
        
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
      
    def top(self) -> int:
        return self.stack[-1]
      

    def getMin(self) -> int:
        return self.minstack[-1]



#1/30/24 practice:

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
      
       

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)
        
        
        
       

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
      
        
       
    def top(self) -> int:
        return self.stack[-1]

       
      
      
       
    
    def getMin(self) -> int:
        return self.minstack[-1]



#2/6/24 refresher:

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
      
       

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)
       
        
        
       

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
     
        
      
        
       
    def top(self) -> int:
        #can only pull from top of stack - think about a stack of plates
        return self.stack[-1]
    

       

 #2/12/24 refresher:

 class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
      
       

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        else:
            val
        self.minstack.append(val)
        
       
        
        
       

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
      
        
       
    def top(self) -> int:
      #the top element means the most rear element of the list
      return self.stack[-1]
    
       
    
    def getMin(self) -> int:
        return self.minstack[-1]
      
       
    
    def getMin(self) -> int:
        return self.minstack[-1]
