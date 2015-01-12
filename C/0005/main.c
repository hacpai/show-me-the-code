#include <stdio.h>

int main()
{
    
    int count = 0;
    int i = 2;
    int m, n;
    int sum = 0;
    scanf ( "%d %d", &n, &m );

    while ( count < m )
    {
        int flag = 1;
        for ( int j = 2; j < i; j++ )
        {
            if ( i % j == 0 )
            {
                flag = 0;
                break;
            }
        }
        if ( flag == 1 )
        {
            count++;
            if ( count >= n && count <= m )
            {
                sum += i;
            }
        }
        i++;
    }
    printf ( "%d", sum );

    return 0;
}
