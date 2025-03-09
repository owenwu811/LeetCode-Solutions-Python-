#easy
#412


#Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.




#correct python3 solution:

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * n
        for i in range(1, n + 1): #start from 1
            if i % 3 == 0 and i % 5 == 0:
                res[i - 1] = "FizzBuzz" #i - 1 because indicies are one less than length
            elif i % 3 == 0:
                res[i - 1] = "Fizz" 
            elif i % 5 == 0:
                res[i - 1] = "Buzz"
            else:
                res[i - 1] = str(i)
        return res



        
