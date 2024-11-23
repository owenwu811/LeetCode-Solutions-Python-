

#251
#medium

#Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

#Implement the Vector2D class:

#Vector2D(int[][] vec) initializes the object with the 2D vector vec.
#next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
#hasNext() returns true if there are still some elements in the vector, and false otherwise.
 

#Example 1:

#Input
#["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
#[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
#Output
#[null, 1, 2, 3, true, true, 4, false]

#Explanation
#Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
#vector2D.next();    // return 1
#vector2D.next();    // return 2
#vector2D.next();    // return 3
#vector2D.hasNext(); // return True
#vector2D.hasNext(); // return True
#vector2D.next();    // return 4
#vector2D.hasNext(); // return False

#my own solution using python3:

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = vec
        self.new = deque()
        for i in range(len(self.v)):
            for j in range(len(self.v[i])):
                self.new.append(self.v[i][j])

    def next(self) -> int:
        if self.new: 
            return self.new.popleft()

    def hasNext(self) -> bool:
        return len(self.new) > 0
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
