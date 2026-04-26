from integer_functionalities import IntegerFunctionalities

number_list = []
file_name = "file_management/integer_file_reader/numbers.txt"

number_file = IntegerFunctionalities.open_number_file(file_name)

for line in number_file:
    line = IntegerFunctionalities.make_number_integer(line)
    number_list.append(line)

for number in number_list:
    even_numbers = IntegerFunctionalities.get_even(number)
    odd_numbers = IntegerFunctionalities.get_odd(number)
    even_numbers = ", ".join(even_numbers)
    odd_numbers = ", ".join(odd_numbers)

separate_file = IntegerFunctionalities.write_number_file(odd_numbers, even_numbers)