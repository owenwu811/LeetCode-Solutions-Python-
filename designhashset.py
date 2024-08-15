
#705
#easy
#67.1%acceptancerate

#Design a HashSet without using any built-in hash table libraries.

#Implement MyHashSet class:

#void add(key) Inserts the value key into the HashSet.
#bool contains(key) Returns whether the value key exists in the HashSet or not.
#void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

#my own solution using python3:

class MyHashSet:

    def __init__(self):
        self.myset = set()
        

    def add(self, key: int) -> None:
        self.myset.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.myset:
            self.myset.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.myset
