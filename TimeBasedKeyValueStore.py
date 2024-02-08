#Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

#Implement the TimeMap class:

#TimeMap() Initializes the object of the data structure.
#void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


#python3 solution:

class TimeMap:
    def __init__(self):
        self.dict = {}
    
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        #adding lists to the rear of lists 
        self.dict[key].append([value, timestamp])
        
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dict.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else: #too big, so cannot set the result
                r = mid - 1
        return res
