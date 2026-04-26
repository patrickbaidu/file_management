class FileHandling:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        text_file = open(self.file_name, "a")
        return text_file
    
    def append_input(self, text_file, text_input):
        text_file.write("\n" + text_input)

class InputText:
    
    def get_input():
        user_input = input("Enter Line: ")
        return user_input
    
    def get_second_input():
        second_input = input("Are there more lines? y/n: ")
        return second_input
    
class Color:
    purple = '\033[95m'
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    green = '\033[92m'