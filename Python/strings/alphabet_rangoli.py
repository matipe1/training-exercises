def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabet[:size]
    complete = [letters[n] for n in range(size)]
    complete.reverse()
    complete.extend([letters[n] for n in range(1, size)])  # input(5): ['e', 'd', 'c', 'b', 'a', 'b', 'c', 'd', 'e']
    middle = ((size * 2) // 2) - 1

    for i in range(size * 2 - 1):

        if i < middle:
            left = complete[:i]
            right = complete[i::-1]
            middle_inside = [complete[i]]

            print(('-'.join(left + middle_inside + right[1:])).center(len(complete) * 2 - 1, '-'))

    print('-'.join(complete))

    for i in reversed(range(size * 2 - 1)):

        if i < middle:
            left = complete[:i]
            right = complete[i::-1]
            middle_inside = [complete[i]]

            print(('-'.join(left + middle_inside + right[1:])).center(len(complete) * 2 - 1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

