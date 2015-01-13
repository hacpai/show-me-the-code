import java.util.Scanner;  

public class Main {
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);
        int count = 0;
        int flag = 0;
        char letter;
        String sentence = new String( in.nextLine() );
        sentence = sentence.trim();
        for ( int i = 0; i < sentence.length(); i++ )
        {
            letter = sentence.charAt(i);
            if ( letter != ' ' && letter != '.' )
            {
                count++;
            }
            else {
                if ( count == 0 )
                {
                    ;
                }
                else if ( flag == 0 )
                {
                    System.out.print( count );
                    flag++;
                }
                else
                {
                    System.out.print( " " + count );
                }
                count = 0;
            }
            
        }
    }
}
