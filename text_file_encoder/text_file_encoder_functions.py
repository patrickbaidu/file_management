class FileHandling:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def open_file(self):
        text_file = open(self.file_name, "a")
        return text_file
    
    def append_file(self, text_file, input):
        text_file.write(input)

class InputText:
    
    def __init__(self, input_text):
        self.input_text = input_text
    
    def get_input(self):
        for input in self.input_text:
            append_input = FileHandling.append_file(input)
        return append_input