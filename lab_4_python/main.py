print("\nEx_1: A function that will receives two lists and returns a list of sets")
def list_operations(list_a, list_b):
    final_set_list = []

    reunion = (set(list_a).union(list_b))
    intersection = (set(list_a).intersection(list_b))
    list1_list2 = (set(list_a).difference(list_b))
    list2_list1 = (set(list_b).difference(list_a))

    final_set_list.append(reunion)
    final_set_list.append(intersection)
    final_set_list.append(list1_list2)
    final_set_list.append(list2_list1)

    return final_set_list

a_list = [0, 1, 2, 3, 4, 5, 6, 7, "False"]
b_list = [6, 7, 8, 9, "True", "False"]
print(list_operations(a_list, b_list))
################################################################

print("\n\nEx_2: A function that receives a string as a parameter and returns a dictionary")
def string_to_dictionary(string):
    dictionary = {}

    for character in string:
        dictionary[character] = string.count(character)
    print(dictionary)

given_string = "Ana has apples."
string_to_dictionary(given_string)
################################################################

print("\n\nEx_3: A function that compares two dictionaries")
def compare_dictionaries(dict_1, dict_2):

    print(dict_1.keys())
    print(dict_1.values())
    if len(dict_1) != len(dict_2):
        return False

    else:
        flag = 0
        for i in dict_1:
            if dict_1.get(i) != dict_2.get(i):
                print(dict_1.get(i))
                print(dict_2.get(i))
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False

dictionary_1 = dict(a=1, b=2, c=dict(d=1, f=1), d=list[1, 2])
dictionary_2 = dict(a=1, b=2, c=dict(d=1, f=1), d=list[1, 2])
print(compare_dictionaries(dictionary_1, dictionary_2))
################################################################

print("\n\nEx_4: A function that compares two dictionaries")
def build_xml_element(tag, content, **name_parameters):

    final_string = "<" + tag + " "
    for name_param in name_parameters.items():
        final_string += (str(name_param[0]) + "=\"" + str(name_param[1])) + "\""
    final_string += "> " + content + "</" + tag + ">"
    print(final_string)

build_xml_element("a", "Hello there", href=" https://python.org ", _class=" my-link ", id=" some_id ")
################################################################

print("\n\nEx_5: A function that validates the dictionary")
def validate_dict(tuples_set, dictionary):
    tuple_keys = []
    flag = 0

    for tuple_i in tuples_set:
        tuple_keys.append(tuple_i[0])
    for key in dictionary.keys():
        if key not in tuple_keys:
            return False

    for tuple_i in tuples_set:
        if tuple_i[0] in dictionary.keys():
            words = dictionary[tuple_i[0]].split()
            print(words)
            if (words[0].startswith(tuple_i[1]) or tuple_i[1] == "") and (dictionary[tuple_i[0]].find(tuple_i[2])
                    not in (0, -1, len(dictionary[tuple_i[0]]) - len(tuple_i[2])) or tuple_i[2] == "") \
                    and (words[-1].endswith(tuple_i[3]) or tuple_i[3] == ""):
                flag += 1
    print("Number of correct keys:", flag)
    if flag == len(dictionary):
        return True
    else:
        return False

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key3", "this", "", "")}
d = {
     "key1": "come inside, it's too cold out",
     "key3": "this is not valid"
    }
print(validate_dict(s, d))
################################################################

print("\n\nEx_6: A function that returns a tuple of unique and duplicate elements")
def unique_and_duplicate(given_list):
    unique = 0
    duplicate_list = []
    for element in given_list:
        count = given_list.count(element)
        if count == 1:
            unique += 1
        else:
            duplicate_list.append(element)

    duplicate = len(set(duplicate_list))
    # print(duplicate_list)
    # print(set(duplicate_list))
    unique_and_duplicate_tuple = tuple((unique, duplicate))
    print(unique_and_duplicate_tuple)

list_1 = [1, 2, "a", 2, "ab", "a", 2, 2]
unique_and_duplicate(list_1)
################################################################

print("\n\nEx_7: A function that returns a dictionary with the operations from all sets")
def set_operations(set_1, set_2, set_3):
    dictionary = {}
    set_list = [set_1, set_2, set_3]
    print(set_list)

    for i in range(0, len(set_list) - 1):
        for j in range(i+1, len(set_list)):
            if set_list[i] != set_list[j]:
                dictionary[str(set_list[i]) + " | " + str(set_list[j])] = set_list[i].union(set_list[j])
                dictionary[str(set_list[i]) + " & " + str(set_list[j])] = set_list[i].intersection(set_list[j])
                dictionary[str(set_list[i]) + " - " + str(set_list[j])] = set_list[i].difference(set_list[j])
                dictionary[str(set_list[j]) + " - " + str(set_list[i])] = set_list[j].difference(set_list[i])
    print(dictionary, sep='\n')


set1 = {1, 2}
set2 = {2, 3}
set3 = {2, 3, 4, 5}
set4 = {6, 7, 8}
set_operations(set1, set2, set3)
################################################################

print("\n\nEx_8: A function that returns the list of objects obtained by mapping")
def loop(mapping):
    visited_keys = []
    current_key = "start"
    while current_key not in visited_keys:
        visited_keys.append(current_key)
        current_value = mapping[current_key]
        current_key = current_value

    print(visited_keys)


loop_dictionary = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
loop(loop_dictionary)
################################################################

print("\n\nEx_9: A function that will return the number of positional arguments found among keyword arguments values")
def positional_argument_no(*positional_args, **keyword_args):
    counter = 0

    for key_arg in keyword_args.values():
        for pos_arg in positional_args:
            if key_arg == pos_arg:
                counter += 1
                continue
    print(counter)

positional_argument_no(1, 2, 3, 4, x=1, y=2, z=3, w=5)
