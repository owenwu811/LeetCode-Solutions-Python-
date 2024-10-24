
#1756
#medium

#Design a queue-like data structure that moves the most recently used element to the end of the queue.

#Implement the MRUQueue class:

#MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
#int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.

#my own solution using python3:

class MRUQueue:

    def __init__(self, n: int):
        self.d = deque()
        for i in range(1, n + 1):
            self.d.append(i)

    def fetch(self, k: int) -> int:
        if k <= len(self.d):
            target = self.d[k - 1]
            self.d.remove(self.d[k - 1])
            self.d.append(target)
            return target
