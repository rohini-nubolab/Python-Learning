# function to check if small string is there in big string

def sub_string(string, sub_str):

    if (string.find(sub_str) == -1):
        print("No")
    else:
        print("Yes")


string = "Welcome python"
sub_str = "python"
sub_string(string, sub_str)

string = "Welcome python"
sub_str = "program"
sub_string(string, sub_str)
