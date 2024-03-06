
#Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

#Implement the LRUCache class:

#LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#int get(int key) Return the value of the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#The functions get and put must each run in O(1) average time complexity.

 

#Example 1:

#Input
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]





#python3 solution:



class LRUCache:
    def __init__(self, capacity: int):
        #ordereddict maintains the order of items based on order of insertion into the dictionary
        self.cache = OrderedDict()
        #max number of elements the cache can hold
        self.cap = capacity
        self.pagefaultcount = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: #although this is get, we still have to pop and reinsert in get to update the order of items in the cache to reflect the most recently accessed item!!!!!
            #cache = [1, 2, 3], and current paging request = 2, so we don't have to go to hard disk and fetch it from there. Instead, we will just fetch page 2 from the cache, which will save us time. Since 2 was already in our cache, it IS NOT CONSIDERED A PAGING FAULT. 
            res = self.cache[key]
            #delete key, value pair and update order of default dict
            self.cache.pop(key)
            #reinsert key value pair at end of ordereddict
            self.cache[key] = res
            return res

    def put(self, key: int, value: int) -> None:
        #our current page request of 3 is already in our cache since cache = [3, 4, 1]. we don't increment the paging fault count, and we instead move 3 from the start to the end, and everything slides to the left - [4, 1, 3]
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else: #our current paging fault request is 4 in 1234, and our cache is [1, 2, 3], but we have reached our capacity 
            if self.pagefaultcount == self.cap:
                #the replacement policy is deleting from beginning befor adding to rear if our current paging request is not already in the cache. For example, let's say our cache = [1, 2, 3], and our paging request is 4, and we want the new paging request of 4 to be added to the rear. The algorithm says we want to remove the least recently used page, so since our requests were in time order from 1 2 3 4, so the oldest request was 1, so 1 is the least recently used in our cache of [1, 2, 3], so we remove 1, and we add 4, so our cache = [2, 3, 4]. Our final goal is to find the number of page faults 
                leastrecentlyusedkey = next(iter(self.cache))
                self.cache.pop(leastrecentlyusedkey)
                self.cache[key] = value
            else:
                #our paging fault count is not in our cache, and the cache HAS NOT reached it's max capacity, so just add the paging request key value pair to end and increment paging fault count. REMEMBER: when the current paging request is not in our cache and we HAVE NOT REACHED CAPACITY YET, this is a paging fault. so when a page is requested by the user, and it's not in our cache, this is a paging fault 
                self.cache[key] = value
                self.pagefaultcount += 1







#practice run




class LRUCache:
    def __init__(self, capacity: int):
        self.givencapacity = capacity
        self.pagefaultcount = 0
        self.cachedict = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.cachedict:
            return -1
        else:
            result = self.cachedict[key]
            self.cachedict.pop(key)
            self.cachedict[key] = result
            return result
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cachedict:
            self.cachedict.pop(key)
            self.cachedict[key] = value
        else:
            if self.pagefaultcount == self.givencapacity:
                leastrecentlyused = next(iter(self.cachedict))
                self.cachedict.pop(leastrecentlyused)
                self.cachedict[key] = value

            else: 
                self.cachedict[key] = value
                self.pagefaultcount += 1



#1/29/24 practice:

class LRUCache:
    def __init__(self, capacity: int):
        #given to us as an integer
        self.cap = capacity
        self.cd = OrderedDict()
        self.pagefaultcount = 0

    def get(self, key: int) -> int:
        if key not in self.cd:
            return -1
        else: #the idea is that we don't have duplicate paging requests in our cache, and we move the current pagging request 3 that is already in our cache to the end by deleting and reinserting 
            res = self.cd[key]
            self.cd.pop(key)
            self.cd[key] = res
            return res
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cd: #if our page request is already in our cache, we remove the one already in the cache and add the current page request (same as just removed) to the end - no pagefaultcount because it was in the cache
            self.cd.pop(key)
            self.cd[key] = value
        else: #if our current page request isn't in our cache, but capacity is full, we don't increase page fault count
            if self.cap == self.pagefaultcount:
                lru = next(iter(self.cd))
                self.cd.pop(lru)
                self.cd[key] = value
            else:
                self.cd[key] = value
                self.pagefaultcount += 1


