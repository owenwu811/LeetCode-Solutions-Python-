


#676
#medium


#Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

#Implement the MagicDictionary class:

#MagicDictionary() Initializes the object.
#void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
#bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.


#my own solution using python3:

class MagicDictionary:

    def __init__(self):
        self.d = defaultdict(int)
        self.longest = 0
        self.shortest = float('inf')

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.longest = max(self.longest, len(word))
            self.shortest = min(self.shortest, len(word))
            self.d[word] += 1
        
    def search(self, searchWord: str) -> bool:
        if len(searchWord) > self.longest or len(searchWord) < self.shortest:
            return False
        for k in self.d.keys():
            now = 0
            if len(k) == len(searchWord):
                for i in range(len(searchWord)):
                    print(searchWord[i], k[i])
                    if searchWord[i] != k[i]:
                        now += 1
                if now == 1:
                    print("h")
                    return True
        return False
