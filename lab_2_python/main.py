print("Enter the number of the exercise you want: ")
ex_nr = int(input())

if ex_nr == 1:
    def find_gcd(x, y):
        if x == 0 and y == 0:
            return 0
        elif y == 0:
            return x
        else:
            return find_gcd(y, x % y)

    number_list = list(map(int, input("The script will compute the gcd of the following numbers: ").split()))

    num1 = number_list[0]
    num2 = number_list[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(number_list)):
        gcd = find_gcd(gcd, number_list[i])

    print(gcd)


elif ex_nr == 2:
    given_string = input("Enter a string: ")
    vowel_no = 0

    for i in given_string:
        if i in "aeiouAEIOU":
            vowel_no = vowel_no+1

    print("The number of vowels in the string: ", vowel_no)


elif ex_nr == 3:
    def find_occurrences(substring, main_string):
        ss = len(substring)
        ms = len(main_string)
        occ_no = 0

        for i in range(ms - ss + 1):
            j = 0
            while j < ss:
                if main_string[i + j] != substring[j]:
                    break
                j += 1

            if j == ss:
                occ_no += 1

        return occ_no

    text = "abdc"
    pattern = "ab"
    print(find_occurrences(pattern, text))


elif ex_nr == 4:
    given_string = input("Enter a string: ")
    final_string = ''
    if given_string[0].isupper():
        final_string += given_string[0].lower()
    else:
        final_string += given_string[0]

    for i in range(1, len(given_string)):
        if given_string[i].isupper():
            final_string += '_' + given_string[i].lower()
        elif given_string[i] == ' ' or given_string[i] == '_':
            final_string += '_'
        else:
            final_string += given_string[i]

    print(final_string)


elif ex_nr == 5:
    def spiral_matrix(a, b, n):

        if a >= n or b >= n:
            return

        for i in range(a, n):
            print(matrix[a][i], end=" ")

        for j in range(a + 1, n):
            print(matrix[j][n - 1], end=" ")

        if (n - 1) != a:
            for k in range(n - 2, b - 1, -1):
                print(matrix[n - 1][k], end=" ")

        if (n - 1) != b:
            for p in range(n - 2, a, -1):
                print(matrix[p][b], end=" ")

        spiral_matrix(a + 1, b + 1, n - 1)

    n = int(input("Enter the number of rows and columns: "))

    matrix = []
    print("Write the matrix: ")
    for i in range(n):
        m = []
        for j in range(n):
            m.append(input())
        matrix.append(m)

    spiral_matrix(0, 0, n)


elif ex_nr == 6:
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

    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print("Yes")
    else:
        print("No")


elif ex_nr == 7:
    given_string = input("Enter a string: ")
    final_string = ''

    for i in range(0, len(given_string)):
        if given_string[i].isdigit():
            final_string += given_string[i]
        elif not given_string[i].isdigit() and len(final_string) > 1:
            break

    print(final_string)


elif ex_nr == 8:
    n = input("Enter a number: ")
    n = int(n)
    print("The binary form of the number is: ")
    binary_form = bin(n)[2:]
    print(binary_form)
    ones = 0
    for i in range(0, len(binary_form)):
        if binary_form[i] == '1':
            ones = ones + 1
    print("There are ", ones, " bits with value 1")


elif ex_nr == 9:
    given_string = input("Enter a string: ")
    given_string = given_string.lower()
    fr = [0 for i in range(27)]
    max_count = 0
    letter = ''
    for i in given_string:
        fr[ord(i) - 97] += 1
    print(fr)

    for j in range(0, 26):
        if fr[j] > max_count:
            max_count = fr[j]
            letter = j
    print(max_count, chr(letter + 97))


elif ex_nr == 10:
    given_string = input("Enter a string: ")
    words = 0
    if given_string[0] or given_string[-1]:
        words = 0
    for i in range(1, len(given_string) - 1):
        if given_string[i] == ' ':
            words = words + 1
    print(words + 1)
