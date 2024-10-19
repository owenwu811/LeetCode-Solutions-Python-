#1429
#medium


#You have a queue of integers, you need to retrieve the first unique integer in the queue.

#Implement the FirstUnique class:

#FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
#int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
#void add(int value) insert value to the queue.




#my own solution using python3:

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = deque(nums)
        self.c = Counter(self.d)
        print(self.c)
        

    def showFirstUnique(self) -> int:
        for i, n in self.c.items():
            if n == 1:
                return i
        return -1
        

    def add(self, value: int) -> None:
        self.c[value] += 1
