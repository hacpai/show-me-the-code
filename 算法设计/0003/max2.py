def find_two_max_element_v1(t, low, high):
    """Find two max element in list using iteration.

    O(n) = 2n -3
    """
    max_element1_index, max_element2_index = low, low
    for i in range(low, len(t)):
        if t[max_element1_index] < t[i]:
            max_element1_index = i
    for i in range(low, max_element1_index):
        if t[max_element2_index] < t[i]:
            max_element2_index = i
    for i in range(max_element1_index + 1, len(t)):
        if t[max_element2_index] < t[i]:
            max_element2_index = i
    return max_element1_index, max_element2_index


def find_two_max_element_v2(t, low, high):
    """Find two max element in list using interation.

    O(n)best = n - 1; O(n)worst = 2n - 3
    """
    max_element1_index, max_element2_index = 0, 1
    for i in range(2, len(t)):
        if t[max_element2_index]< t[i]:
            max_element2_index = i
            if max_element1_index < max_element2_index:
                max_element1_index, max_element2_index = max_element2_index, max_element1_index
    return max_element1_index, max_element2_index


def find_two_max_element_v3(t, low, high):
    """Find two max element in list using Divide-and-conquer method."""
    if high - low == 1:
        if t[low] > t[low+1]:
            return low, low+1
        else:
            return low+1, low
    elif high - low == 2:
        if t[low] < t[low+1]:
            if t[low+1] < t[high]:
                return high, low+1
            else:
                return low+1, high
        else:
            if t[low+1] > t[high]:
                return low, low+1
            else:
                return high, low
    midle = (low + high) / 2
    l_max1, l_max2 = find_two_max_element_v3(t, low, midle)
    r_max1, r_max2 = find_two_max_element_v3(t, midle+1, high)
    if t[l_max1] > t[r_max1]:
        if t[l_max2] > t[r_max1]:
            max_element1_index, max_element2_index = l_max1, l_max2
        else:
            max_element1_index, max_element2_index = l_max1, r_max1
    else:
        if t[l_max1] < t[r_max2]:
            max_element1_index, max_element2_index = r_max1, r_max2
        else:
            max_element1_index, max_element2_index = r_max1, l_max1

    return max_element1_index, max_element2_index


if __name__ == '__main__':
    t = [2323, 324, 32, 355]
    print find_two_max_element_v3(t, 0, len(t)-1)

