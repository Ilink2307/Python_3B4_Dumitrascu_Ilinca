given_string = input("Enter a string: ")
vowel_no = 0

for i in given_string:
    if(i in "aeiouAEIOU"):
        vowel_no = vowel_no+1

print(vowel_no)