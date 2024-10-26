
#170
easy

#Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

#Implement the TwoSum class:

#TwoSum() Initializes the TwoSum object, with an empty array initially.
#void add(int number) Adds number to the data structure.
#boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.


#my own solution using python3:

class TwoSum:
    def __init__(self):
        self.d = []
        self.map = defaultdict(int)

    def add(self, number: int) -> None:
        self.d.append(number)
        self.map[number] += 1

    def find(self, value: int) -> bool:
        self.d.sort()
        l, r = 0, len(self.d) - 1
        while l < r:
            if self.d[l] + self.d[r] == value:
                return True
            elif self.d[l] + self.d[r] > value:
                r -= 1
            else:
                l += 1
        return False
