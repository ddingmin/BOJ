import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    static long[][] dp = new long[91][2];
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
        //StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(br.readLine());
    }


    private static void solve() {
        dp[1][1] = 1;
        for (int i = 2; i < n + 1; i++) {
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
            dp[i][1] = dp[i - 1][0];
        }
        answer.append(dp[n][0] + dp[n][1]);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}