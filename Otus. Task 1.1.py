def exponentiation(k, *args):
    """ Raising numbers to the power of k """
    res = []
    for i in range(len(args)):
        num = int(args[i]) ** k
        res.append(num)

    args = list(args)
    print('List of arguments:', args)
    print('Numbers to the power of k =', k, ':', res)


exponentiation(3, 1, 2, 3, 4, 5, 6)
