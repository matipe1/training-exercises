def door_mat(first, second):
    middle = (int(first) // 2)
    obj = '.|.'
    count = -1

    for i in range(int(first)):
        if i < middle:
            print((obj * i + obj + obj * i).center(int(second), '-'))
            count += 1
        if i == middle:
            print('WELCOME'.center(int(second), '-'))
        if i > middle:
            pass
            print((obj * count + obj + obj * count).center(int(second), '-'))
            count -= 1


if __name__ == '__main__':
    vert, horiz = input().split()
    door_mat(vert, horiz)
