#Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

#Implement the TimeMap class:

#TimeMap() Initializes the object of the data structure.
#void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


#python3 solution:

class TimeMap:
    def __init__(self):
        #self.dict = dict() works too here - so {} and dict() all work for initializing an empty dictionary, but set only does set() for an empty set even though sets are printed with {} around them to the console
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


#python3 solution with notes:

class TimeMap:
    def __init__(self):
        self.cache = {} #key = string, value = [list of [value, timestamp]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        #if our current dictionary looks like: "foo": [bar, 1], and our current operation is a set operation with "foo": [bar2, 4] associated with the set operation, we would add this to our dictionary
        #and get "foo": [[bar, 1], [bar2, 4]] - as the state of our dictionary - when we add to this list, we will always add to the end of this list, which is also 0(1) time
        #set will be a 0(1) operation because finding the key means we are using a hashmap
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([value, timestamp]) #to the list, append to the end of the list the pair of values [value, timestamp] - adding to rear of list "foo": [[bar, 1], [bar2, 4]]
       
    def get(self, key: str, timestamp: int) -> str:
        #if we don't find an exact match in our key value store - {"foo": [bar, 1]} - to our timestamp, then return the closest value to timestamp that's closest to timestamp, so if timestamp was 3 for example, we would return the closest to 3 but less than 3, so if {"foo": [bar, 1]} is the only one in our dictionary, we would return 1. if we had {"foo": [bar, 4]} in our dictionary, but our timestamp was still 3, we wouldn't return 4 because 4 is greater than 3
        #if we had "foo" and ["bar", 1] and ["bar", 2], we would return 2 because 2 is closest to our timestamp value of 3
        #binary search algorithm runs in 0(log(n)) time, which is better than 0(n) time, which would 
        #require our dictionary to be sorted - "foo": [[bar, 1], [bar2, 4]], so we sort by the timestamp since we 
        #if we sorted, the tc would be n (log (n))
        #since we know that the timestamps of our set are strictly increasing, as denoted by the problem
        #so if we just add to the rear of the list everytime we set a value - "foo": [[bar, 1], [bar2, 4]] - then we know the list is going to be sorted by TIMESTAMP BY DEFAULT, so since THE TIMESTAMPS ARE ALREADY SORTED, WE DON'T HAVE TO SORT THE TIMESTAMPS AGAIN AND CAN JUST RUN A BINARY SEARCH
        #in a real interview, you would ask that, everytime we set a value, is the timestamp going to be in ascending order 
        #BECAUSE TIME USUALLY FLOWS IN ON DIRECTION, IT MAKES SENSE THAT THESE LISTS THAT WE ARE ADDING WOULD ALREADY BE IN SORTED ORDER IN TERMS OF TIMESTAMPS - "foo": [[bar, 1], [bar2, 4]]
        #if the get ["foo", 4] request's value was already in our dictionary, you would just return bar2 - "foo": [[bar, 1], [bar2, 4]]
        #if another request is - get ["foo", 5], and 5 isn't in our dictionary - "foo": [[bar, 1], [bar2, 4]] - then 4 is the closest that is smaller than 5, so you would return bar2 for the value of that get request input again 
        res = "" #if the key dosen't exist in the dictionary itself, then we return an empty string
        correspondence = self.cache.get(key, []) #if it finds a match, it will return the corresponding [value, timstamp] list. if no match is found with the key in our dictionary, then it will return [] by default
        #print(correspondence)
        l, r = 0, len(correspondence) - 1 #correspondence is an array here!!! since we corresponded to [value, timestamp]
        while l <= r:
            mid = (l + r) // 2 #without // double slashes in python does decimal division instead of integer division
            #the 2nd value in the list is the timestamp hence index 1
            if correspondence[mid][1] <= timestamp: #valid value if equal to or less than timestamp - [value, timstamp] - index 1 is
                #correspondence[mid][1] is a valid value and the closest - so basically mid 1 maps to mid 0 because correspondence[mid][1] is the 4 in "foo": [[bar, 1], [bar2, 4]] while correspondence[mid][0] is the bar2 in "foo": [[bar, 1], [bar2, 4]]
                res = correspondence[mid][0] #we set to mid 0 because if "foo": [[bar, 1], [bar2, 4]] and request is 5, then we assume that 4 is less than but closest to 5 and return "bar2"
                l = mid + 1
            else: #if timestamp in [value, timstamp] is greater than our timestamp request, then that is not allowed
                #invalid value since bigger than timestamp request, so we CANNOT ASSIGN IT TO THE RESULT
                r = mid - 1
        return res

        #if correspondence[mid][1] <= timestamp: - could be more optimized because correspondence[mid][1] even if we find exact match == to the timestamp, the binary search still keeps going
                
        

