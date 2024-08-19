
#There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.

#You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

#Return the matrix after sorting it.

#Input: score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2
#Output: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
#Explanation: In the above diagram, S denotes the student, while E denotes the exam.
#- The student with index 1 scored 11 in exam 2, which is the highest score, so they got first place.
#- The student with index 0 scored 9 in exam 2, which is the second highest score, so they got second place.
#- The student with index 2 scored 3 in exam 2, which is the lowest score, so they got third place.


#correct python3 solution:

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        index_dict = {}
        for index, item in enumerate(score): #each item is each sublist in the input
            print(index, item) #0 [10, 6, 9, 1], 1 [7, 5, 11, 2]
            index_dict[item[k]] = index
            print(index_dict) #{9: 0}, {9: 0, 11: 1} 
        print(index_dict) #{9: 0, 11: 1, 3: 2}
        sort_key = sorted(index_dict.keys(), reverse=True)  # sort_key = [11, 9, 3]
        print(sort_key) #[11, 9, 3] #notice index 2 value in each sublist
        output = []
        for key in sort_key:
            output.append(score[index_dict[key]])  
            print(score) #[[10,6,9,1],[7,5,11,2],[4,8,3,15]] - score is just the input list of lists itself, so score[1] = [7, 5, 11, 2]
            print(index_dict) #{9: 0, 11: 1, 3: 2}
            print(output)# output = [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]] - output will include each sublist in the input in the correct order  
        return output
