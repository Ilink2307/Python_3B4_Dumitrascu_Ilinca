import os

################################################################

print("\n\nEx1: A function that returns a list with the sorted extensions")

def order_by_extension(directory_1):
    file_list = os.listdir(directory_1)
    extension_list = []

    for file in file_list:
        file_name, file_extension = os.path.splitext(file)
        if file_extension != '':
            extension_list.append(file_extension[1:])

    extension_list.sort()
    return extension_list

given_directory = "D:\\scoala\\Facultate\\AN 1\\Logica"
print(order_by_extension(given_directory))
################################################################

print("\n\nEx2: File with directory files")

def directory_files(directory, file):
    file_list = os.listdir(directory)

    file = open(file, 'w')

    for file_index in file_list:
        file_name = os.path.splitext(file_index)[0]
        if file_name[0] == "A":
            file.write(os.path.abspath(file_index))
            file.write('\n')

    file.close()
    return "File modified successfully"

given_directory = "D:\\scoala\\Facultate\\AN 1\\Mate" # "D:\\scoala\\Facultate\\AN_2\\Sem1\\AG\\Tema_1"
given_file = "D:\\scoala\\Facultate\\AN_3\\Python\\Python_3B4_Dumitrascu_Ilinca\\lab_5_python\\Directory\\File1.txt"

print(directory_files(given_directory, given_file))
################################################################

print("\n\nEx3: Directory -> extension tuples || File -> last 20 characters")
def file_characters_directory_tuples(my_path):

    extension_list = []
    tuple_list = []
    if os.path.isdir(my_path):
        print("It's a directory: ")
        file_list = os.listdir(my_path)

        for file_index in file_list:
            file_extension = os.path.splitext(file_index)[1]
            extension_list.append(file_extension)
        for extension in extension_list:
            tuple_list.append((extension, extension_list.count(extension)))
        return list(set(tuple_list))

    elif os.path.isfile(my_path):
        print("It's a file: ")
        file = open(my_path, 'r')
        return file.read()[-20:]

given_directory = "D:\\scoala\\Facultate\\AN 1\\Mate" # "D:\\scoala\\Facultate\\AN_2\\Sem1\\AG\\Tema_1"
given_file = "D:\\scoala\\Facultate\\AN_3\\SI\\curs_1_notes.txt"
print(file_characters_directory_tuples(given_directory))
# print(file_characters_directory_tuples(given_file))
################################################################

print("\n\nEx4: Directory -> extension tuples || File -> last 20 characters")
def ordered_extensions(directory):

    file_list = os.listdir(directory)
    extension_list = []

    for file in file_list:
        file_name, file_extension = os.path.splitext(file)
        if file_extension != '':
            extension_list.append(file_extension[1:])

    extension_list.sort()
    return extension_list
print("Diferenta 1 4????")

input_directory = "D:\\scoala\\Facultate\\AN 1\\Logica"
# input("Input a directory: ")
print(ordered_extensions(input_directory))
################################################################

print("\n\nEx5: Find a string in a file or directory")
def search_string(file_path, string):

    with open(file_path, 'r') as file:
        content = file.read()
        if string in content:
            return 1
        else:
            return 0

def find_string(target, to_search):
    file_contains = []
    try:
        assert os.path.isdir(target) or os.path.isfile(target), "target should be a file or a directory"

    except Exception as e:
        print(e)

    else:
        if os.path.isdir(target):
            file_list = os.listdir(target)
            for file_dir in file_list:
                find_string(file_dir, to_search)

        elif os.path.isfile(target):
            if search_string(target, "informatiei"):
                file_contains.append(target)

        print(file_contains)

input_path = "D:\\scoala\\Facultate\\AN_3\\SI\\curs_1_notes.txt"
find_string(input_path, "informatiei ")
################################################################

print("\n\nEx6: ?not now ty?")
################################################################

print("\n\nEx7: Dictionary with path information")
def file_info(file_path):
    dictionary ={
        "full_path": os.path.abspath(file_path),
        "file_size": os.stat(file_path).st_size,
        "file_extension": os.path.splitext(file_path)[1][1:],
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK)
    }

    return dictionary

file = "D:\\scoala\\Facultate\\AN_3\\SI\\curs_1_notes.txt"
print(file_info(file))
################################################################

print("\n\nEx8: Absolute paths of files in a directory")
def file_paths(directory):
    absolute_paths = []

    file_list = os.listdir(directory)
    for content in file_list:
        print(content)
        if os.path.isfile(content):
            print(content)
            absolute_paths.append(os.path.abspath(content))

    return absolute_paths

input_directory = "D:\\scoala\\Facultate\\AN_3\\DSFUM"
print(file_paths(input_directory))
print("Nu merge nush dc, not now ty x2")