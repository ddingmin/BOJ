import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static int N = 0;
    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
    }

    private static void solve() {
        int temp;
        int ans = 0;
        int original;
        original = N;
        do {
            temp = 10 * (N % 10) + (N / 10 + N % 10) % 10;
            N = temp;
            ans += 1;
        } while (N != original);
        answer.append(ans);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
