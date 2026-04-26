from integer_functionalities import OpenFile
from integer_functionalities import NumberFunctionalities
from integer_functionalities import WriteFile

file_name = "file_management/integer_file_reader/numbers.txt"

file = OpenFile(file_name)
opened_file = OpenFile.open_file(file)
number_file = NumberFunctionalities(opened_file)

list_of_numbers = number_file.get_number()
even_numbers_list = number_file.get_even_number(list_of_numbers)
odd_numbers_list = number_file.get_odd_number(list_of_numbers)

write_number_file = WriteFile(even_numbers_list, odd_numbers_list)
write_number_file.write_file()

print(even_numbers_list)
print(odd_numbers_list)