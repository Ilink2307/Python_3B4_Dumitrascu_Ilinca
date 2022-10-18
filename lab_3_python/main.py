print("\nEx_1: A function to return a list of the first n numbers in the Fibonacci string.")
def fibo_list(n):
    number_list = [0, 1]

    if n == 0:
        print("[]")
    elif n == 1:
        print("[0]")
    else:
        for i in range(2, n):
            number_list.append(number_list[i - 2] + number_list[i - 1])

        print(number_list)

fibo_list(3)
################################################################

print("\n\nEx_2: A function that receives a list of numbers and returns a list of the prime numbers found in it.")
def is_prime(x):
    ok = False

    if x <= 1:
        return 0
    else:
        for i in range(2, x//2):
            if (x % i) == 0:
                ok = True
                break
    if ok:
        return 0
    else:
        return 1

def prime_list(given_list):
    list_of_prime = []

    for i in range(0, len(given_list)):
        if is_prime(given_list[i]):
            list_of_prime.append(given_list[i])
    print(list_of_prime)

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 99, 97]
prime_list(number_list)
################################################################

print("\n\nEx_3: A function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)")
def list_operations(list1, list2):

    reunion = list(set(list1).union(list2))
    intersection = list(set(list1).intersection(list2))
    list1_list2 = list(set(list1).difference(list2))
    list2_list1 = list(set(list2).difference(list1))

    print("a reunited with b: ", reunion,
          "\na intersected with b: ", intersection,
          "\na - b: ", list1_list2,
          "\nb - a: ", list2_list1)

# a_list = [0, 1, 2, 3, 4, 5, 6, 7]
# b_list = [4, 5, 6, 7, 8, 9, 10]
a_list = [0, 1, 2, 3, 4, 5, 6, 7, "False"]
b_list = [6, 7, 8, 9, "True", "False"]

list_operations(a_list, b_list)
################################################################

print("\n\nEx_4: A function that composes the song")
def compose(notes_list, move_list, start):
    final_list = [notes_list[start]]
    last_position = start
    for i in range(0, len(move_list)):
        final_list.append(notes_list[(last_position + move_list[i]) % len(notes_list)])
        last_position = last_position + move_list[i]

    print(final_list)

compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
################################################################

print("\n\nEx_5: A function that replaces all the elements under the main diagonal with 0 ")
def replace_with_0(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    print(rows, columns)
    for i in range(0, rows):
        for j in range(0, columns):
            if i > j:
                matrix[i][j] = 0
    for i in range(0, rows):
        for j in range(0, columns):
            print(matrix[i][j], end = " ")
        print()

a = [[4, 1, 4, 2, 3],
    [4, 2, 9, 1, 5],
    [2, 2, 1, 6, 3],
    [3, 4, 5, 3, 5]]

b = [[4, 1, 4],
    [4, 2, 9],
    [2, 2, 1],
    [3, 4, 5]]
#replace_with_0(a)
replace_with_0(b)
################################################################
print("\n\nEx_6: A function that returns a list containing the items that appear exactly x times")
def frequency_list(list1, list2, list3, list4, list5, x):
    extended_list = []
    final_list = []
    [extended_list.extend(i) for i in (list1, list2, list3, list4, list5)]
    print(extended_list)
    for i in extended_list:
        if extended_list.count(i) == x:
            final_list.append(i)
    print(list(set(final_list)))

frequency_list([1,2,3], [2,3,4], [4,5,6], [4,1, "test"], [4, 3, "test"], 2)

################################################################

print("\n\nEx_7: A function that returns a tuple: number of palindromes and the greatest palindrome")
def is_palindrome(n):
    if 0 <= n < 10:
        return True

    if n < 0:
        n = (-n)

    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n //= 10
    if temp == rev:
        return True
    else:
        return False

def palindrome_tuple(number_list):
    palindrome_no = 0
    max_palindrome = 0
    for i in range(0, len(number_list)):
        if is_palindrome(number_list[i]):
            palindrome_no += 1
            if number_list[i] > max_palindrome:
                max_palindrome = number_list[i]

    this_tuple = tuple((palindrome_no, max_palindrome))
    print(this_tuple)

palindrome_tuple([121, 54, 65, 666, 7564, 343, 8])
################################################################

print("\n\nEx_8: A function that returns the characters that have the ASCII code divisible by x (or not)")
def ascii_div(string_list, num=1, flag=True):
    final_list = []
    character_list = []
    for string_index in range(0, len(string_list)):
        character_list.clear()
        for character_index in string_list[string_index]:
            if (flag == True and ord(character_index) % num == 0) or (flag == False and ord(character_index) % num != 0):
                character_list.append(character_index)
        final_list.append(list(character_list))

    print(final_list)

ascii_div(["test", "hello", "lab002"], 2, False)
################################################################

print("\n\nEx_9: A function that returns the characters that have the ASCII code divisible by x (or not)")
