class OpenFile:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        number_file = open(self.file_name)
        return number_file

class IntegerFunctions:
    
    def __init__(self, integers):
        self.integers = integers
    
    def get_integer(self):
        list_of_integers = []
        for integer in self.integers:
            integer = int(integer.strip())
            list_of_integers.append(integer)
        return list_of_integers

    def square_integer(self, list_of_integers):
        squared_integers_list = []
        for integer in list_of_integers:
            squared_integer = integer ** 2
            squared_integer = str(squared_integer)
            squared_integers_list.append(squared_integer)
        squared_integers_list = ", ".join(squared_integers_list)
        return squared_integers_list
    
    def cube_integer(self, list_of_integers):
        cubed_integers_list = []
        for integer in list_of_integers:
            cubed_integer = integer ** 3
            cubed_integer = str(cubed_integer)
            cubed_integers_list.append(cubed_integer)
        cubed_integers_list = ", ".join(cubed_integers_list)
        return cubed_integers_list
    
class WriteFile:
    
    def __init__(self, squared_integer, cubed_integer):
        self.squared_integer = squared_integer
        self.cubed_integer = cubed_integer
    
    def write_file(self):
        squared_integer_file = open("double.txt", "w")
        cubed_integer_file = open("triple.txt", "w")
        squared_integer_file.write(self.squared_integer)
        cubed_integer_file.write(self.cubed_integer)