#another practice run:

class LRUCache:
    def __init__(self, capacity: int):
        #capacity is an integer that is given to us that represents the limit to the size of the cache aka how many items the cache can store
        self.cap = capacity
        #cache will be a dictionary with key, value pairs
        self.cached = OrderedDict()
        #we want to find the number of paging faults aka when the current paging request number does not exist as a key in our cached ordereddict
        self.pagefaultcount = 0
       

    def get(self, key: int) -> int:
        if key not in self.cached:
            return -1
        else: #key (number of our current paging request)exists as a key in cached, so we want to remove it from it's current position and insert the key at the end since we don't want duplicate keys in our cachedict
            res = self.cached[key]
            self.cached.pop(key)
            self.cached[key] = res
            #return the value of the key if it exists
            return res
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cached:
            #again, since our current paging request number is already in our cached, this will not be a paging fault, but we do want to delete it and reinsert at the rear
            self.cached.pop(key)
            self.cached[key] = value
        else: #our current paging request number is not in our current cached dictionary as a key, so if our capacity is equal to the number of page fault counts, we want to pop and reinsert into the rear without incrementing pagefaultcount
            if self.pagefaultcount == self.cap:
                lru = next(iter(self.cached))
                self.cached.pop(lru)
                self.cached[key] = value
            else: #if our current paging request number is not in our current cached dictionary as a key and our current capacity is not full, then we do have a page fault count, and then insert the current page fault count at the rear of our dictionary
                self.cached[key] = value
                self.pagefaultcount += 1


#1/30/24 practice:

class LRUCache:
    def __init__(self, capacity: int):
        #int that is given to us as capacity is positive as in the constraints
        self.cap = capacity
        self.pagefaultcount = 0
        self.cache = OrderedDict()
       
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            result = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = result
            return result
     
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #no paging fault
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if self.cap == self.pagefaultcount:
                #we are full, so we need to replace by deleting the least recently used cache and add our current page request to the end as a replacement
                lru = next(iter(self.cache))
                self.cache.pop(lru)
                self.cache[key] = value
            else: #not full and not in cache, so do increment page fault count
                self.cache[key] = value
                self.pagefaultcount += 1

#1/31/24 practice:

class LRUCache:
    def __init__(self, capacity: int):
        #positive integer that is given to us
        self.cap = capacity
        self.cachedict = OrderedDict()
        #pagefault count is when we are not at max capacity and our current paging request is not in our cache
        self.pagefaultcount = 0
        

    def get(self, key: int) -> int:
        if key not in self.cachedict:
            return -1
        else:
            result = self.cachedict[key]
            self.cachedict.pop(key)
            self.cachedict[key] = result
            return result

       
     
    def put(self, key: int, value: int) -> None:
        #no page fault count since our paging request (key) exists in our cachedict
        if key in self.cachedict:
            #move it to the most recently used
            self.cachedict.pop(key)
            #inserting at rear
            self.cachedict[key] = value
        else:
            if self.cap == self.pagefaultcount:
                lru = next(iter(self.cachedict))
                self.cachedict.pop(lru)
                self.cachedict[key] = value
            else: #not in it and not at capacity
                self.cachedict[key] = value
                self.pagefaultcount += 1


#2/1/24 practice:

