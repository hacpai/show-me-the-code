#include <stdio.h>

int isCompNum ( int n )
{
    int sum = 0;
    int is_comp_num;
    for ( int i = 1; i < n; i++ )    
    {
       if ( n % i == 0 )
       {
           sum += i;
       }
    }

    if ( n == sum )
    {
        is_comp_num = 1;
    }
    else
    {
        is_comp_num = 0;
    }
    return is_comp_num;
}

int main ()
{

    int n, m;
    scanf( "%d %d", &n, &m );
/*    int n = 10;*/

    /*int test = isCompNum ( n );*/
/*[>    p<]rintf ( "%d", test );*/

    int flag = 0;
    int count = 0;
    for ( int i = n; i < m; i++ )
    {
        if ( isCompNum( i ) == 1 )
        {
            count++;
            flag = 1;
            if ( count == 1 )
            {
                printf ( "%d", i );
            }
            else
            {
                printf ( " %d", i );
            }
        }
    }
    if ( flag == 0 )
    {
        printf ( "\n" );
    }
        
    return 0;
}
