
#Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

#Return the sorted string. If there are multiple answers, return any of them.

#Input: s = "tree"
#Output: "eert"
#Explanation: 'e' appears twice while 'r' and 't' both appear once.
#So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.



#my solution in python3:

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        minheap = []
        for letter in d:
            heapq.heappush(minheap, [d[letter], letter])
            print(minheap)
        minheap.sort()
        res = ""
        for i in range(len(minheap) -1, -1, -1):
            res += minheap[i][1] * minheap[i][0]
        return res

