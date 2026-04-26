from student_grade_file_reader_functions import OpenFile
from student_grade_file_reader_functions import StudentFile
from student_grade_file_reader_functions import HighestGrade
from student_grade_file_reader_functions import TopStudent

file_name = "file_management/student_grade_file_reader/students_grades.txt"

try:
    file = OpenFile(file_name)
    opened_file = OpenFile.open_file(file)
    student_file = StudentFile(opened_file)

    student_data_list = student_file.split_data_file()
    student_name_list = student_file.add_student_name(student_data_list)
    student_grade_list = student_file.add_student_grade(student_data_list)

    student_grades = HighestGrade(student_grade_list)
    highest_grade = student_grades.get_max_grade()
    highest_grade_index = student_grades.get_grade_index(highest_grade)

    student_names = TopStudent(student_name_list)
    top_student = student_names.get_top_student(highest_grade_index)

    print(top_student, highest_grade)

except:
    print("Error in handling the request.")
