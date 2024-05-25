




#python3 solution:

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1 #self.freq = {5: 3, 7: 2, 4: 1}
        #will always be true on 1st turn because self.maxFreq starts at 0, and we already know that self.freq[val] is atleast 1
        if self.freq[val] > self.maxFreq: #this line is about finding the most frequent value
            self.maxFreq = self.freq[val] #sets self.maxFreq = 1 in 1st iteration
        #always append whether above if condition was True or not 
        self.groups[self.freq[val]].append(val) #self.groups = {1: [5, 7, 4], 2: [5, 7], 3: [5]}
    #pop most frequent element from stack and returns the most frequent element. if tie for most frequent element, element closest to stack's top is removed and returned
    def pop(self) -> int:
        #In Python, lists maintain the order of elements as they were added
        #the reason why this pops the most recent element is because append is in order while pop is from the end, so we pop the element that was last (most recently) added in LIFO order
        first = self.groups[self.maxFreq].pop() 
        self.freq[first] -= 1 #we decrement the value we just popped, so 3: [5] becomes 3: [], so we have to do self.freq[5] -= 1 to go from {5: 3} to {5: 2}
        if not self.groups[self.maxFreq]: #since 3: [] is an empty bracket, we don't have any numbers with frequency of 3, so that can't be a maxfrequency anymore, so decrement frequency by one from 3 to 2 because if a number appeared 3 times, it had to have appeared twice and once as well
            self.maxFreq -= 1
        #always return first whether above if condition was True or not 
        return first

#5/25/24 refresher:

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
        self.groups[self.freq[val]].append(val)
        

    def pop(self) -> int:
        first = self.groups[self.maxFreq].pop()
        self.freq[first] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return first
        
