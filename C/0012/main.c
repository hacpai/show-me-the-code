#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int chk_sum ( char sen[] );
int chk_val ( char sen[] );
int uct_to_bjt( char uct[] );

int main()
{
    char sen[255] = { '\0' };
    char uct[8] = { '\0' };
    scanf ( "%s", sen );

    while ( strcmp( sen, "END" ) != 0 )
    {
        if ( strncmp( sen, "$GPRMC,", 7 ) == 0 )
        {
/*            printf ( "chksum = %d, chkval = %d\n",*/
                    /*chk_sum( sen ), chk_val( sen ) );*/
            int chksum = chk_sum( sen );
            int chkval = chk_val( sen );
            char *loc = strchr( strchr( sen, ',' ) + 1, ',' ) + 1;
            if ( chksum == chkval && *loc == 'A' )
            {
                strncpy( uct, ( strchr( sen, ',' ) + 1 ), 6 );
            }
        }
        scanf ( "%s", sen );
    }
    int bjt = uct_to_bjt( uct );
    printf( "%02d:%02d:%02d", bjt/10000, bjt/100%100, bjt%100 );

    return 0;
}

int chk_sum ( char sen[] )
{
    int i, xor;
    for ( i = 2, xor = sen[1]; sen[i] != '*'; i++ )
    {
        xor ^= sen[i];
    }
    xor %= 65536;
    return xor;
}

int chk_val ( char sen[] )
{
    char xor[8] = { '\0' };
    int i = ( strchr( sen, '*' ) - sen ) + 1;
    for ( int k = 0; sen[i] != '\0'; k++, i++ )
    {
        xor[k] = sen[i];
    }

    int chkval;
    /*sscanf( xor, "%d", &chkval );*/
    chkval = (int)strtol( xor, NULL, 16 );

    return chkval;
}

int uct_to_bjt( char uct[] )
{
    int iuct = atoi( uct );
    int h = ( iuct / 10000 + 8 ) % 24;
    int bjt = h*10000 + iuct % 10000;
    return bjt;
}

