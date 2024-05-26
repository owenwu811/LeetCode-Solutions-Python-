
#Implement the RandomizedSet class:

#RandomizedSet() Initializes the RandomizedSet object.
#bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
#You must implement the functions of the class such that each function works in average O(1) time complexity.



#python3 solution:

class RandomizedSet:
    def __init__(self):
        self.mylist = []
        self.mydict = dict()

    def insert(self, val: int) -> bool:
        if val not in self.mydict:
            self.mylist.append(val)
            self.mydict[val] = len(self.mylist) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mydict: #remove 1 from [1, 2]
            last = self.mylist[-1] #2
            index = self.mydict[val] #0
            self.mylist[index] = last #[2, 2]
            self.mylist.pop() #[2]
            self.mydict[last] = index #{2: 0}
            del self.mydict[val] #we delete the original value we intended to delete - the above is just because we popped from list, so we have to reflect that in our dictionary
            return True
        return False

    def getRandom(self) -> int: 
        return random.choice(self.mylist)

#inserting and removing a value is 0(1) using a set
#searching is also 0(1) for a set
#you cannot index into a set because sets are unordered in python
#converting set to list would take o(n), so we can't just maintain hashset - we need a list at same time
#EVERYTIME WE ADD A VALUE TO THE SET, WE ALSO ADD THE VALUE TO THE LIST - getting random value will be o(1) operation

#if we would insert 1, we call out insert function that is given to us. since 1 is not in our set, we add 1 to our set (unordered) and also add 1 to end of our list
#next, we want to add 2 - check if 2 is in our set. since 2 is not in our set, we add 2 to our set and append 2 to the end of our list
#we want to add 1, and since 1 is already in our set, so we do not add another 1 to our set and we don't add another 1 to our list
#now, if we wanted a random value, we would look at the 2 values in our list [1, 2] and generate a random value between 0 and 1 because 0 and 1 are the indicies, and we would return either one of the values.

#if we want to remove 2, we check if in set. if it is, pop 2 from the set and also 2 from the end of the list

#to remove a value from middle of array, we must shift everything over to the left, which is o(n)

#if we were removing 2 in our set also in our list as the value 2 in our list, we don't know what index 2 is at, so we need to search entire array to find 2. since 2 is in our hashet, we know it exists in our array for sure, but we just don't know where it is. 

#instead of using a set, we use a hashmap as {valueweinserted: indexinsertedat}, so if our hashmap was {1, 2, 3}, it would map to 0, 1, 2 in our list

#to remove 2 in our list, we can't just remove 2 and replace it with a default value of 0 because if we wanted to generate a random value, what it if landed at the spot the value 0 in our list is at

#we TAKE LAST VALUE OF ARRAY AND COPY IT INTO INDEX OF ARRAY we are removing from (3 of index 2 shifts to the 2 of index 1 position and then 3 is popped from rear of list) and then popping that value from rear of list so that we don't consider that popped position a valid position anymore, so that now the length of the array is one less and contiguous, we can generate a random value in o(1) time because we did not have to shift the entire array with all its elements left - we only had to swap one value in the array. we also have to update this in our hashmap, so since 3 originally mapped to the now popped index 2 in our array that now dosen't exist, 3 should now map to index 1

#set = {1}
#list = [1, 2] append to rear of list


#practice run again with my own thoughts:

class RandomizedSet:
    def __init__(self):
        self.mydict = dict()
        self.mylist = []



    def insert(self, val: int) -> bool:
        if val not in self.mydict: #we use dict instead of set
            self.mylist.append(val) #length must change before we can determine the index to be added to righthand side of dictionary
            self.mydict[val] = len(self.mylist) - 1
            return True #return True if item was not present (instructions)
        return False #return False if item was present (instructions)
 
    def remove(self, val: int) -> bool:
        if val in self.mydict: #we use dict instead of set
            #instructions say to remove val from mydict if present - we use dict instead of set
            #[1, 2] > let's say we want to remove 1
            rear = self.mylist[-1] #2
            indextoplace = self.mydict[val] #0
            self.mylist[indextoplace] = rear #[1, 2] becomes [2, 2] as we placed 2 in the index 0 position
            self.mylist.pop() #[2, 2] becomes [2] 
            self.mydict[rear] = indextoplace #2 is now at index 0 of our list not index 1 because index 1 dosen't exist anymore, so our dictionary must reflect whatever was in our list in terms of being added and removed
            del self.mydict[val] #remove value from mydict aka set as originally intended from instructions
            return True #instructions say to return True if item was present, and it was because we were able to remove it (item referring to val)
        return False



    def getRandom(self) -> int: 
        return random.choice(self.mylist)


#5/26/24 review:

class RandomizedSet:

    def __init__(self):
        self.mydict = dict()
        self.mylist = []
        

    def insert(self, val: int) -> bool:
        if val not in self.mydict:
            self.mylist.append(val)
            self.mydict[val] = len(self.mylist) - 1
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.mydict:
            rear = self.mylist[-1]
            indextoplace = self.mydict[val]
            self.mylist[indextoplace] = rear
            self.mylist.pop()
            self.mydict[rear] = indextoplace
            del self.mydict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.mylist)
