class OpenFile:
    
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        number_file = open(self.file_name)
        return number_file

class NumberFunctionalities:
    
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get_number(self, numbers):
        list_of_numbers = []
        for number in numbers:
            number = int(number.strip())
            list_of_numbers.append(number)
        return list_of_numbers
    
    def get_even_number(self, list_of_numbers):
        even_number_list = []
        for even_number in list_of_numbers:
            if even_number % 2 == 0:
                even_number = str(even_number)
                even_number_list.append(even_number)
        even_number_list = ", ".join(even_number_list)
        return even_number_list
    
    def get_odd_number(self, list_of_numbers):
        odd_number_list = []
        for odd_number in list_of_numbers:
            if odd_number % 2 == 1:
                odd_number = str(odd_number)
                odd_number_list.append(odd_number)
        odd_number_list = ", ".join(odd_number_list)
        return odd_number_list
