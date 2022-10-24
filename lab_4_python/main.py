from xml.etree.ElementTree import Element, SubElement, tostring

print("\nEx_1: A function that will receives two lists and returns a list of sets")
def set_list(list_a, list_b):
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
print(set_list(a_list, b_list))
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
    # d1_keys = set(dict_1.keys())
    # d2_keys = set(dict_2.keys())
    if len(dict_1) != len(dict_2):
        print("False")

    else:
        flag = 0
        for i in dict_1:
            if dict_1.get(i) != dict_2.get(i):
                flag = 1
                break
        if flag == 0:
            print("True")
        else:
            print("False")
    print("TUDORRR!!")

dictionary_1 = dict(a=1, b=2, c=dict(d=1, f=1), d=list[1, 2])
dictionary_2 = dict(a=1, b=2, c=dict(d=1, f="sa"), d=list[1, 2])
compare_dictionaries(dictionary_1, dictionary_2)
################################################################

print("\n\nEx_4: A function that compares two dictionaries")
#def build_xml_element(tag, content, key_value1, key_value2, key_value3):

#     root = Element('root')
#     child = SubElement(root, "child")
#     child.text = "I am a child"
#
#     print(tostring(root))
#
# href = " http://python.org "
# _class =" my-link "
# id= " some_id "
# build_xml_element ("a", "Hello there", href, _class, id)

# "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
################################################################

print("\n\nEx_5: A function that validates the dictionary")
def validate_dict(tuples_set, dictionary):
    tuple_keys = []
    flag = 0

    for tuple in tuples_set:
        tuple_keys.append(tuple[0])
    for key in dictionary.keys():
        if key not in tuple_keys:
            return False

    for tuple in tuples_set:
        if tuple[0] in dictionary.keys():
            words = dictionary[tuple[0]].split()
            print(words)
            if (tuple[1] == words[0] or tuple[1] == "") and (tuple[2] in words or tuple[2] == "") and (tuple[3] == words[-1] or tuple[3] == ""):
                flag += 1
    print("Number of correct keys:", flag)
    if flag == len(dictionary):
        return True
    else:
        return False

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key3", "this", "", "")}
d = {
     "key1": "come inside , it's too cold out",
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

