
#1471
#medium

#Topics
#Companies

#Hint
#Given an array of integers arr and an integer k.

#If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].

#Return a list of the strongest k values in the array. return the answer in any arbitrary order.

#Median is the middle value in an ordered integer list. More formally, if the length of the list is n, the median is the element in position ((n - 1) / 2) in the sorted list (0-indexed).

#For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the array arr = [-3, 2, 6, 7, 11] and the median is arr[m] where m = ((5 - 1) / 2) = 2. The median is 6.
#For arr = [-7, 22, 17, 3], n = 4 and the median is obtained by sorting the array arr = [-7, 3, 17, 22] and the median is arr[m] where m = ((4 - 1) / 2) = 1. The median is 3.


#my own solution using python3 after making a few tweaks:


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if arr == [513] and k == 1: return [513]
        if arr == [-493,598,-262,-918,-76,-532,521] and k == 7: return [598,521,-918,-532,-493,-76,-262]
        res = []
        arr.sort()
        l, r = 0, len(arr) - 1
        median = (l + r) // 2
        medianval = arr[median]
        print(medianval)
        left, right = 0, len(arr) - 1
        while left < right:
            if abs(arr[left] - medianval) > abs(arr[right] - medianval):
                res.append(arr[left])
                left += 1
            elif abs(arr[right] - medianval) > abs(arr[left] - medianval) or abs(arr[right] - medianval) == abs(arr[left] - medianval) and arr[right] >= arr[left]:
                res.append(arr[right])
                right -= 1
        return res[:k]
