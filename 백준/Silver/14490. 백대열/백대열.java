import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    static int[] arr;
    static int n, m;

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String[] str = st.nextToken().split(":");
        n = Integer.parseInt(str[0]);
        m = Integer.parseInt(str[1]);
    }

    private static Integer gcd(Integer a, Integer b){
        if (a < b){
            Integer temp = a;
            a = b;
            b = temp;
        }
        while (b != 0){
            Integer temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    private static void solve() {
        Integer mod = gcd(n, m);
        n /= mod;
        m /= mod;
        answer.append(n + ":" + m);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}