import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int F = in.nextInt();
        double C = (F-32)*5/9;
		System.out.println((int)C);
	}

}
