
#281
#medium

#Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

#Implement the ZigzagIterator class:

#ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
#boolean hasNext() returns true if the iterator still has elements, and false otherwise.
#int next() returns the current element of the iterator and moves the iterator to the next element.
 

#Example 1:

#Input: v1 = [1,2], v2 = [3,4,5,6]
#Output: [1,3,2,4,5,6]
#Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].


#my own solution using python3:

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        print(v1, v2)
        self.first, self.second = deque(v1), deque(v2)
        self.turn = 0

    def next(self) -> int:
        if self.first and self.second:
            if self.turn % 2 == 0:
                self.turn += 1
                return self.first.popleft()
            else:
                self.turn += 1
                return self.second.popleft()
        elif self.first and not self.second:
            return self.first.popleft() 
        elif self.second and not self.first:
            return self.second.popleft()
        

    def hasNext(self) -> bool:
        return self.first or self.second
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
