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


text = "aaaa"
pattern = "aa"
print(find_occurrences(text, pattern))
