
#1268
#medium

#You are given an array of strings products and a string searchWord.

#Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

#Return a list of lists of the suggested products after each character of searchWord is typed.

 

#Example 1:

#Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
#Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
#Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
#After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
#After typing mou, mous and mouse the system suggests ["mouse","mousepad"].


#my own solution using python3:

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        cur = []
        for i, c in enumerate(searchWord):
            tmp = []
            for p in products:
                if p.startswith(searchWord[:i + 1]):
                    tmp.append(p)
            cur.append(tmp)
        for c in cur:
            c.sort()
        res = []
        for i, c in enumerate(cur):
            turn = []
            count = 1
            print(cur[i])
            for j in range(len(cur[i])):
                print(cur[i][j])
                if count <= 3:
                    turn.append(cur[i][j])
                count += 1
            res.append(turn)
        print(res)
        return res
