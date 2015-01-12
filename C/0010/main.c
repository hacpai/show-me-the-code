#include <stdio.h>
 
int main ()
{
    int size;
    scanf( "%d", &size );
    int matrix[size][size];
 
    for ( int i = 0; i < size; i++ )
    {
        for ( int j = 0; j < size; j++ )
        {
            scanf( "%d", &matrix[i][j] );
        }
    }
 
/*    {*/
    /*for ( int i = 0; i < size; i++ )*/
    /*{*/
    /*for ( int j = 0; j < size; j++ )*/
    /*{*/
    /*printf ( "%d\t", matrix[i][j] );*/
    /*}*/
    /*printf ( "\n" );*/
    /*}*/
/*    }*/
 
    int row=0, col=0;
    int flag= 0;
 
    for ( int i = 0; i < size; i++ )
    {
        for ( int j = 0; j < size - 1; j++ )
        {
            if ( matrix[i][col] < matrix[i][j+1] )
            {
                col = j+1;
 
            }
        }
//        printf("%d\n", col);
        int count = 0;
        for ( int k = 0; k < size; k++ )
        {
            if ( matrix[i][col] < matrix[k][col] && matrix[i][col] != matrix[k][col]) {
                count++;
            }
            if ( count == size - 1)
            {
                printf("%d %d", i, col );
                flag = 1;
                goto OUT;
            }
        }
 
    }
    OUT:
        if ( flag == 0 )
        {
            printf("NO");
        }
    return 0;
}
