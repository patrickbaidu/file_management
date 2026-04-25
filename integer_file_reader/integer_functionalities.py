class IntegerFunctionalities:
    
    def __init__(self, oddnumber, evennumber, number, filename, numberfile, numberline):
        self.oddnumber = oddnumber
        self.evennumber = evennumber
        self.number = number
        self.filename = filename
        self.numberfile = numberfile
        self.numberline = numberline
    
    def make_number_integer(self, numberline):
        numberline = int(numberline.strip())
    
    def get_even(self, number):
        even_number_list = []
        if number % 2 == 0:
            number = str(number)
            even_number_list.append(number)
        return even_number_list
    
    def get_odd(self, number):
        odd_number_list = []
        if number % 2 == 1:
            number = str(number)
            odd_number_list.append(number)
        return odd_number_list
    
    def open_number_file(self, filename):
        number_file = open(filename)
        number_file.close()
    
    def write_number_file(self, oddnumber, evennumber):
        odd_number_file = open("odd_numbers.txt", "w")
        even_number_file = open("even_numbers.txt", "w")
        
        odd_number_file.write(oddnumber)
        even_number_file.write(evennumber)