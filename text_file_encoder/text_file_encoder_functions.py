class AppendFile:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        text_file = open(self.file_name, "a")
        return text_file
    
    def append_file(self, text_file, input):
        text_file.write(input)

class InputText:
    
    def __init__(self):
        pass