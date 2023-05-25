import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static final int MOD = 15746;
    //static int[][] dp = new int[1000001];
    static int[] arr;
    static long temp = 0;

    static int n, m;
    static ArrayList<String> list = new ArrayList<>();
    static Deque<Integer> queue = new ArrayDeque<>();

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
//        StringTokenizer st = new StringTokenizer(br.readLine());
    }

    private static void solve() {
        if (n == 1){
            answer.append("1/1");
            return;
        }

        int maxValue = 2;
        int a, b;
        boolean flag = true;
        a = 1;
        b = maxValue;
        for (int i = 2; i < n; i++) {
            if (flag) {
                if (b == 1) {
                    flag = false;
                    a += 1;
                }
                else {
                    a += 1;
                    b -= 1;
                }
            }
            else {
                if (a == 1) {
                    flag = true;
                    b += 1;
                }
                else {
                    b += 1;
                    a -= 1;
                }
            }
        }
        answer.append(a + "/" + b);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}