#practice run 2:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
    
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        #key is already a key in our mydict dictionary:
        self.mydict[key].append([value, timestamp])
        #we know that above will already be appended in order of timestamps because time always flows in one direction, so we don't have to manually sort, so we can just use binary search to get the value below
      
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #we are retriving the corresponding [value, timestamp] associated with the given key and setting this [value, timestamp] list to the variable called rightlist. If the key we are trying to retrieve the value of dosen't exist in the dictionary, then we can just set it to an empty list by default
        rightlist = self.mydict.get(key, [])
        l, r = 0, len(rightlist) - 1
        while l <= r:
            #we may have a dictionary pair like: {"foo": [bar, 1], [bar2, 4]}, so we want to retrieve the appropriate 0th index of one of the lists depending on how close it's corresponding timestamp is to our timestamp request number without exceeding our timestamp request number
            mid = (l + r) // 2
            #if out timestampvalue is 5, and 4 from [bar2, 4] is less than 5 but the closest timestamp to 5 that exists in any of the sublists in our dictionary, then we can return 4
            if rightlist[mid][1] <= timestamp:
                res = rightlist[mid][0]
                l = mid + 1
            else: #the 1st index value being larger than the timstamp request is not acceptable, so we narrow the search space to the left half of our lists because we know timestamps are sorted in ascending order
                r = mid - 1
        return res


#2/10/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
       
    
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        #because we know that the timstamps are already sorted as time goes in one direction and we are adding to the rear of the list, we can just run a binary search
        self.mydict[key].append([value, timestamp])
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        correspondence = self.mydict.get(key, [])
        l, r = 0, len(correspondence) - 1
        while l <= r:
            mid = (l + r) // 2
            if correspondence[mid][1] <= timestamp:
                res = correspondence[mid][0]
                l = mid + 1
            else: #the current timestamp in the list has exceeded the value of timestamp, so it's not a valid corresponding result to the same index 0
                r = mid - 1
        return res
     

#2/10/24 practice again:

