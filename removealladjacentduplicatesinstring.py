
#1209

#You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

#We repeatedly make k duplicate removals on s until we no longer can.

#Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.



#my incorrect solution that got time limit exceeded with 19/21 test cases passing:

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            origk = k
            stack.append(char)
            if len(stack) < k:
                continue
            portion = stack[len(stack) - k:]
            if len(set(portion)) == 1:
                while k > 0 and stack:
                    stack.pop()
                    k -= 1
                k = origk
        return "".join(stack)


#the correct solution:

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1][0]: #seeing same character again
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1]) #need brackets here
        res = []
        for i, j in stack: #don't need enumerate here because we are just unpacking each sublist
            res.append(i * j)
        return "".join(res)


#another much more intuitive way from grokking course that I came up with using their psuedocode:

def remove_duplicates(s):
    stack = []
    for char in s:
      if stack and char == stack[-1]:
        stack.pop()
      else:
        stack.append(char)
    return "".join(stack)

