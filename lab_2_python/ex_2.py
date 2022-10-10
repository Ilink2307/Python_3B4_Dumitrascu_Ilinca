
# vowel_no = 0
#
# for i in given_string:
#     if(i in "aeiouAEIOU"):
#         vowel_no = vowel_no+1
#
# print(vowel_no)

# --4-- Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
# given_string = input("Enter a string: ")
# final_string = ''
# if given_string[0].isupper():
#     final_string += given_string[0].lower()
# else:
#     final_string += given_string[0]
#
# for i in range(1, len(given_string)):
#     if given_string[i].isupper():
#         final_string += '_' + given_string[i].lower()
#     elif given_string[i] == ' ' or given_string[i] == '_':
#         final_string += '_'
#     else:
#         final_string += given_string[i]
#
# print(final_string)

# --5--  the string obtained by going through the matrix in spiral order
# def spiral_matrix(a, b, n):
#
#     if a >= n or b >= n:
#         return
#
#     for i in range(a, n):
#         print(matrix[a][i], end=" ")
#
#     for j in range(a + 1, n):
#         print(matrix[j][n - 1], end=" ")
#
#     if (n - 1) != a:
#         for k in range(n - 2, b - 1, -1):
#             print(matrix[n - 1][k], end=" ")
#
#     if (n - 1) != b:
#         for p in range(n - 2, a, -1):
#             print(matrix[p][b], end=" ")
#
#     spiral_matrix(a + 1, b + 1, n - 1)
#
#
# n = int(input("Enter the number of rows and columns: "))
#
# matrix = []
# print("Write the matrix: ")
# for i in range(n):
#     m = []
#     for j in range(n):
#         m.append(input())
#     matrix.append(m)
#
# spiral_matrix(0, 0, n)

# --6-- Write a function that validates if a number is a palindrome.
# def isPal(n):
#     if 0 <= n < 10:
#         return True
#
#     if n < 0:
#         n = (-n)
#
#     temp = n
#     rev = 0
#     while n > 0:
#         dig = n % 10
#         rev = rev * 10 + dig
#         n = n // 10
#     if temp == rev:
#         return True
#     else:
#         return False
#
#
# num = int(input())
# if isPal(num):
#     print("Yes")
# else:
#     print("No")

# --7-- Write a function that extract a number from a text. first number that is found.
# given_string = input("Enter a string: ")
# final_string = ''
#
# for i in range(0, len(given_string)):
#     if given_string[i].isdigit():
#         final_string += given_string[i]
#     elif not given_string[i].isdigit() and len(final_string) > 1:
#         break
#
# print(final_string)


# --8-- Write a function that counts how many bits with value 1 a number has.
# n = input("Enter a number: ")
# n = int(n)
# print("The binary form of the number is: ")
# binary_form = bin(n)[2:]
# print(binary_form)
# ones = 0
# for i in range(0, len(binary_form)):
#     if binary_form[i] == '1':
#         ones = ones + 1
# print("There are ", ones, " bits with value 1")

# --10-- Write a function that counts how many words exists in a text.
# given_string = input("Enter a string: ")
# words = 0
# if given_string[0] or given_string[-1]:
#     words = 0
# for i in range(1, len(given_string)-1):
#     if given_string[i] == ' ':
#         words = words + 1
# print(words + 1)

# --9-- Write a functions that determine the most common letter in a string.
# given_string = input("Enter a string: ")
# given_string = given_string.lower()
# fr = [0 for i in range(26)]
# max_count = 0
# letter = ''
# for i in given_string:
#     fr[ord(i)-97] += 1
# print(fr)
#
# for j in range(0, 26):
#     if fr[j] > max_count:
#         max_count = fr[j]
#         letter = j
# print(max_count, chr(letter + 97))
