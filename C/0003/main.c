#include <stdio.h>
int main ()
{
    int x;
    int odd = 0, even = 0;
    while ( scanf( "%d", &x ) != EOF && x != -1 )
    {
        if ( x % 2 == 1 )
        {
            odd ++;
        }
        else
        {
            even ++;
        }
    }
    printf ( "%d %d", odd, even );
    return 0;
}
