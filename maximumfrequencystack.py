




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

#5/25/24 evening review:

class FreqStack:
    def __init__(self):
        self.maxFreq = 0
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)

        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
        self.groups[self.freq[val]].append(val)

        

    def pop(self) -> int:
        res = self.groups[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return res


#5/26/24 review:

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0


    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
        #{freq: [values]}
        self.groups[self.freq[val]].append(val)


    
    def pop(self) -> int:
        first = self.groups[self.maxFreq].pop() 
        self.freq[first] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return first



#practice again:

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
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

#5/29/24 review:

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.maxFreq = 0
        self.mylist = defaultdict(list)
        

    def push(self, val: int) -> None:
        self.freq[val] += 1 #{5: 1}
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
        #[3: [5, 7]]
        self.mylist[self.freq[val]].append(val) #self.mylist[self.freq[val]].append(val) not self.mylist[self.maxFreq].append(val) because we need to have all frequencies as keys!


    def pop(self) -> int:
        first = self.mylist[self.maxFreq].pop() 
        self.freq[first] -= 1
        if not self.mylist[self.maxFreq]:
            self.maxFreq -= 1
        return first

#6/14/24 review:

class FreqStack:

    def __init__(self):
        self.d = defaultdict(int)
        self.lst = defaultdict(list)
        self.maxfreq = 0
        

    def push(self, val: int) -> None:
        self.d[val] += 1 
        if self.d[val] > self.maxfreq:
            self.maxfreq = self.d[val]
        self.lst[self.d[val]].append(val)
        

    def pop(self) -> int:
        first = self.lst[self.maxfreq].pop()
        self.d[first] -= 1 #1: 2: 3:[3, 5] - if 5 appeared in 3 bucket, but we popped, then 5 now appears in 2 bucket aka 5: 2 now instead of 5: 3
        if not self.lst[self.maxfreq]:
            self.maxfreq -= 1
        return first

#6/15/24 review:

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxfreq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxfreq:
            self.maxfreq = self.freq[val]
        self.groups[self.freq[val]].append(val)
        

    def pop(self) -> int:
        first = self.groups[self.maxfreq].pop()
        self.freq[first] -= 1
        if not self.groups[self.maxfreq]:
            self.maxfreq -= 1
        return first
