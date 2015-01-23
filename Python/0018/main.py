def is_palin_num( num ):
    num = str(num)
    for i in range( len(num)/2 ):
        if num[i] != num[-1-i]:
            return False
            
    return True
 
def gener_max_palin_num( n ):
    flag = 0
    for i in range( 10**(n)-1, 10 ** (n-1)-1, -1 ):
        for j in range( 10**(n)-1, 10 ** (n-1)-1, -1 ):
            if is_palin_num( i * j  ) == True:
                if flag == 0:
                    first_pali = i * j
                    flag = 1
                    break
                else:
                    if first_pali > i * j:
                        ret = first_pali
                    else:
                        ret = i * j
                    return ret
 
n = int( raw_input() )
print gener_max_palin_num( n )
