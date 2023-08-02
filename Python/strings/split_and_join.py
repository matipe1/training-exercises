# A basic Python code about Split and Join
def split_and_join(string):
    conversion = string.split(" ")
    return "-".join(conversion)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)