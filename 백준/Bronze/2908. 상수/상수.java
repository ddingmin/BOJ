import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int a, b;
        Scanner sc = new Scanner(System.in);
        StringBuffer n1 = new StringBuffer(sc.next());
        StringBuffer n2 = new StringBuffer(sc.next());
        a = Integer.parseInt(n1.reverse().toString());
        b = Integer.parseInt(n2.reverse().toString());

        if (a > b){
            System.out.println(a);
        }
        else{
            System.out.println(b);
        }
    }
}
