#682
#easy

#You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

#You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

#An integer x.
#Record a new score of x.
#'+'.
#Record a new score that is the sum of the previous two scores.
#'D'.
#Record a new score that is the double of the previous score.
#'C'.
#Invalidate the previous score, removing it from the record.
#Return the sum of all the scores on the record after applying all the operations.

#Input: ops = ["5","2","C","D","+"]
#Output: 30
#Explanation:
#"5" - Add 5 to the record, record is now [5].
#"2" - Add 2 to the record, record is now [5, 2].
#"C" - Invalidate and remove the previous score, record is now [5].
#"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
#"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
#The total sum is 5 + 10 + 15 = 30.



#my own solution using python3:

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for o in operations:
            if o != "+" and o != "D" and o != "C":
                res.append(o)
            elif o == "+":
                last = int(res[-1])
                secondlast = int(res[-2])
                res.append(last + secondlast)
            elif o == "D":
                last = int(res[-1])
                res.append(last * 2)
            elif o == "C":
                res.pop()
        print(res)
        ans = 0
        for r in res:
            if type(r) == int:
                ans += r
            elif r[0] == "-":
                ans += (int(r[1:]) * -1)
            else:
                ans += int(r)
        print(ans)
        return ans
