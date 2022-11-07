# import utils
# import app
from functools import reduce
################################################################

print("\nEx_2a: A function that returns the sum of the keyword arguments")
def sum_function(*args, **keyword_args):
    args_sum = 0
    for keyword in keyword_args.values():
        args_sum += keyword
    return args_sum

print(sum_function(1, 2, c=3, d=4))

print("\nEx_2b: Lambda function: ")

def sum_lambda_function(*args, **keyword_args):
    args_sum = reduce((lambda x, y: x + y), keyword_args.values())
    return args_sum

print(sum_lambda_function(1, 2, c=3, d=4))
################################################################

print("\nEx_3a: A function that returns the vowels in a string")
def vowel_function(string):
    vowel_list = []
    for character in string:
        if character in "aeiouAEIOU":
            vowel_list.append(character)
    return vowel_list

given_string = "Programming in Python is fun"
print(vowel_function(given_string))

print("\nEx_3b: Lambda function: ")
def vowel_lambda_function(string):
    vowel_list = []
    vowel_list.append(lambda character: string if(character in "aeiouAEIOU") else '')

    return "!!!!vowel_list!!!!!!!!!!!!!!!!!!"

print(vowel_lambda_function(given_string))

print("\nEx3c: List comprehension: ")
def vowel_list_comprehension(string):
    vowel_list = [character for character in string if character in "aeiouAEIOU"]
    return vowel_list

print(vowel_list_comprehension(given_string))
################################################################

print("\nEx_4: A function that returns the specified dictionaries")
def dictionary_list(*args, **keyword_args):
    final_list = []

    for argument in args:
        key_no = 0
        string_keys = 0
        if type(argument) is dict:
            for key in argument.keys():
                if type(key) is str and len(key) >= 3:
                    string_keys += 1
                key_no += 1
            if key_no >= 2 and string_keys >= 1:
                final_list.append(argument)
    print("MAI FAC UN FOR PT CEALALTA SAU POT ALTFEL??????")
    # key_no = 0
    # for keyword in keyword_args.values():
    #     if type(keyword) is dict:
    #         for key in keyword.keys():
    #             key_no += 1
    #         if key_no >= 2:
    #             print(keyword)
    #             final_list.append(keyword)
    return final_list

print(dictionary_list(
        {1: 2, 3: 4, 5: 6},
        {'a': 5, 'b': 7, 'c': 'e'},
        {2: 3},
        [1, 2, 3],
        {'abc': 4, 'def': 5},
        3764,
        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
        test={1: 1, 'test': True}
    ))
################################################################

print("\nEx_5: A function that returns a list containing all the numbers found in the given list.")
def number_list(given_list):
    final_list = []
    for element in given_list:
        if type(element) is int or type(element) is float:
            final_list.append(element)
    return final_list

print(number_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
################################################################

print("\nEx_6: A function that returns a list containing all the numbers found in the given list.")
def group_even_odd(given_list):
    tuple_list = []
    even_list = []
    odd_list = []
    for element in given_list:
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)
    for i in range(0, len(given_list)//2):
        tuple_list.append(tuple((even_list[i], odd_list[i])))
    return tuple_list

print(group_even_odd([1, 3, 5, 2, 8, 7, 4, 10, 9]))
################################################################

print("\nEx_7: A function that returns a list containing all the numbers found in the given list.")
def sum_digits(x):

    return sum(map(int, str(x)))

def process(**keyword_args):
    final_list = []
    offset = keyword_args.get("offset")
    limit = keyword_args.get("limit")
    fibo_1 = 0
    fibo_2 = 1

    for terms in range(2, 1000):
        counter = 0
        fibo_term = fibo_1 + fibo_2
        for function in keyword_args.get("filters"):
            if function(fibo_term):
                counter += 1
        if counter == len(keyword_args.get("filters")):
            final_list.append(fibo_term)
        fibo_1 = fibo_2
        fibo_2 = fibo_term

    print(final_list)

    final_list = final_list[offset:]
    final_list = final_list[0:limit]
    return final_list

print(process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=5,
        offset=3
    ))
################################################################

print("\nEx_8: A function that ")


################################################################

print("\nEx_9: A function that ")
