number_file = open("file_management/integer_file_reader/numbers.txt", "r")

file_read = number_file.read()

for line in file_read:
    print(line)

number_file.close()