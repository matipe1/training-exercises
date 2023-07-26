if __name__ == '__main__':
    n = int(input('Amount of lines: '))
    t = list()
    my_dict = {'insert': t.insert, 'remove': t.remove, 'append': t.append,
               'sort': t.sort, 'print': print, 'pop': t.pop, 'reverse': t.reverse}

    for _ in range(n):
        command = input().split()

        # Principal variables
        func = my_dict.get(command[0])
        arguments = tuple(map(int, command[1:]))
        if len(command) > 1:
            func(*arguments)
        elif command[0] == 'print':
            func(t)
        else:
            func()
