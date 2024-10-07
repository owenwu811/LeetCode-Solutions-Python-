

#2512
#medium


#You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

#Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

#You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

#Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

 

#Example 1:

#Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
#Output: [1,2]
#Explanation: 
#Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.


#my own solution using python3 after minor hint about using set positive_feedback:

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        res = []
        myheap = []
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        for i, s in enumerate(student_id):
            points = 0
            formatted = report[i].split(" ")
            student = []
            #print(formatted)
            for word in formatted:
                if word in positive_feedback:
                    points += 3
                elif word in negative_feedback:
                    points -= 1
            student.append([points, s])
            heapq.heappush(myheap, [-points, s])
        print(myheap)
        while k > 0:
            a, b = heapq.heappop(myheap)
            res.append(b)
            k -= 1
        return res

