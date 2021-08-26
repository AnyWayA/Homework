def even(res, num):
    """ Search for even numbers """
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            res.append(num[i])
    print('chetnie: ', res)
    return res


def odd(res, num):
    """ Search for odd numbers """
    for i in range(len(num)):
        if int(num[i]) % 2 != 0:
            res.append(num[i])
    print('nechetnie: ', res)
    return res


def simple(res, num):
    """ Search for simple numbers """
    for i in range(len(num)):
        correct_num = True
        for x in range(2, num[i] - 1):
            if int(num[i]) % int(x) == 0:
                correct_num = False
        if correct_num:
            res.append(int(num[i]))
    print('simple: ', res)
    return res


def math(num, wtd):
    """ Selecting a list operation """
    res = []
    # num = list(input('Vvedite spisok : >>  '))
    if wtd == 'even':
        even(res, num)
    elif wtd == 'odd':
        odd(res, num)
    elif wtd == 'simple':
        simple(res, num)
    else:
        print('Wrong operation')


num = [17, 18, 19, 20, 21, 22]

math(num, 'simple')
