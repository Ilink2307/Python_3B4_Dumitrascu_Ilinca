import re
################################################################

print("\nEx_1: A function that extracts the words from a given text as a parameter")
def find_words(string):
    return re.split(r"\W", string)

print(find_words("Color from pixel 20,30 is 123"))
################################################################

print("\nEx_2: A function that returns x-length matching words")
def match_length(regex_string, text_string, length):
    final_list = []
    result = re.findall(regex_string, text_string)
    for element in result:
        if len(element) == length:
            final_list.append(element)
    return final_list

print(match_length(r"\w+", "aaa-sasa  +6f..sad fdx ana", 3))
################################################################

print("\nEx_3: A function that returns a list of the strings that match on at least one regular expression")
def regex_list_function(string_list, regex_list):
    final_list = []

    for string in string_list:
        for pattern in regex_list:
            if re.search(pattern, string):
                final_list.append(string)

    return final_list

string_list_1 = ["aaa", "1020Ar", "..d12!", "a..a space !.."]
regex_list_1 = [r"\d+", r"\%", r"\*"]
print(regex_list_function(string_list_1, regex_list_1))
################################################################

print("\nEx_6: A function that returns censure words with vowels")

def check(string):

    regex_begin = '^[aeiouAEIOU][A-Za-z0-9_]*'
    regex_end = '[A-Za-z0-9_]*[aeiouAEIOU]$'
    if re.search(regex_begin, string) or re.search(regex_end, string):
        return True
    else:
        return False

def censor(word):
    censored_word = ''
    for index, char in enumerate(str(word)):
        if index % 2 == 1:
            censored_word += '*'
        else:
            censored_word += char

    return censored_word

def censor_vowels(text):

    final_list = []
    word_list = text.split()

    for word in word_list:
        if check(word):
            censor(word)
            final_list.append(censor(word))

    return final_list

print(censor_vowels("aaa dddd adddd dda ..a."))

