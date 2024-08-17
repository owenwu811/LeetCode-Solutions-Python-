
#A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

#Implement the Trie class:

#Trie() Initializes the trie object.
#void insert(String word) Inserts the string word into the trie.
#boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

#Input
#["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#Output
#[null, null, true, false, true, null, true]



#my solution - python3:

class Trie:

    def __init__(self):
        self.mydict = dict()
        

    def insert(self, word: str) -> None:
        self.mydict[word] = []
        

    def search(self, word: str) -> bool:
        if word not in self.mydict:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        for d in self.mydict:
            if d.startswith(prefix): #d.startswith is needed!
                return True
        return False


#3/12/24:

class Trie:

    def __init__(self):
        self.mydict = dict()
        

    def insert(self, word: str) -> None:
        self.mydict[word] = []

        

    def search(self, word: str) -> bool:
        if word in self.mydict: 
            return True
        return False
     

    def startsWith(self, prefix: str) -> bool:
        for d in self.mydict:
            if d.startswith(prefix):
                return True
        return False


#3/16/24:

class Trie:

    def __init__(self):
        self.mydict = dict()

    def insert(self, word: str):
        if word not in self.mydict:
            self.mydict[word] = []
        
        


    def search(self, word: str) -> bool:
        for d in self.mydict:
            if d == word:
                return True
        

    def startsWith(self, prefix: str) -> bool:
        for d in self.mydict:
            if d.startswith(prefix):
                return True
        return False


      
#4/6/24 review:

class Trie:

    def __init__(self):
        self.mydict = dict()
        

    def insert(self, word: str) -> None:
        if word not in self.mydict:
            self.mydict[word] = 0
        self.mydict[word] += 1
        

    def search(self, word: str) -> bool:
        for d in self.mydict:
            if d == word:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for d in self.mydict:
            if d.startswith(prefix):
                return True
        return False


#5/14/24 refresher (my own solution):

class Trie:

    def __init__(self):
        self.d = dict()
        

    def insert(self, word: str) -> None:
        self.d[word] = 1


    def search(self, word: str) -> bool:
        for k in self.d:
            if k == word:
                return True
        return False


        

    def startsWith(self, prefix: str) -> bool:
        for j in self.d:
            if j.startswith(prefix):
                return True
        return False

#8/16/24 review:

class Trie:

    def __init__(self):
        self.d = dict()
        
        

    def insert(self, word: str) -> None:
        self.d[word] = []


        

    def search(self, word: str) -> bool:
        if word in self.d:
            return True
        return False
     

    def startsWith(self, prefix: str) -> bool:
        for k in self.d:
            if k.startswith(prefix):
                return True
        return False
        
        
        
