#1564
#medium


#You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labelled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

#Boxes are put into the warehouse by the following rules:

#Boxes cannot be stacked.
#You can rearrange the insertion order of the boxes.
#Boxes can only be pushed into the warehouse from left to right only.
#If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
#Return the maximum number of boxes you can put into the warehouse.



#my own solution using python3:

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True) 
        i, j = 0, 0
        res = 0
        while i < len(boxes) and j < len(warehouse):
            if boxes[i] <= warehouse[j]:
                res += 1
                i += 1
                j += 1
            else:
                i += 1
        return res
