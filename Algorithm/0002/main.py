def reverse_list(t, start, end):
    """Computes invert list using Decrease-and-Conquer method.

    t: list
    start: first index
    end: last index
    """
    if start < end:
        t[start], t[end] = t[end], t[start]
        return reverse_list(t, start+1, end-1)


def sum_list(t, low, high):
    """Computes sum of list using Divide-and-conquer method.

    t: list
    low: first index
    high = last index
    """
    if low == high:
        return t[low]
    midle = (low + high) / 2
    return sum_list(t, low, midle) + sum_list(t, midle+1, high)


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    reverse_list(t, 0, len(t)-1)
    print sum_list(t, 0, len(t)-1)
    print t
