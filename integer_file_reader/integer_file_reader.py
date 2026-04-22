number_file = open("file_management/integer_file_reader/numbers.txt")

number_list = []
odd_number_list = []
even_number_list = []


for line in number_file:
    line = int(line.strip())
    number_list.append(line)

for number in number_list:
    if number % 2 == 0:
        number = str(number)
        even_number_list.append(number)
    else:
        number = str(number)
        odd_number_list.append(number)

print(number_list)
print(odd_number_list)
print(even_number_list)

odd_numbers = ", ".join(odd_number_list)
even_numbers = ", ".join(even_number_list)

odd_number_file = open("odd_numbers.txt", "w")
even_number_file = open("even)numbers.txt", "w")

odd_number_file.write(odd_numbers)    
even_number_file.write(even_numbers)

number_file.close()
