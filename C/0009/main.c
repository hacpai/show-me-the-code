#include <stdio.h>
int main ()
{
    int exp;
    /*scanf( "%d", &exp );*/
    int coe;
    const int form_len = 101;
    int form[form_len];
    for ( int i = 0; i < sizeof(form)/sizeof(form[0]); i++ )
    {
        form[i] = 0;
    }
    int flag = 0;
    while ( scanf( "%d", &exp ) )
    {
        int store_rev = form_len - exp - 1;
        scanf( "%d", &coe );
        form[store_rev] += coe;
        if ( exp == 0 )
        {
            flag++;
        }
        if ( flag == 2 )
        {
            break;
        }
    }

    /*{*/
        /*for ( int i = 0; i < sizeof(form)/sizeof(form[0]); i++ )*/
        /*{*/
            /*printf ( "%d\t%d", i, form[i] );*/
            /*printf ( "\n" );*/
        /*}*/
    /*}*/
    int pre_form_value = 0;
    int mark = 0;
    for ( int i = 0; i < form_len; i++ )
    {
        int exp = form_len - 1 - i;

        if ( exp == 0 )
        {
            switch ( form[i] )
            {
                case 0:
                    if ( pre_form_value != 0 )
                    {
                        printf ( "+0" );
                    }
                    else
                    {
                        printf ( "%d", 0 );
                    }
                    break;
                default:
                    if ( form[i] > 0 )
                    {
                        printf ( "+%d", form[i] );
                    } 
            }
        }
        else 
        {
            switch ( form[i] )
            {
                case 0:
                    break;
                case 1:
                    if ( exp == 1 )
                    {
                        printf ( "+x" );
                    }
                    else
                    {
                        printf ( "+x%d", exp ); 
                    }
                    break;
                case -1: 
                    if ( exp == 1 )
                    {
                        printf ( "-x" );
                    }
                    else
                    {
                        printf ( "-x%d", exp );
                    }
                    break;
                default:
                    if ( form[i] > 0 && mark > 0 )
                    {
                        printf ( "+" );
                    }
                    if ( exp == 1 )
                    {
                        printf ( "%dx", form[i] );
                    }
                    else
                    {
                        printf ( "%dx%d", form[i], exp );
                    }
            }
            if ( form[i] != 0 )
            {
                pre_form_value = form[i];
                mark++;
            }
            
        }
    }
    return 0;
}
