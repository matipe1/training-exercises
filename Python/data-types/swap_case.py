def swap_case(s):
    sentence = str()
    for n in s:
        if n in 'abcdefghijklmnñopqrstuvwxyz':
            sentence += n.upper()
        elif n in 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ':
            sentence += n.lower()
        else:
            sentence += n
    return sentence


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)