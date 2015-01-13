#include <stdio.h>
#include <string.h>

int main()
{
    char words[255];

    scanf ( "%[^\n]", words );
    int count = 0;
    char letter;
    for ( int i = 0; i < strlen( words ); i++ )
    {
        letter = words[i];
        if ( letter != ' ' && letter != '.' )
        {
            count++;
        }
        else 
        {
            if ( count == 0 )
            {
                ;
            }
            else
            {
                printf( "%d", count );
                if ( letter != '.' )
                {
                    printf( " " );
                }
            }
            
            count = 0;
        }
            
    }
    return 0;
}

