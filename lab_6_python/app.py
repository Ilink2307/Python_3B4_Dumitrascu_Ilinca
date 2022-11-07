import utils

print("Ex1b: ")
flag = 1
while flag != 0:
    x = input("Enter a number or q to quit: ")
    if x == "q":
        flag = 0
    else:
        int_number = int(x)
        print(utils.process_item(int_number))
