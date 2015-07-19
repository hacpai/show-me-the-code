import sun.net.ftp.FtpClient;

import java.security.Principal;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Fraction a = new Fraction(in.nextInt(), in.nextInt());
        Fraction b = new Fraction(in.nextInt(),in.nextInt());
        a.print();
        b.print();
        a.plus(b).print();
        a.multiply(b).plus(new Fraction(5,6)).print();
        a.print();
        b.print();
        in.close();
    }

}

class Fraction {

    public int n;
    public int d;
    public Fraction(int n, int d) {
        this.n = n;
        this.d = d;
    }

    public double toDouble() {
        double ret = this.n / this.d;
        return ret;
    }

    public Fraction plus(Fraction r) {
        return new Fraction(this.n*r.d+this.d*r.n, this.d*r.d);
    }

    public Fraction multiply(Fraction r) {
        return new Fraction(this.n * r.n, this.d * r.d);
    }

    public void print() {
        Fraction reduction = reduct(this.n, this.d);
        if (reduction.d == 1) {
            System.out.println(reduction.n);
        } else {
            System.out.println(reduction.n + "/" + reduction.d);
        }
    }

    public Fraction reduct(int n, int d) {
        return new Fraction(n/gcd(n, d), d/gcd(n, d));
    }

    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a%b);
        }
    }
}
