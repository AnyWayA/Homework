from time import time


def decorator(func):
    """ Wrapper for the function """
    def timing_func(*args):
        """ Counting the time of process """
        start = time()
        res = func(*args)
        end = time()
        time_res = int(end) - int(start)
        print('Time =', time_res, 's')
        return res
    return timing_func


@decorator
def exponentiation(*args, k=1000000):
    """ Raising numbers to the power of k """
    res = []
    for i in range(len(args)):
        num = int(args[i]) ** k
        res.append(num)
    print('List of arguments:', args)
    return res


exponentiation(27, 29, 31, 33)
