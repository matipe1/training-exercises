def count_substring(string, sub_string):
    n = 0

    for i in range(0, len(string)):
        looking = string[i:len(sub_string) + i]  # Important to understand
        if looking == sub_string:
            n += 1

    return n


if __name__ == '__main__':
    strg = input().strip()
    sub_strg = input().strip()

    count = count_substring(strg, sub_strg)
    print(count)
