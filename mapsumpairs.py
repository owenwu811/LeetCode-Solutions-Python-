
#medium
#56.8%acceptancerate

#Design a map that allows you to do the following:

#Maps a string key to a given value.
#Returns the sum of the values that have a key with a prefix equal to a given string.
#Implement the MapSum class:

#MapSum() Initializes the MapSum object.
#void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
#int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix

#my own solution using python3:


#note that this problem and solution is identical to Implement Trie (leetcode 208) prefix tree!!!!!


class MapSum:

    def __init__(self):
        self.d = dict()
        

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
        

    def sum(self, prefix: str) -> int:
        res = 0
        for k in self.d:
            if k.startswith(prefix):
                res += self.d[k]
        return res
