from student_grade_file_reader_functions import OpenFile
from student_grade_file_reader_functions import StudentFile
from student_grade_file_reader_functions import HighestGrade
from student_grade_file_reader_functions import TopStudent

file_name = "file_management/student_grade_file_reader/students_grades.txt"

try:
    file = OpenFile(file_name)
    opened_file = OpenFile.open_file(file)
    student_file = StudentFile(opened_file)