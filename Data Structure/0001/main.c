#include <stdio.h>
int main()
{
    int base, exp;
    scanf ( "%d %d", &base, &exp );
    if ( exp == 0 )
    {
        printf ( "%d %d", 0, 0 );
    }
    else
    {
        printf ( "%d %d", base*exp, exp-1 );
 
        while ( (scanf ( "%d %d", &base, &exp ) ) != EOF )
        {
            if ( exp == 0 )
            {
                ;
            }
            else
            {
                printf ( " %d %d", base*exp, exp-1 );
            }
        }  
    }
 
    return 0;
}
