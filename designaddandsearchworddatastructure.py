

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
         

#5/7/24 (missed):

class WordDictionary:

    def __init__(self):
        self.lst = []
        

    def addWord(self, word: str) -> None:
        self.lst.append(word)


    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.lst
        #we know "." is in word now, so like "ab." "abc" 
        for w in self.lst:
            if len(w) != len(word): #because "." can only match one character, so the length still needs to be the same between word = "ab." and w = "abc"
                continue
            #lengths match - "ab." "abc"
            for i in range(len(word)):
                if word[i] == ".": #".b" "cb"
                    continue
                if w[i] != word[i]: #".c" "cb"
                    break
            else: #hasn't been broken yet aka the loop was allowed to finish all iterations - The else clause in a for loop in Python has a special meaning. It is executed only if the loop completes all its iterations without encountering a break statement!!!!!!
                return True
        return False

#6/9/24 review:

class WordDictionary:
    def __init__(self):
        self.lst = []
        

    def addWord(self, word: str) -> None:
        self.lst.append(word)


    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.lst
        for wordd in self.lst:
            if len(word) != len(wordd):
                continue
            for i in range(len(word)):
                if word[i] == ".":
                    continue
                elif word[i] != wordd[i]:
                    break
            else: #hasn't been broken yet aka the loop was allowed to finish all iterations - The else clause in a for loop in Python has a special meaning. It is executed only if the loop completes all its iterations without encountering a break statement!!!!!!
                return True
        return False


#6/13/24 review:

class WordDictionary:
    def __init__(self):
        self.mylst = []


    def addWord(self, word: str) -> None:
        self.mylst.append(word)
        

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.mylst
        for worddd in self.mylst:
            if len(word) != len(worddd):
                continue
            for i in range(len(word)):
                if word[i] == ".":
                    continue
                if worddd[i] != word[i]:
                    break
            else:
                return True
        return False

#6/26/24 review:

class WordDictionary:
    def __init__(self):
        self.mydict = dict()
        self.mylist = []
        

    def addWord(self, word: str) -> None:
        self.mylist.append(word)
        

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.mylist
        for worddd in self.mylist:
            if len(worddd) != len(word):
                continue
            for i in range(len(worddd)):
                if word[i] == ".":
                    continue
                if word[i] != worddd[i]:
                    break
            else:
                return True
        return False

#7/8/24 review:

class WordDictionary:

    def __init__(self):
        self.mylist = []
        

    def addWord(self, word: str) -> None:
        self.mylist.append(word)

        
    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.mylist
        for worddd in self.mylist:
            if len(word) != len(worddd):
                continue
            for i in range(len(word)):
                if word[i] == ".":
                    continue
                if word[i] != worddd[i]:
                    break
            else:
                return True
        return False

#8/2/24 refresher:

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
            for i in range(len(worddd)):
                if word[i] == ".":
                    continue
                if word[i] != worddd[i]:
                    break
            else:
                return True
        return False
        
