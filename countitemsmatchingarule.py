
#1773
#easy

#You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

#The ith item is said to match the rule if one of the following is true:

#ruleKey == "type" and ruleValue == typei.
#ruleKey == "color" and ruleValue == colori.
#ruleKey == "name" and ruleValue == namei.
#Return the number of items that match the given rule.

 

#Example 1:

#Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
#Output: 1
#Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].


#my own solution using python3:

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for a, b, c in items:
            if ruleKey == "type" and ruleValue == a or ruleKey == "color" and ruleValue == b or ruleKey == "name" and ruleValue == c:
                res += 1
        return res