class LRUCache:

    def __init__(self, capacity: int):
        #positive integer capacity is given to us
        self.cap = capacity
        #retains the order in which key, value pairs were inserted
        self.cache = OrderedDict()
        self.pagefaultcount = 0
       
        
       
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            result = self.cache[key]
            self.cache.pop(key) #By uncommenting the two lines, you would essentially move the accessed key-value pair to the end of the OrderedDict, indicating that it was the most recently used since the GET METHOD also focuses on updating the order to reflect recent usage.  In a traditional LRU cache, when you access an existing key using the get method, it is a common expectation that the accessed key-value pair should be moved to the most recently used position (i.e., the end of the cache order).
            #While the problem description may not explicitly mention this behavior, it's a reasonable assumption to make
            self.cache[key] = result
            return result
        
       
     
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else: #if key not in self.cache, and we can't store another pagefault count, we define replacement policy
            if self.cap == self.pagefaultcount:
                lru = next(iter(self.cache))
                self.cache.pop(lru)
                self.cache[key] = value
            else:
                self.cache[key] = value
                self.pagefaultcount += 1


#important notes: the get method focuses on retrieving a value and updating the order to reflect recent usage, while the put method has the additional responsibility of managing the cache capacity, inserting or updating key-value pairs, and ensuring that the usage order is updated for existing keys
#important notes: so the get method: retrives values, updates usage order. the put method: inserts or updates key value pairs, handles overflow capacity, and updates usage order (same as with get)


#2/2/24 practice:

class LRUCache:

    def __init__(self, capacity: int):
        #positive integer capacity is given to us
        self.cap = capacity
        self.cache = OrderedDict()
        #occurs when we want to put a key into the dict that is not already there and we have NOT reached full capacity yet
        self.pagefaultcount = 0
       
        
       
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: #key exists in self.cache
            #we still need to remove it and readd to the rear
            result = self.cache[key]
            self.cache.pop(key)
            #we are adding the key, value pair to the end of the dictionary
            self.cache[key] = result
            return result

        
        
       
     
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #move the k, v pair to the rear
            self.cache.pop(key)
            self.cache[key] = value
        else: #our key is not in our cache, and we HAVE reached full capacity, so define the replacement policy by popping from the left and adding the new k, v pair to the end
            if self.cap == self.pagefaultcount:
                lrutoremove = next(iter(self.cache))
                self.cache.pop(lrutoremove)
                self.cache[key] = value
            else: #key not in our cache and haven't reached capacity, so we need to increase page fault count
                self.cache[key] = value
                self.pagefaultcount += 1


#2/4/24 my own solution refresher:

class LRUCache:

    def __init__(self, capacity: int):
        #capacity of the cache we are given as a positive integer
        self.cap = capacity
        #we want to keep track of the order in which we insert key, value pairs (items), so we use ordereddict - deque works too, but the problem specifically tells us to check if the key exists in the cache, so OrderedDict is easier to implement here
        self.cache = OrderedDict()
        #will be the count of when our cache isn't at full capacity, and our current page request is a number that isn't a number in our cache as a key to the dictionary, and we are trying to insert into our cache
        self.pagefaultcount = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            #still have to move to rear for get requests
            result = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = result
            return result
       
     
    def put(self, key: int, value: int) -> None:
        if key in self.cache: #and we are not at capacity yet since not explicitly stated
            self.cache.pop(key)
            self.cache[key] = value
        else:
            #len(self.cache) works too instead of self.pagefaultcount because pagefaultcount happened everytime you put a value into your dict that wasn't already there!
            if len(self.cache) == self.cap:
                lru = next(iter(self.cache))
                self.cache.pop(lru)
                self.cache[key] = value
            else:
                #not at capacity and not in our cache
                self.cache[key] = value
                self.pagefaultcount += 1


#2/6/24:

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()
        self.pagefaultcount = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: #remove current k, v pair and insert at rear 
            result = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = result
            return result
        
     
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            #don't forget self in self.cache for len(self.cache)
            if self.cap == len(self.cache):
                lru = next(iter(self.cache))
                self.cache.pop(lru)
                self.cache[key] = value
            else:
                self.cache[key] = value
                self.pagefaultcount += 1
       
  

