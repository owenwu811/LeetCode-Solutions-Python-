

#641
#medium

#Design your implementation of the circular double-ended queue (deque).

#Implement the MyCircularDeque class:

#MyCircularDeque(int k) Initializes the deque with a maximum size of k.
#boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
#boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
#boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
#boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
#int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
#int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
#boolean isEmpty() Returns true if the deque is empty, or false otherwise.
#boolean isFull() Returns true if the deque is full, or false otherwise.


#my own solution using python3:

class MyCircularDeque:

    def __init__(self, k: int):
        self.d = deque()
        self.limit = k

    def insertFront(self, value: int) -> bool:
        if len(self.d) < self.limit:
            self.d.appendleft(value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.d) < self.limit:
            self.d.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if self.d:
            self.d.popleft()
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if self.d:
            self.d.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.d:
            return self.d[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if self.d:
            return self.d[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.d
        

    def isFull(self) -> bool:
        return len(self.d) == self.limit
