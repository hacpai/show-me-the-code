#include <stdio.h>
#include <math.h>

int main()
{
    int num;
    scanf( "%d", &num );
    int mark = 0;
    int num_read;

    if ( num < 0 )
    {
        printf ( "fu " );
        num = -num;
    }
    int num_ori = num;
    while ( num > 9 )
    {
        num /= 10;
        mark++;
    }
    for ( int i = mark; i >= 0; i-- )
    {
        num_read = num_ori / pow( 10, i );
        switch ( num_read )
        {
            case 0:
                printf ( "ling" );
                break;
            case 1:
                printf ( "yi" );
                break;
            case 2:
                printf ( "er" );
                break;
            case 3:
                printf ( "san" );
                break;
            case 4:
                printf ( "si" );
                break;
            case 5:
                printf ( "wu" );
                break;
            case 6:
                printf ( "liu" );
                break;
            case 7:
                printf ( "qi" );
                break;
            case 8:
                printf ( "ba" );
                break;
            case 9:
                printf ( "jiu" );
                break;
        }
        if ( i > 0 )
        {
            printf ( " " );
        }
        num_ori = num_ori %  (int)pow( 10, i );
    }


    return 0;
}
