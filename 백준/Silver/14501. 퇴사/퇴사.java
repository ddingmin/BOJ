import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    static long[] dp = new long[16];
    static int[][] arr = new int[16][2];
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

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i + 1][0] = Integer.parseInt(st.nextToken());
            arr[i + 1][1] = Integer.parseInt(st.nextToken());
        }
    }


    private static void solve() {
        bt(0, 1);
        answer.append(temp);
    }

    private static void bt(long sum, int idx){
        updateAnswer(sum);
        for (int i = idx; i < n + 1; i++) {
            if (i + arr[i][0] - 1 < n + 1){
                bt(sum + arr[i][1], i + arr[i][0]);
            }
        }
    }

    private static void updateAnswer(long a) {
        if (a > temp){
            temp = a;
        }
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}