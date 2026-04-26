class OpenFile:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        number_file = open(self.file_name)
        return number_file

class GradeFunctionalities:
    
    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade
