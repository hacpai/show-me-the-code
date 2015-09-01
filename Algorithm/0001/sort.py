def insertion_sort(lst):
    """"Processes an element one by one.

    Compares sorted elements and move to right sort position
    until processes last element.
    """
    for i in range(1, len(lst)):
        current_value = lst[i]
        compares_index = i - 1
        while compares_index > -1 and lst[compares_index] > current_value:
            lst[compares_index+1] = lst[compares_index]
            compares_index -= 1
        lst[compares_index+1] = current_value


def selection_sort(lst):
    """Processes an element at a time.

    Find a minimum element in unsorted part and move it to sorted part.
    """
    for i in range(len(lst)-1):
        min_val_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_val_index]:
                min_val_index = j
        if min_val_index != i:
            lst[i], lst[min_val_index] = lst[min_val_index], lst[i]


def bubble_sort(lst):
    """Processes an element at a time.

    Swap a pair of adjacent element that inconformity sort requirements .
    until a pair of adjacent element don't swap.
    """
    for i in range(len(lst)-1):
        has_change = False
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                has_change = True
        if not has_change:
            break
