if __name__ == '__main__':
    N = int(input())
    my_list = list()

    for _ in range(N):
        command, *b = input().split()
        param = list(map(int, b))
        my_list.append([command, param])

    print(my_list)