
#1570
#medium

#Given two sparse vectors, compute their dot product.

#Implement class SparseVector:

#SparseVector(nums) Initializes the object with the vector nums
#dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
#A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

#Example 1:

#Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
#Output: 8
#Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
#v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
#Example 2:

#Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
#Output: 0
#Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
#v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

#Follow up: What if only one of the vectors is sparse?


#my own solution using python3 after clarifying the format of the input from someone else's solution:

class SparseVector:
    def __init__(self, nums: List[int]):
        self.one = nums
        print(self.one)


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        self.two = vec.one #so apparently the other array is vec.whatevernameyoudeclaredasnumsintheinit
        res = 0
        for i in range(len(self.one)):
            res += (self.one[i] * self.two[i])
        return res

