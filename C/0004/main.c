#include <stdio.h>
#include <math.h>
int main ()
{
    int x;
    int digit;
    scanf ( "%d", &x );
    int count = 0;
    int ret = 0; 
    int sum = 0;
    while ( x > 0 )
    {
        digit = x % 10;
        count ++;
        if ( digit % 2 == count % 2 )
        {
            ret = 1 * pow(2, count - 1);
            sum += ret;
        }
        x /= 10;
    }

    printf ( "%d", sum );
    
    return 0;
}
