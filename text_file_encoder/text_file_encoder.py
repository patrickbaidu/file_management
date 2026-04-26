from text_file_encoder_functions import FileHandling
from text_file_encoder_functions import InputText
from text_file_encoder_functions import Color

file_name = "my_life.txt"

file_name = FileHandling(file_name)
make_file = file_name.open_file()

try:
    user_input = InputText.get_input()
    file_name.append_input(make_file, user_input)

    while True:
        second_input = InputText.get_second_input()
        if second_input == "y":
            user_input = InputText.get_input()
            file_name.append_input(make_file, user_input)
        elif second_input == "n":
            print(f"{Color.green + Color.bold}Thank You For Using This Program.{Color.end}")
            break
        else:
            print("Please Enter an Appropriate Value.")

except:
    print("Error in Handling the request.")
