import numpy as np

EXP = np.e

class NotPositiveInt(ValueError):
    def __init__(self, message):
        self.message = message
        super.__init__(self.message)


def get_fibonacci(n):

    if n <= 0 or n != int(n):
        raise NotPositiveInt('Input n must be a positive integer.')

    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        r_list = [1, 1]
        for idx in range(2, n):
            r_list.append(r_list[-1] + r_list[-2])

        return r_list

def get_factorial(n):
    if n <= 0 or n != int(n):
        raise NotPositiveInt('Input n must be a positive integer.')

    if n == 1:
        return [1]
    else:
        r_list = [1]
        for idx in range(1, n):
            r_list.append(r_list[-1] * (idx+1))
        return r_list
