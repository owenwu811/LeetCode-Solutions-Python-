
#1286
#medium

#Design the CombinationIterator class:

#CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
#next() Returns the next combination of length combinationLength in lexicographical order.
#hasNext() Returns true if and only if there exists a next combination.
 

#Example 1:

#Input
#["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
#[["abc", 2], [], [], [], [], [], []]
#Output
#[null, "ab", true, "ac", true, "bc", false]

#Explanation
#CombinationIterator itr = new CombinationIterator("abc", 2);
#itr.next();    // return "ab"
#itr.hasNext(); // return True
#itr.next();    // return "ac"
#itr.hasNext(); // return True
#itr.next();    // return "bc"
#itr.hasNext(); // return False


#my own solution using python3:

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        #print(self.s)
        self.c = combinationLength
        self.comb = deque()
        for a in combinations(self.s, self.c):
            #print(a)
            self.comb.append("".join(a))

    def next(self) -> str:
        if self.comb:
            return self.comb.popleft()

        

    def hasNext(self) -> bool:
        return len(self.comb) > 0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
