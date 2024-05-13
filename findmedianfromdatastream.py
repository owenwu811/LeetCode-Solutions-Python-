
#The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

#For example, for arr = [2,3,4], the median is 3.
#For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#Implement the MedianFinder class:

#MedianFinder() initializes the MedianFinder object.
#void addNum(int num) adds the integer num from the data stream to the data structure.
#double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


#python3 solution:

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0] 
        return (-1 * self.small[0] + self.large[0]) / 2


#practice again:

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) 
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2



#5/9/24:

class MedianFinder(object):

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1: #if we get rid of the + 1 and just do len(self.small) > len(self.large), it works too!
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1: #if we get rid of the + 1 and just do len(self.large) > len(self.small), it works too!
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


#5/10/24 refresher:

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) #negation to make this a min heap
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


#5/12/24 refresher:

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.small) > len(self.large):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
       
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


#5/13/24 refresher:

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.small) > len(self.large):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2

