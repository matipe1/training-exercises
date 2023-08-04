def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = size
    letters = [alphabet[i] for i in range(int(n))]

    letters.reverse()
    complete = []

    for i in range(len(letters)):
        middle = letters[i]
        first = [letters[j] for j in range(i)]
        second = [letters[k] for k in range(i)]
        second.reverse()

        complete.extend(first)
        complete.extend(middle)
        complete.extend(second)

        print(('-'.join(complete)).center((((int(n) - 1) * 4) + 1), '-'))  # How it looks in each line

        if not i == len(letters) - 1:
            complete = []  # Delete

    complete_2 = complete

    complete_2.reverse()
    letters.reverse()

    for j in range(1, len(letters)):
        middle = letters[j]
        # print(('-'.join(complete_2)).center((((int(n) - 1) * 4) + 1), '-'))
        left = complete[0:len(letters) - 1 - j]
        # print('left', left)
        right = complete_2[0: len(letters) - 1 - j]
        right.reverse()
        # print('right', right)
        print(('-'.join(left)).rjust(((int(n) - 1) * 2) - 1, '-') + middle.center(3, '-') + ('-'.join(right)).ljust(((int(n) - 1) * 2) - 1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
