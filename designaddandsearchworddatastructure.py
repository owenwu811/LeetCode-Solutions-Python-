

#Design a data structure that supports adding new words and finding if a string matches any previously added string.

#Implement the WordDictionary class:

#WordDictionary() Initializes the object.
#void addWord(word) Adds word to the data structure, it can be matched later.
#bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

  


#python3 solution:

class WordDictionary:
    def __init__(self):
        self.lst = []
        

    def addWord(self, word: str) -> None:
        self.lst.append(word)

        

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.lst
        for worddd in self.lst:
            if len(worddd) != len(word):
                continue
            #is of same length, so we iterate over word (given to us) because we were told "." could be in word and could count for a requirement from word for worddd
            for i in range(len(word)):
                if word[i] == ".":
                    continue
                if word[i] != worddd[i]:
                    break
            #assuming we don't break aka try the next word in our list to see if match, then that means "." did all it's job or the letters were the exact same between worddd and word (given to us), so we return True
            else:
                return True
        return False #we looked through all words in our list and couldn't find any matches even with ".", so return False
         
