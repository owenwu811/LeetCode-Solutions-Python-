
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


#5/19/24 refresher:

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

#5/26/24 review:

#https://algo.monster/liteproblems/295

#To find the median efficiently, we need a data structure that allows quick access to the middle elements.
#Utilizing two heaps is an elegant solution: a max heap to store the smaller half of the numbers and a min heap to store the larger half. 
#This way, the largest number in the smaller half or the smallest number in the larger half can easily give us the median.

#In Python, the default heapq module provides a min heap implementation. To get a max heap behavior, we insert negatives of the numbers into a heap.

#By balancing the heaps so that their size differs by at most one, we ensure that we either have a single middle element when the combined size is odd (this will be at the top of the larger heap), or two middle elements when the combined size is even (the top of each heap).

#The addNum method works by adding a new number to the max heap (smaller half) first, by pushing its negative value. We then pop the top value from the max heap and push it to the min heap (larger half) to maintain the order and balance. If the larger half has more than one extra element compared to the smaller half, we move the top element from the larger half to the smaller half.

#findMedian checks the current size of the heaps. If the heaps are of the same size, the median is the average of the top values of both heaps. If the sizes differ, the median is the top element of the larger heap.

class MedianFinder:
    def __init__(self):
        self.a, self.b = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.a, -1 * num)
        if self.a and self.b and (-1 * self.a[0]) > self.b[0]:
            val = heapq.heappop(self.a)
            heapq.heappush(self.b, -val)
        if len(self.a) > len(self.b):
            val = heapq.heappop(self.a)
            heapq.heappush(self.b, -val)
        elif len(self.b) > len(self.a):
            val = heapq.heappop(self.b)
            heapq.heappush(self.a, -val)

    def findMedian(self) -> float:
        if len(self.a) > len(self.b):
            return -1 * self.a[0]
        elif len(self.b) > len(self.a): #If h2 has more elements than h1, the median is just the top element of h2 (the smallest number in the larger half).
            return self.b[0]
        #If h1 and h2 have the same number of elements, the median is the average of the top element of h1 (the largest number in the smaller half, remember h1 is storing negatives) and the top element of h2 (the actual smallest number in the larger half).
        return ((-1 * self.a[0]) + self.b[0]) / 2

#6/2/24 refresher:

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
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
        return ((-1 * self.small[0]) + self.large[0]) / 2

#7/1/24 review (missed 5 days ago):

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
        elif len(self.large) > len(self.small):
            return self.large[0]
        return ((-1 * self.small[0]) + (self.large[0])) / 2
        