#2/8/24:

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cachd = OrderedDict()
        self.pagefaultcount = 0
        

    def get(self, key: int) -> int:
        if key in self.cachd:
            result = self.cachd[key]
            self.cachd.pop(key)
            self.cachd[key] = result
            return result
        else:
            return -1

        
     
    def put(self, key: int, value: int) -> None:
        if key in self.cachd:
            self.cachd.pop(key)
            self.cachd[key] = value
        else:
            if len(self.cachd) == self.cap:
                lru = next(iter(self.cachd))
                self.cachd.pop(lru)
                self.cachd[key] = value
            else:
                self.cachd[key] = value
                self.pagefaultcount += 1


#2/10/24:

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cachd = dict()
        self.pagefaultcount = 0
      
        

    def get(self, key: int) -> int:
        if key not in self.cachd:
            return -1
        else:
            result = self.cachd[key]
            self.cachd.pop(key)
            self.cachd[key] = result
            return result
     
        
     
    def put(self, key: int, value: int) -> None:
        if key in self.cachd:
            self.cachd.pop(key)
            self.cachd[key] = value
        else:
            if self.cap == len(self.cachd):
                lru = next(iter(self.cachd))
                self.cachd.pop(lru)
                self.cachd[key] = value
            else:
                #we don't need to pop the item pair because the key dosen't exist in the dictionary, so we just add it 
                self.cachd[key] = value
                self.pagefaultcount += 1
            
        

     
       

        
#2/16/24:

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity #positive integer given to us 
        self.mydict = OrderedDict()
        self.pagefaultcount = 0

    def get(self, key: int) -> int:
        if key not in self.mydict:
            return -1
        else:
            result = self.mydict[key]
            self.mydict.pop(key)
            self.mydict[key] = result
            return result
        
    def put(self, key: int, value: int) -> None:
        if key in self.mydict:
            self.mydict.pop(key)
            self.mydict[key] = value
        else:
            if len(self.mydict) == self.cap:
                lru = next(iter(self.mydict))
                self.mydict.pop(lru)
                self.mydict[key] = value
            else: #since the key is not in our dictionary, you don't pop it!!!
                self.mydict[key] = value
                self.pagefaultcount += 1

       


#2/21/24:


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity #integer given to us
        self.dict = OrderedDict()
        self.pagefaultcount = 0
         
        
        
       
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            result = self.dict[key]
            self.dict.pop(key)
            self.dict[key] = result
            return result
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            self.dict[key] = value
        else:
            if self.cap == len(self.dict):
                lru = next(iter(self.dict)) #our key is not in our dict, so we have to REMOVE FROM THE FRONT OF THE DICT, SO WE DON'T PASS IN ANY KEY TO SELF.DICT!
                self.dict.pop(lru)
                self.dict[key] = value
            else:
                self.dict[key] = value
                self.pagefaultcount += 1

 

#2/28/24:

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity #positive integer given to us
        self.cache = OrderedDict()
        self.pagefaultcount = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: #key is in self.cache dict
            result = self.cache.pop(key) #remove 
            self.cache[key] = result #insert to rear
            return result #return inserted result
            
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.cap:
                lru = next(iter(self.cache)) #get from front
                self.cache.pop(lru) #pop from front
                self.cache[key] = value #add to rear
            else:
                self.cache[key] = value
                self.pagefaultcount += 1
       

                
#3/6/24 practice:

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity #positive integer given to us
        self.mydict = dict()
        self.pagefaultcount = 0
        
       
    def get(self, key: int) -> int:
        if key not in self.mydict:
            return -1
        else: #key already exists in our dictionary, so we pop and insert at rear
            res = self.mydict.pop(key)
            self.mydict[key] = res
            return res

      

    def put(self, key: int, value: int) -> None:
        if key in self.mydict: #key exists
            self.mydict.pop(key)
            self.mydict[key] = value
        else:
            if len(self.mydict) == self.cap: #key does not exist and reached capacity
                lru = next(iter(self.mydict))
                self.mydict.pop(lru)
                self.mydict[key] = value
            else: #key does not exist and have not reached capacity
                self.mydict[key] = value
                self.pagefaultcount += 1
        
        

      