class TimeMap:

    def __init__(self):
        self.cachd = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cachd:
            self.cachd[key] = []
        self.cachd[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #gives us [value, timestamp]
        c = self.cachd.get(key, [])
        l, r = 0, len(c) - 1
        while l <= r:
            #since we know timestamps were already inserted in order, we can just search for the one we want and try to get the closest to it that is less than it
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#2/11/24:

class TimeMap:

    def __init__(self):
        self.cachd = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cachd:
            self.cachd[key] = []
        self.cachd[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        pair = self.cachd.get(key, [])
        l, r = 0, len(pair) - 1
        while l <= r:
            mid = (l + r) // 2
            if pair[mid][1] <= timestamp:
                res = pair[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


#2/12/24:

class TimeMap:
    def __init__(self):
        #key, value data structure is a dead giveaway that we need a dictionary
        self.cachd = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        #stores the key key with value value at given timestamp indicates that value and timestamp are correlated because key and value are on left and right (seperate) sides of dictionary 
        if key not in self.cachd:
            self.cachd[key] = []
        self.cachd[key].append([value, timestamp])

       
       
    def get(self, key: str, timestamp: int) -> str:
        #timestampprev is likely the current timestamp page request
        res = ""
        #get the value - [value, timestamp] list associated with key if key exists in self.cachd. If not, then correspondence variable equals an empty list by default. 
        correspondence = self.cachd.get(key, [])
        #we can run a binary search without sorting since binary search requires timestamp to be sorted, which they already are
        l, r = 0, len(correspondence) - 1
        #remember - we want less than or equals to timestamp page request, not bigger than
        while l <= r:
            #again, python uses // to get whole numbers like 2 instead of decimal numbers like 2.5, which is given from /
            mid = (l + r) // 2
            #correspondence = {"foo":["bar2", 4]} - 4
            if correspondence[mid][1] <= timestamp:
                #"bar2"
                res = correspondence[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#2/13/24:

class TimeMap:

    def __init__(self):
        self.cachd = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cachd:
            #we know that the [value, timestamp] are correlated as a list, so do add an empty list even if the key dosen't exist in the dict yet
            self.cachd[key] = []
        #the timestamps are being added in order already, so we can just run a binary search without sorting again
        self.cachd[key].append([value, timestamp])
       
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #we want the largest but closest to without exceeding timestamp in our list as the timestamp given in the request
        correspondence = self.cachd.get(key, [])
        l, r = 0, len(correspondence) - 1
        while l <= r:
            mid = (l + r) // 2
            #closest to timestamp_prev means can be equal to
            if correspondence[mid][1] <= timestamp:
                res = correspondence[mid][0]
                l = mid + 1
            else: # we can't exceed the request
                r = mid - 1
        return res

#2/14/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        #will already be in sorted order of timestamps, so we can just run a binary search in get method without sorting again. Time flows in one direction. 
        self.mydict[key].append([value, timestamp])
       
       
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #we are getting the [value, timestamp] associated with the given key
        correspondence = self.mydict.get(key, [])
        #binary search
        l, r = 0, len(correspondence) - 1
        while l <= r:
            mid = (l + r) // 2
            #ideally, we want to get equal and an exact match, but if not, then we want the closest timestamp in our dictionary as our request while still being less than
            if correspondence[mid][1] <= timestamp:
                #[bar2, 1] - bar2 - let's say our request was 1
                res = correspondence[mid][0]
                l = mid + 1
            else: #too big, but still sorted order, so move right to mid - 1
                r = mid - 1
        return res

#2/16/24:

class TimeMap:
    def __init__(self):
       self.mydict = dict()        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
      
       
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        correspondence = self.mydict.get(key, []) #[value, timestamp]
        l, r = 0, len(correspondence) - 1
        while l <= r:
            mid = (l + r) // 2
            if correspondence[mid][1] <= timestamp:
                res = correspondence[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#2/20/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([timestamp, value])
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        correspondence = self.mydict.get(key, [])
        #since the keys are already in sorted order, we can jut run a binary search without sorting again
        l, r = 0, len(correspondence) - 1
        while l <= r:
            mid = (l + r) // 2
            #binary search only works if the values are in sorted order 
            if correspondence[mid][0] <= timestamp:
                res = correspondence[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

#3/2/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
        
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        correspondence = self.mydict.get(key, []) #[value, timestamp] - returns the value means we compare timestamp and return corresponding value
        l, r = 0, len(correspondence) - 1 
        while l <= r:
            mid = (l + r) // 2
            if correspondence[mid][1] <= timestamp:
                res = correspondence[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


#3/8/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, []) #corresponds to a [value, timestamp]
        l, r = 0, len(c) - 1
        while l <= r:
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#3/9/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict() 
        
        
    def set(self, key: str, value: str, timestamp: int) -> None: #value and timestamp are a list that is the value of the dictionary
        if key not in self.mydict:
            self.mydict[key] = [] #empty list if the key dosen't exist in mydict
        self.mydict[key].append([value, timestamp]) #this is going to add the list in order since time only goes in one direction and because we can now do a binary search because the timestamps are already sorted

       
       
       
    def get(self, key: str, timestamp: int) -> str:
        #returning a value means that we return a string that is the 0th index correspondant to the timestamp, which is the 1st index
        res = ""
        c = self.mydict.get(key, []) #retrieve the value associated with that key, or give an empty list, so it shoudl correspond to [value, timestamp]
        l, r = 0, len(c) - 1
        while l <= r: #we can run a binary search
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1 #we want to find the closest possible but not bigger than
            else:
                r = mid - 1 #too big, so we have to go back since the array is sorted in order by timestamps 
        return res


#3/11/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp]) #already sorted in order of time by timestamp
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, [])
        l, r = 0, len(c) - 1 #can run binary search since already sorted
        while l <= r:
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#3/17/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()

        
        
    def set(self, key: str, value: str, timestamp: int) -> None: #value and timestamp are a list that is the value of the dictionary
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, []) #list of lists value side [value, timestamp] - retrieve 
        l, r = 0, len(c) - 1
        while l <= r: # run binary search since already in sorted order
            mid = (l + r) // 2 #decimal vs int - 2 vs 2.5
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#3/21/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, [])
        l, r = 0, len(c) - 1
        while l <= r:
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


#3/23/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
        
        
    def set(self, key: str, value: str, timestamp: int) -> None: 
        #value and timestamp are a list that is the value of the dictionary
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
   
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, [])
        l, r = 0, len(c) - 1
        while l <= r: #binary search works because we are already sorted in ascending order
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1 
            else:
                r = mid - 1
        return res

#4/3/24 practice:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
    
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, []) #[value, timestamp]
        l, r = 0, len(c) - 1
        while l <= r:
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
#4/8/24:

class TimeMap:
    def __init__(self):
        self.mydict = dict()
        
        
    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key not in self.mydict:
            self.mydict[key] = []
        self.mydict[key].append([value, timestamp])
        
   
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        c = self.mydict.get(key, [])
        l, r = 0, len(c) - 1
        while l <= r:
            mid = (l + r) // 2
            if c[mid][1] <= timestamp:
                res = c[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
       

#5/1/24 refresher:

#d = {"foo": [['bar', 1], ['baz', 2]]
#need = [['bar', 1], ['baz', 2]]
#l, r = 0, 1 because ['bar', 1] = index 0 and ['baz', 2] = index 1
#mid, if 0, = ['bar', 1], so mid represents each sublist itself
#need[mid][1] = 1 from the 1st index in mid

class TimeMap:
    def __init__(self):
        self.d = dict()
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #already in sorted order, so we can just perform binary search
        need = self.d.get(key, []) #gets [value, timestamp] > timestamp
        l, r = 0, len(need) - 1
        while l <= r:
            mid = (l + r) // 2
            if need[mid][1] <= timestamp:
                res = need[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

#THIS IS WHY YOU NEED self.d[key] = [], which yeilds in [['bar', 1]], while just doing self.d[key] = [value, timestamp] results in ['bar', 1], which is wrong!
#b = [['bar', 1]]
#print(len(b)) > 1
#c = ['bar', 1]
#print(len(c)) > 2

#wrong choice with - self.d[key] = [value, timestamp] results in a = ['bar', 1] causing l, r = 0, 1, so a[mid][1] dosen't exist and results in str vs. int comparison error!
#correct choice with self.d[key] = [] results in a = [['bar', 1]] causing l, r = 0, 0, so a[mid][1] does exist!

#note the l, r = 0, 1 vs. 0, 0 correct version difference dosen't matter because (0 + 1) // 2 still yeilds 0, but you can't have a[mid][1] for ['bar', 1] because it's a single list!
        
