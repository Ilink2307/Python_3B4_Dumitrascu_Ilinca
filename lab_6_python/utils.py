def is_prime(x):
    ok = False

    if x <= 1:
        return 0
    else:
        for i in range(2, x):
            if (x % i) == 0:
                ok = True
                break
    if ok:
        return 0
    else:
        return 1

def process_item(x):
    found = 0
    i = x + 1
    while found == 0:
        if is_prime(i):
            return i
        else:
            i += 1


if __name__ == "__main__":
    print(process_item(int(input("Enter a number: "))))
