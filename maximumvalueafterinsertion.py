
#1881
#medium

#You are given a very large integer n, represented as a string,​​​​​​ and an integer digit x. The digits in n and the digit x are in the inclusive range [1, 9], and n may represent a negative number.

#You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n​​​​​​. You cannot insert x to the left of the negative sign.

#For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
#If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
#Return a string representing the maximum value of n​​​​​​ after the insertion.

 

#Example 1:

#Input: n = "99", x = 9
#Output: "999"
#Explanation: The result is the same regardless of where you insert 9.
#Example 2:

#Input: n = "-13", x = 2
#Output: "-123"
#Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.


#my own solution using python3:

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        n = list(n)
        orig = n.copy()
        if n[0] == "-":
            j = []
            for i in range(1, len(n)):
                if x < int(n[i]):
                    n.insert(i, str(x))
                    print(n)
                    j.append("".join(n.copy()))
                    n[:] = orig 
                    break
            n[:] = orig
            #print(n, "n")
            n.append(str(x))
            #print(n)
            j.append("".join(n))
            #print(j)
            j.sort()
            return j[0]
        for i in range(len(n)):
            j = []
            if x > int(n[i]):
                n.insert(i, str(x))
                j.append("".join(n.copy()))
                n[:] = orig
                break
        n[:] = orig
        n.append(str(x))
        j.append("".join(n))
        j.sort()
        print("".join(j))
        return max(j)
