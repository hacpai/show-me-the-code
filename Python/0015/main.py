def generLastRow( n ):
    lst = []
    if n == 1:
        lst.append( n )
        return lst
    elif n == 2:
        lst.insert( 0, 1 )
        lst.append( 1 )
        return lst
    else:
        pre_lst = generLastRow( n - 1 )
        for i in range( len(pre_lst) - 1 ):
            lst.append( pre_lst[i]+pre_lst[i+1] )

        lst.insert( 0, 1 )
        lst.append( 1 )

        return lst

def printLastRow( n ):
    lst = generLastRow( n )
    for i in range( len(lst) ):
        print lst[i],

def printSpace( n ):
    while n - 1 != 0:
        print "", 
        n -= 1
        
n = int( raw_input() )
space = n

#printSpace( n )

for i in range(1, n+1):
    printSpace( space )
    printLastRow(i)
    space -= 1
    print
