


#1804
#medium


#A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

#Implement the Trie class:

#Trie() Initializes the trie object.
#void insert(String word) Inserts the string word into the trie.
#int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
#int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
#void erase(String word) Erases the string word from the trie.

#my own solution using python3:

class Trie:

    def __init__(self):
        self.d = defaultdict(int)
        
    def insert(self, word: str) -> None:
        self.d[word] += 1
        
    def countWordsEqualTo(self, word: str) -> int:
        res = 0
        for k in self.d:
            if word == k:
                res += self.d[k]
        return res

    def countWordsStartingWith(self, prefix: str) -> int:
        res = 0
        for k in self.d:
            if k.startswith(prefix):
                res += self.d[k]
        return res
        

    def erase(self, word: str) -> None:
        if word in self.d:
            self.d[word] -= 1
            if self.d[word] == 0:
                del self.d[word]
