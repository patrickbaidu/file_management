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

class WriteFile:
    
    def __init__(self):
        pass