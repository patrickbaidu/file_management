number_file = open("file_management/integer_file_reader/numbers.txt")

number_list = []
odd_number_list = []
even_number_list = []


for line in number_file:
    line = int(line.strip())
    number_list.append(line)

for number in number_list:
    if number % 2 == 0:
        even_number_list.append(number)
    else:
        odd_number_list.append(number)

print(number_list)
print(odd_number_list)
print(even_number_list)

number_file.close()