#362
#medium


#Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

#Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

#Implement the HitCounter class:

#HitCounter() Initializes the object of the hit counter system.
#void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
#int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).



#my own solution using python3:

class HitCounter:

    def __init__(self):
        self.d = dict()
    
    def hit(self, timestamp: int) -> None:
        if timestamp not in self.d:
            self.d[timestamp] = 0
        self.d[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        print(self.d)
        self.d = dict(sorted(self.d.items(), key=lambda x: x[0]))
        print(self.d)
        starting = timestamp - 300
        ending = timestamp
        res = 0
        for k in self.d:
            if k > starting and k <= ending:
                res += (self.d[k])
        return res
