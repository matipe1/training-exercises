def print_formatted(number):
    decimal = [n for n in range(1, number + 1)]
    octal = [oct(n) for n in range(1, number + 1)]
    hexadecimal = [hex(n).upper() for n in range(1, number + 1)]
    binary = [bin(n) for n in range(1, number + 1)]

    space_padded = len(binary[-1]) - 2

    for i in range(number):
        print(f'{decimal[i]}'.rjust(space_padded), f'{octal[i][2:]}'.rjust(space_padded),
              f'{hexadecimal[i][2:]}'.rjust(space_padded), f'{binary[i][2:]}'.rjust(space_padded))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
