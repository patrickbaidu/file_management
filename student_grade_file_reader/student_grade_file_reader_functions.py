class OpenFile:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        grades_file = open(self.file_name)
        return grades_file

class StudentFile:
    
    def __init__(self, grades_file):
        self.grades_file = grades_file
    
    def split_data_file(self):
        student_name_list = []
        student_grade_list = []
        data_list = []
        for data in self.grades_file:
            data = data.replace(" = ", "")
            data = data.split()
            data_list.append(data)
        for data in data_list:
            student_name_list.append([0])
            student_grade_list.append([1])
        return student_grade_list and student_name_list
    
class HighestGrade:
    
    def __init__(self, student_grade):
        self.student_grade = student_grade
    
    def get_max_grade(self):
        max_grade = max(self.student_grade)
        return max_grade
    
    def get_grade_index(self):
        index_grade = self.student_grade.index(HighestGrade.get_max_grade())
        return index_grade

class TopStudent:
    
    def 