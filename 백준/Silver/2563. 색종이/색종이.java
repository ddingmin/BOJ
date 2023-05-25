import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static final int MOD = 15746;
    //static int[][] dp = new int[1000001];
    static int[] arr;
    static int[][] map = new int[101][101];
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
        int a, b;
        for (int k = 0; k < n; k++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            for (int i = a; i < a + 10; i++) {
                for (int j = b; j < b + 10; j++) {
                    map[i][j] = 1;
                }
            }
        }
    }

    private static void solve() {
        int count = 0;
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (map[i][j] == 1){
                    count += 1;
                }
            }
        }
        answer.append(count);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}