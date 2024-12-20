#599
#easy


#Given two arrays of strings list1 and list2, find the common strings with the least index sum.

#A common string is a string that appeared in both list1 and list2.

#A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

#Return all the common strings with the least index sum. Return the answer in any order.

 

#Example 1:

#Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
#Output: ["Shogun"]
#Explanation: The only common string is "Shogun".

#my own solution using python3:

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        smallest = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    res.append([i + j, list1[i]])
                    smallest = min(smallest, i + j)
        print(res)
        print(smallest)
        new = []
        for r in res:
            if r[0] == smallest:
                new.append(r[1])
        return new
        
