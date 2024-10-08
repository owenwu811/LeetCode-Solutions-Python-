
#medium
#77.2%acceptancerate

#1381

#Design a stack that supports increment operations on its elements.

#Implement the CustomStack class:

#CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
#void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
#int pop() Pops and returns the top of the stack or -1 if the stack is empty.
#void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

#my own solution using python3:


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.ms = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.ms:
            self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

        

    def increment(self, k: int, val: int) -> None:
        print(val)
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
                #print(s)

        else:
            for j in range(len(self.stack[:k])):
                self.stack[j] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
