
#1845
#medium


#Design a system that manages the reservation state of n seats that are numbered from 1 to n.

#Implement the SeatManager class:

#SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
#int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
#void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.



#my own solution using python3:

class SeatManager:

    def __init__(self, n: int):
        self.myheap = []
        for i in range(1, n + 1):
            heapq.heappush(self.myheap, i)
        print(self.myheap)
        

    def reserve(self) -> int:
        a = heapq.heappop(self.myheap)
        return a
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.myheap, seatNumber)
