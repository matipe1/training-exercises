# Print all the possible solutions

def permutation(x, y, z, n):
    # All the possible solutions are:
    # my_comprehension_list = [list([i, j, k]) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    my_comprehension_list = [
        [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if not i + j + k == n
    ]

    return my_comprehension_list


if __name__ == '__main__':
    a = int(input("valor a: "))
    b = int(input("valor b: "))
    c = int(input("valor c: "))
    d = int(input("valor d: "))

    print(permutation(a, b, c, d))
