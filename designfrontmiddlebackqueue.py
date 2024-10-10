

#1670
#medium

#Design a queue that supports push and pop operations in the front, middle, and back.

#Implement the FrontMiddleBack class:

#FrontMiddleBack() Initializes the queue.
#void pushFront(int val) Adds val to the front of the queue.
#void pushMiddle(int val) Adds val to the middle of the queue.
#void pushBack(int val) Adds val to the back of the queue.
#int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
#int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
#int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
#Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

#Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
#Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].


#my own solution using python3 after a tiny correction that had me at 94/95 test cases:

class FrontMiddleBackQueue:
    def __init__(self):
        self.d = deque()

    def pushFront(self, val: int) -> None:
        print("pushfront")
        self.d.appendleft(val)
        print(self.d)
        
    def pushMiddle(self, val: int) -> None:
        if len(self.d) % 2 != 0:
            middle = ((len(self.d) + 1) // 2) - 1
            self.d.insert(middle, val)
        elif len(self.d) % 2 == 0:
            middle = ((len(self.d) + 1) // 2)
            self.d.insert(middle, val)

    def pushBack(self, val: int) -> None:
        print("pushback")
        self.d.append(val)
        print(self.d)
        
    def popFront(self) -> int:
        if not self.d:
            return -1
        return self.d.popleft()

    def popMiddle(self) -> int:
        print("popmiddle")
        print(self.d)
        if not self.d:
            return -1
        if len(self.d) % 2 == 0:
            middle = (len(self.d) // 2) - 1
            ans = self.d[middle]
            self.d.remove(self.d[middle])
            return ans
        elif len(self.d) % 2 != 0:
            middle = len(self.d) // 2
            print(middle)
            ans = self.d[middle]
            print(middle, self.d[middle])
            del self.d[middle]
            #self.d.remove(self.d[middle])
            return ans 
        
    def popBack(self) -> int:
        if not self.d:
            return -1
        return self.d.pop()
