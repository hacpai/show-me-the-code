import java.util.Scanner;  

public class Main {
	public  static int IsPrime ( int n ) {
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
	public static void SolutDivisor( int n ) {
		int i = 2;
        System.out.print (  n + "=" );
        while ( n != 1 )
        {
            if ( n % i == 0 )
            {
                n /= i;
                System.out.print ( i );
                    if ( n != 1 )
                    {
                        System.out.print ( "x" );
                    }
                continue;
            }
            i++;
        }
	}
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();

        if ( IsPrime( n ) == 1 )
        {
            System.out.print (  n + "=" + n );
        }
        else
        {
            SolutDivisor ( n );
        }
    } 
}
