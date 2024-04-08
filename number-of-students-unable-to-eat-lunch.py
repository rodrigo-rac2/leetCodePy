# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        repeat = 0
        l_s = len(students)
        while sandwiches and repeat < l_s:
            student = students[0]
            students = students[1:]
            if student == sandwiches[0]:
                sandwiches = sandwiches[1:]
                repeat = 0
            else:
                repeat += 1
                students.append(student)
            l_s = len(students)
        return len(students)
