#include <stdio.h>


int isPrime ( int n );
void solutDivisor ( int n );

int main () 
{
    int n;
    scanf ( "%d", &n );
    /*n = 18;*/
    /*solutDivisor( n );*/
    /*printf ( "%d", test );*/
    if ( isPrime( n ) == 1 )
    {
        printf ( "%d=%d", n, n );
    }
    else
    {
        solutDivisor ( n );
    }
    return 0;
}

int isPrime ( int n )
{
    int is_prime = 1;
    for ( int i = 2; i < n; i++ )
    {
        if ( n % i == 0 )
        {
            is_prime = 0;
            break;
        }
    }
    return is_prime;
}

void solutDivisor ( int n )
{
    
    int i = 2;
    printf ( "%d=", n );
    while ( n != 1 )
    {
        if ( n % i == 0 )
        {
            n /= i;
            printf ( "%d", i );
                if ( n != 1 )
                {
                    printf ( "x" );
                }
            continue;
        }
        i++;
    }
}
