import java.util.Scanner;  
 
public class Main {
	public static int IsCompNum ( int n ) {
		int sum = 0;
        int is_comp_num;
        for ( int i = 1; i < n; i++ )    
        {
           if ( n % i == 0 )
           {
               sum += i;
           }
        }

        if ( n == sum )
        {
            is_comp_num = 1;
        }
        else
        {
            is_comp_num = 0;
        }
        return is_comp_num;
	}
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);

            int n = in.nextInt();
    		int m = in.nextInt();

            int flag = 0;
            int count = 0;
            for ( int i = n; i < m; i++ )
            {
                if ( IsCompNum( i ) == 1 )
                {
                    count++;
                    flag = 1;
                    if ( count == 1 )
                    {
                        System.out.printf ( "%d", i );
                    }
                    else
                    {
                        System.out.printf ( " %d", i );
                    }
                }
            }
            if ( flag == 0 )
            {
                System.out.printf ( "\n" );
            }
    } 
}
