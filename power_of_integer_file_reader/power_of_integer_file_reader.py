from power_of_integer_functionalities import OpenFile
from power_of_integer_functionalities import IntegerFunctions
from power_of_integer_functionalities import WriteFile

file_name = "file_management/power_of_integer_file_reader/integers.txt"

file_name = OpenFile(file_name)
opened_file = file_name.open_file()

integer_file = IntegerFunctions(opened_file)
integer_list = integer_file.get_integer()

squared_integers = integer_file.square_integer(integer_list)
cubed_integers = integer_file.cube_integer(integer_list)

print(squared_integers)
print(cubed_integers)