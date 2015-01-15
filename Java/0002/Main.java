import java.util.Scanner;  

 
public class Main {
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner in = new Scanner(System.in);
        String sen = new String(in.nextLine());
        String bjt = new String();
        while ( sen.equals( "END" ) == false )
        {
            boolean isGPRMC = false;
	        boolean isVaild = false;
	        boolean isLoc = false;
	        
        	String [] words = sen.split( "," );
        	
        	if ( words[0].equals( "$GPRMC" ) )
        	{
        		isGPRMC = true;
        	}

        	
        	if ( words[2].equals( "A" ) )
        	{
        		isLoc = true;
        	}
        	
        	
	        int dataStart = sen.indexOf( '$' ) + 1;
	        int dataEnd = sen.indexOf( '*' );
//	        System.out.println( words[3].equals( "A" ) );
	        int xorVal = 'G' & 0xFFFF;
	        for ( int i = dataStart; i < dataEnd - dataStart ; i++ )
	        {
	        	xorVal ^= sen.charAt(i + 1);
	        }
	        
	        int vaildValStart = words[words.length-1].indexOf( '*' );
	        String vaildVal = words[words.length - 1].substring( vaildValStart + 1, vaildValStart + 3 );
	        
	        if ( xorVal == Integer.parseInt( vaildVal, 16 ) )
	        {
	        	isVaild = true;
	        }
//	        System.out.println( isGPRMC + "," + isLoc + "," +  isVaild );
	        if ( isGPRMC == true && isLoc == true && isVaild == true )
	        {
		        String utc = words[1].substring( 0, 6 );
		        int utc_hh = Integer.parseInt( utc.substring(0, 2));
		        int bjt_hh = ( utc_hh + 8 ) % 24;
//		        System.out.println(bjt_hh);
	
		        if ( bjt_hh > 9 )
		        {
		        	bjt = bjt_hh + ":" + utc.substring( 2, 4 ) + ":" + utc.substring( 4 );
		        }
		        else {
		        	bjt = "0" + bjt_hh + ":" + utc.substring( 2, 4 ) + ":" + utc.substring( 4 );
				}
	        }
	        sen = in.nextLine();

        }
        System.out.print( bjt );
    }
}

