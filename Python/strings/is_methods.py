if __name__ == '__main__':
    s = input()
    properties = {
        'alnum': False, 'al': False, 'dig': False, 'low': False, 'upp': False
    }
    for i in s:
        if i.isalnum():
            properties["alnum"] = True
        if i.isalpha():
            properties["al"] = True
        if i.isdigit():
            properties["dig"] = True
        if i.islower():
            properties["low"] = True
        if i.isupper():
            properties["upp"] = True

    for i in properties:
        print(properties[i])
