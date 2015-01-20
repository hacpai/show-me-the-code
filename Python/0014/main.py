def isPrime ( n ):
    for i in range(2, n ):
        if n % i == 0:
            return False
    return True

def prime( n ):
    lst = [] 
    for i in range( 2, n ):
        if isPrime(i) == True:
            lst.append(i)

    return lst

def bi_search( lst, start, stop, key ):
    mid = ( start + stop ) / 2
    if lst[mid] == key:
        return mid
    elif start >= stop:
        return -1
    elif lst[mid] > key:
        return bi_search( lst, start, mid-1, key )
    else:
        return bi_search( lst, mid+1, stop, key )


#lst = [2, 3, 5, 7]


def isPrime ( n ):
    for i in range(2, n ):
        if n % i == 0:
            return False
    return True

def prime( n ):
    lst = [] 
    for i in range( 2, n ):
        if isPrime(i) == True:
            lst.append(i)

    return lst

def bi_search( lst, start, stop, key ):
    mid = ( start + stop ) / 2
    if lst[mid] == key:
        return mid
    elif start >= stop:
        return -1
    elif lst[mid] > key:
        return bi_search( lst, start, mid-1, key )
    else:
        return bi_search( lst, mid+1, stop, key )


#lst = [2, 3, 5, 7]

#print bi_search( lst, 4 )

n = int( raw_input() )

lst = prime( n )

start = 0
stop = len(lst) - 1


for key in iter( raw_input, '' ):
    key = int(key)
    print bi_search( lst, start, stop, key )
