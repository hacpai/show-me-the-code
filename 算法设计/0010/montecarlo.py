import random
import math


def compute_pi(n):
    """Computes pi with Monte Carlo method.

    n: the number of iterations.
    """
    total = 0
    for i in xrange(n):
        x, y = random.random(), random.random()
        if math.sqrt(x**2 + y**2) < 1.0:
            total += 1

    return 4.0 * total / n


if __name__ == '__main__':
    n = raw_input('Please input the number of iterations: ')
    mypi = compute_pi(int(n))
    print 'Estimating pi with', n, 'iterations:', mypi
    print 'Value of math.pi is', math.pi
    print 'Error is', abs(math.pi - mypi) / math.pi
