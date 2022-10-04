

def find_gcd(x, y):
    if (y == 0):
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
