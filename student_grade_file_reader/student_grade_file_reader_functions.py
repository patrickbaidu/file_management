class OpenFile:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        grades_file = open(self.file_name)
        return grades_file

class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def split_data_file(self, grades_file):
        student_name_list = []
        student_grade_list = []
        data_list = []
        for data in grades_file:
            data = data.replace(" = ", "")
            data = data.split()
            data_list.append(data)
        for data in data_list:
            student_name_list.append([0])
            student_grade_list.append([1])
        return student_grade_list and student_name_list
    
class GradeFunctionalities:
    
    def __init__(self, student_grade):
        self.student_grade = student_grade
    