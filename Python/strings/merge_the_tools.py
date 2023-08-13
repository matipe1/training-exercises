def merge_the_tools(string, k):

    split_list = [string[i:i + k] for i in range(0, len(string), k)]
    for i in split_list:
        elements = ''
        for j in i:
            if j not in elements:
                elements += j
        print(elements)
        elements = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)