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
        data_list = []
        for data in self.grades_file:
            data = data.strip()
            data = data.replace(" =", "")
            data = data.split()
            data_list.append(data)
        return data_list
    
    def add_student_name(self, data_list):
        student_name_list = []
        for data in data_list:
            student_name_list.append(data[0])
        return student_name_list
    
    def add_student_grade(self, data_list):
        student_grade_list = []
        for data in data_list:
            student_grade_list.append(data[1])
        return student_grade_list
    
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
    
    def __init__(self, student_list):
        self.student_list = student_list
    
    def get_top_student(self, index_grade):
        top_student_index = index_grade
        top_student = self.student_list.index(top_student_index)
        return top_student