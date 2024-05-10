
#A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

#Every adjacent pair of words differs by a single letter.
#Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#sk == endWord
#Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

#Example 1:

#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5
#Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.



#python3 solution:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        #run bfs 
        visited = set(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)): #initially just beginWord
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in neighbor[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0


#practice again 5/6/24:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord) #we need to start the recursion with beginWord 
        for word in wordList:
            for j in range(len(word)): #j increases in next iteration
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        visited = set(beginWord) #the purpose of the set is to avoid redundant visits and to increase time complexity 
        q = deque([beginWord])
        res = 1
        #the goal of the bfs traversal here in the word ladder problem is to explore all paths that could lead from begword to endword by flipping one letter in each iteration and almost backtracking by using the set if the path goes down the wrong way not leading towards endword
        while q:
            for i in range(len(q)):
                cur = q.popleft() #bfs = fifo
                if cur == endWord: 
                    return res
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in neighbor[pattern]:
                        if n not in visited:
                            visited.add(n) 
                            q.append(n)
            res += 1
        return 0


#important insight:

#BFS works to find the shortest path summary because BFS traverses the graph level by level outwards from the start -- because we're making sure we look at all the neighbors of all the vertices on the current level, it means that the first time that we see some vertex u means that we've found the shortest path to u. I think path means how many movement zig zags it takes to get to somewhere



#5/7/24 refresher:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        visited = set(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)): 
                cur = q.popleft() 
                if cur == endWord:
                    return res
                for j in range(len(cur)): #j increases in every iteration
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0


#5/8/24 refresher:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList: #we need to filter each word
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word) #as we get to the word, we will add it as value in the dictionary
        visited = set(beginWord) #more efficient bfs for shortest path
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)): #start with beginWord and flip one letter
                cur = q.popleft() #starts with only beginWord in the queue
                if cur == endWord: #base case if we already reached endWord through flips
                    return res
                for i in range(len(cur)):
                    pattern = cur[:i] + "*" + cur[i + 1:]
                    for n in neighbor[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0

#5/10/24 refresher:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList: 
            for j in range(len(beginWord)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        visited = set(beginWord) #increase time complexity so we don't visit the same word more than once
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0
            
